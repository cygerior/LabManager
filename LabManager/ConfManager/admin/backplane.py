from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin

from ConfManager.models import BackplaneSlot, BackplaneGroup, BackplaneNetworkInterface, Interface


@admin.register(BackplaneSlot)
class BackplaneSlotAdmin(admin.ModelAdmin):
    list_display = ['controller', 'port_number', 'power']
    list_filter = ['controller']


@admin.register(BackplaneGroup)
class BackplaneGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(BackplaneNetworkInterface)
class BackplaneNetworkInterfaceAdmin(PolymorphicChildModelAdmin):
    base_model = Interface