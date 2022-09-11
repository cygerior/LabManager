from django.contrib import admin

from ConfManager.models import PowerSupply, PowerController


class PowerSupplyInline(admin.TabularInline):
    model = PowerSupply
    extra = 8


@admin.register(PowerController)
class PowerControllerAdmin(admin.ModelAdmin):
    inlines = (PowerSupplyInline, )
