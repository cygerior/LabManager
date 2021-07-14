from ipaddress import IPv4Address

from django.db import models
from macaddress.fields import MACAddressField


class Label(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class IpPool(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    labels = models.ManyToManyField(Label)
    comment = models.TextField(blank=True, default='', null=True)

    def label_list(self):
        return ", ".join([p.title for p in self.labels.all()])

    @classmethod
    def add_range(cls, ip_start: IPv4Address, ip_end: IPv4Address):
        ip = ip_start
        while ip <= ip_end:
            entry = cls(ip=str(ip), comment=None)
            entry.save()
            ip = ip + 1

    def __str__(self):
        return self.ip


class Arp(models.Model):
    ip = models.ForeignKey(IpPool, on_delete=models.CASCADE)
    mac = MACAddressField(null=True)
    date = models.DateTimeField(null=True)


class NetInterface(models.Model):
    title = models.CharField(max_length=120)
    mac_address = MACAddressField(null=True)
    comment = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title


class IpReservation(models.Model):
    ip_ref = models.OneToOneField(IpPool, on_delete=models.CASCADE)
    interface_ref = models.OneToOneField(NetInterface, on_delete=models.CASCADE)
    release = models.DateTimeField(null=True)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_ref.ip
