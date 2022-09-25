from django.contrib import admin

from ConfManager.models import UartPort, UartServer, UartGroup, UartGroupEntry
from ConfManager.forms.uart import UartForm

admin.site.register(UartPort)


@admin.register(UartServer)
class UartServerAdmin(admin.ModelAdmin):
    form = UartForm


class UartGroupEntryInline(admin.TabularInline):
    model = UartGroupEntry
    extra = 1


@admin.register(UartGroup)
class UartConnectorAdmin(admin.ModelAdmin):
    inlines = (UartGroupEntryInline, )
