import ipaddress
import logging
from ipaddress import IPv4Address

from django.db import models
from django.utils import timezone
from macaddress.fields import MACAddressField
from django.utils.translation import gettext_lazy as _


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


class Ip(models.Model):
    ip = IntegerIPAddressField(unique=True)
    labels = models.ManyToManyField(Label)

    @property
    def ip_type(self):
        return self.ip.__class__.__name__

    @property
    def ip_num(self):
        return int(self.ip)

    def label_list(self):
        return ", ".join([p.title for p in self.labels.all()])

    @classmethod
    def add_range(cls, ip_start: IPv4Address, ip_end: IPv4Address):
        ip = ip_start
        while ip <= ip_end:
            entry = cls(ip=ip, comment=None)
            entry.save()
            ip = ip + 1

    def __str__(self):
        return str(self.ip)


class Arp(models.Model):
    ip = models.ForeignKey(Ip, on_delete=models.CASCADE)
    mac = MACAddressField(null=True)
    date = models.DateTimeField(null=True)


def next_year():
    return timezone.now() + timezone.timedelta(days=365)


class Reservation(models.Model):
    ip = models.OneToOneField(Ip, on_delete=models.CASCADE, primary_key=True)
    comment = models.TextField(blank=True, default='', null=True)
    release = models.DateTimeField(default=next_year)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ip}'
