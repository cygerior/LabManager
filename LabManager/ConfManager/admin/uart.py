from django.contrib import admin

from ConfManager.forms.multi_port import MultiPortForm
from ConfManager.models import UartPort, UartServer, UartGroup, UartGroupEntry

admin.site.register(UartPort)


@admin.register(UartServer)
class UartServerAdmin(admin.ModelAdmin):
    form = MultiPortForm
    pass

class UartGroupEntryInline(admin.TabularInline):
    model = UartGroupEntry
    extra = 1


@admin.register(UartGroup)
class UartConnectorAdmin(admin.ModelAdmin):
    inlines = (UartGroupEntryInline, )
