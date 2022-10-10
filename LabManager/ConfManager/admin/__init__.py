from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin
from polymorphic.admin import PolymorphicParentModelAdmin

from .power import PowerControllerAdmin
from .uart import UartConnectorAdmin, UartServerAdmin
from .backplane import BackplaneGroupAdmin, BackplaneSlotAdmin, BackplaneNetworkInterfaceAdmin
from .unit import UnitAdmin, UnitTypeAdmin, ModuleTypeAdmin, BoardTypeAdmin, DeviceAliasAdmin
from ..models import TestPlatform, Reservation, DeviceType, Interface, NetworkInterface, \
    UartInterface, BackplaneNetworkInterface, PowerSupply

admin.site.register(PowerSupply)
admin.site.register(TestPlatform)
admin.site.register(Reservation)

admin.site.register(DeviceType)


@admin.register(Interface)
class InterfaceAdmin(PolymorphicParentModelAdmin):
    base_model = Interface
    child_models = [NetworkInterface, UartInterface, BackplaneNetworkInterface]


@admin.register(NetworkInterface)
class NetworkInterfaceAdmin(PolymorphicChildModelAdmin):
    base_model = Interface


@admin.register(UartInterface)
class UartInterfaceAdmin(PolymorphicChildModelAdmin):
    base_model = Interface
