from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from .models import *
from .models.interfaces import NetworkInterface, UartInterface


class RackInline(admin.TabularInline):
    model = RackSlot
    extra = 1


class DeviceInline(admin.TabularInline):
    model = Device
    extra = 1


class RackAdmin(admin.ModelAdmin):
    inlines = (RackInline, )


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    inlines = (RackInline, DeviceInline)


class PowerSupplyInline(admin.TabularInline):
    model = PowerSupply
    extra = 1


@admin.register(PowerController)
class PowerControllerAdmin(admin.ModelAdmin):
    inlines = (PowerSupplyInline, )


admin.site.register(BoardType)
admin.site.register(Configuration)
admin.site.register(Resource)
admin.site.register(Reservation)
admin.site.register(Rack, RackAdmin)
admin.site.register(Device)
admin.site.register(Label)
admin.site.register(ModuleDefinition)
admin.site.register(BoardDefinition)

@admin.register(Interface)
class InterfaceAdmin(PolymorphicParentModelAdmin):
    base_model = Interface
    child_models = [NetworkInterface, UartInterface]


@admin.register(NetworkInterface)
class NetworkInterfaceAdmin(PolymorphicChildModelAdmin):
    base_model = NetworkInterface


@admin.register(UartInterface)
class UartInterfaceAdmin(PolymorphicChildModelAdmin):
    base_model = UartInterface

