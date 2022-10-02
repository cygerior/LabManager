from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from ConfManager.models import Device, BoardTypeDeviceAlias, Unit, UnitType, BoardType, ModuleType


class DeviceInline(admin.TabularInline):
    model = Device
    extra = 1


class BoardTypeDeviceAliasInline(admin.TabularInline):
    model = BoardTypeDeviceAlias
    extra = 4
    show_change_link = False


class BoardTypeModuleInline(admin.StackedInline):
    model = ModuleType
    fk_name = 'board'
    extra = 1


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


@admin.register(UnitType)
class UnitTypeAdmin(PolymorphicParentModelAdmin):
    base_model = UnitType
    child_models = [BoardType, ModuleType]


@admin.register(BoardType)
class BoardTypeAdmin(PolymorphicChildModelAdmin):
    base_model = UnitType
    inlines = (BoardTypeModuleInline, BoardTypeDeviceAliasInline)


@admin.register(ModuleType)
class ModuleTypeAdmin(PolymorphicChildModelAdmin):
    base_model = UnitType


@admin.register(BoardTypeDeviceAlias)
class DeviceAliasAdmin(admin.ModelAdmin):
    pass


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass
