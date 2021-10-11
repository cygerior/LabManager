from django.db import models
from macaddress.fields import MACAddressField


class Network(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class NetworkAddress(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    mac = MACAddressField(null=True)

    def __str__(self):
        return f'{self.network} - {self.ip} - {self.mac}'

    class Meta:
        verbose_name_plural = 'Network addresses'
        constraints = [
            models.UniqueConstraint(fields=["network", "ip", "mac"], name="unique_network_address")
        ]
