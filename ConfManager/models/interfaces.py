from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from polymorphic.models import PolymorphicModel


class Interface(PolymorphicModel):
    name = models.CharField(max_length=30, unique=True)
    device = models.ForeignKey('Device', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class BaseNetworkInterface(Interface):

    network_address = models.OneToOneField(
        "NetworkAddress",
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Net - {self.name} - {self.network} - {self.network_address}'


class NetworkInterface(BaseNetworkInterface):
    mac_address = models.CharField(max_length=23)


class BackplaneNetworkInterface(BaseNetworkInterface):

    backplane = models.ForeignKey("BackplaneSlot", on_delete=models.CASCADE)
    device_number = models.IntegerField()

    @property
    def mac_address(self):
        return f'02:00:00:{self.backplane.slot_number:02x}:{self.backplane.domain_id:02x}:{self.device_number:02x}'


class UartInterface(Interface):
    uri = models.CharField(max_length=30)
