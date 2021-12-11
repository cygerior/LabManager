from builtins import property

from django.db import models
from macaddress.fields import MACAddressField
from polymorphic.models import PolymorphicModel

from LabNet.models import NetworkAddress


class Interface(PolymorphicModel):
    name = models.CharField(max_length=30, unique=True)
    device = models.ForeignKey('Device', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class NetworkInterface(Interface):
    network = models.OneToOneField(
        "LabNet.Network",
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
    )
    mac_address = MACAddressField(null=False)

    @property
    def network_address(self):
        return NetworkAddress(network=self.network, mac_address=self.mac_address)

    def __str__(self):
        return f'Net - {self.name} - {self.network} - {self.network_address.ip}'


class BackplaneNetworkInterface(Interface):

    backplane = models.ForeignKey("BackplaneSlot", on_delete=models.CASCADE)
    device_number = models.IntegerField()

    @property
    def mac_address(self):
        """ For instance 02:40:43:80:12:01 """
        return f'02:40:43:{self.backplane.slot_number:02x}:{self.backplane.domain_id:02x}:{self.device_number:02x}'


class UartInterface(Interface):
    uri = models.CharField(max_length=30)
