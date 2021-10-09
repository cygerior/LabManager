from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from .models import *


class DeviceInline(admin.TabularInline):
    model = Device
    extra = 1


class BoardTypeDeviceAliasInline(admin.TabularInline):
    model = BoardTypeDeviceAlias
    extra = 0
    show_change_link = False


class BackplaneSlotInline(admin.TabularInline):
    model = BackplaneSlot
    extra = 8






@admin.register(Unit)
class BoardAdmin(admin.ModelAdmin):
    inlines = (DeviceInline, )


class PowerSupplyInline(admin.TabularInline):
    model = PowerSupply
    extra = 1


@admin.register(PowerController)
class PowerControllerAdmin(admin.ModelAdmin):
    inlines = (PowerSupplyInline,)


@admin.register(UnitType)
class UnitTypeAdmin(PolymorphicParentModelAdmin):
    base_model = UnitType
    child_models = [BoardType, ModuleType]


@admin.register(BoardType)
class BoardTypeAdmin(PolymorphicChildModelAdmin):
    base_model = UnitType
    inlines = (BoardTypeDeviceAliasInline, )


@admin.register(ModuleType)
class ModuleTypeAdmin(PolymorphicChildModelAdmin):
    base_model = UnitType


admin.site.register(PowerSupply)
admin.site.register(TestPlatform)
admin.site.register(Resource)
admin.site.register(Reservation)
admin.site.register(Label)

admin.site.register(DeviceType)


@admin.register(BoardTypeDeviceAlias)
class DeviceAliasAdmin(admin.ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass

admin.site.register(BackplaneSlot)


@admin.register(BackplaneGroup)
class BackplaneGroupAdmin(admin.ModelAdmin):
    inlines = (BackplaneSlotInline,)


@admin.register(Interface)
class InterfaceAdmin(PolymorphicParentModelAdmin):
    base_model = Interface
    child_models = [NetworkInterface, UartInterface, BackplaneNetworkInterface]


@admin.register(NetworkInterface)
class NetworkInterfaceAdmin(PolymorphicChildModelAdmin):
    base_model = Interface
    list_display = ('name', 'address')
    fields = (('name', 'mac_address'), 'address')


@admin.register(UartInterface)
class UartInterfaceAdmin(PolymorphicChildModelAdmin):
    base_model = Interface


@admin.register(BackplaneNetworkInterface)
class UartInterfaceAdmin(PolymorphicChildModelAdmin):
    base_model = Interface
