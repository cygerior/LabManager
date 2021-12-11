import ipaddress
import logging
from ipaddress import IPv4Address

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from macaddress.fields import MACAddressField


class Label(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class IntegerIPAddressField(models.Field):
    description = _("IP Address stored as integer")

    def get_internal_type(self):
        return 'IntegerField'

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)
        return value

    def get_prep_value(self, value):
        if value is not None:
            value = int(value)
        return value

    def from_db_value(self, value, _expression, _connection):
        if value is None:
            return value
        return ipaddress.ip_address(value)

    def to_python(self, value):
        logging.warning(f'to_python {value}')
        if isinstance(value, (ipaddress.IPv6Address, ipaddress.IPv4Address)):
            return value
        if value is None:
            return value

        return ipaddress.ip_address(value)


class Network(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def add_ip_range(self, ip_start: IPv4Address, ip_end: IPv4Address, labels: [Label] or None = None):
        NetworkAddress.add_range(self, ip_start, ip_end, labels)

    def __str__(self):
        return self.name


class NetworkAddress(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    ip = IntegerIPAddressField(unique=True)
    labels = models.ManyToManyField(Label)
    mac_address = MACAddressField(null=True, default=None, blank=True)

    @property
    def ip_type(self):
        return self.ip.__class__.__name__

    @property
    def ip_num(self):
        return int(self.ip)

    def label_list(self):
        return ", ".join([p.title for p in self.labels.all()])

    @classmethod
    def add_range(cls, network: Network, ip_start: IPv4Address, ip_end: IPv4Address, labels: [Label] or None = None):
        ip = ip_start
        while ip <= ip_end:
            entry = cls(network=network.pk, ip=ip)
            entry.save()
            ip = ip + 1

    class Meta:
        verbose_name_plural = 'Network addresses'
        constraints = [
            models.UniqueConstraint(fields=["network", "ip"], name="ln_unique_network_address"),
            models.UniqueConstraint(fields=["network", "mac_address"], name="ln_unique_network_mac_address")
        ]
        ordering = ["network", "ip"]

    def __str__(self):
        return f'{self.network} - {self.ip} - {self.mac_address}'


class Arp(models.Model):
    ip = models.ForeignKey(NetworkAddress, on_delete=models.CASCADE)
    mac = MACAddressField(null=True)
    date = models.DateTimeField(null=True)


def next_year():
    return timezone.now() + timezone.timedelta(days=365)


class Reservation(models.Model):
    ip = models.OneToOneField(NetworkAddress, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='ip_reservation',
        null=True
    )
    comment = models.TextField(blank=True, default='', null=True)
    release = models.DateField(default=next_year)
    datetime = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.ip}'
