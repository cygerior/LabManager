from django.contrib import admin

from ConfManager.models import UartPort, UartServer, UartGroup, UartGroupEntry


admin.site.register(UartPort)


class UartInline(admin.TabularInline):
    model = UartPort
    extra = 1


@admin.register(UartServer)
class UartServerAdmin(admin.ModelAdmin):
    inlines = (UartInline, )


class UartGroupEntryInline(admin.TabularInline):
    model = UartGroupEntry
    extra = 1


@admin.register(UartGroup)
class UartConnectorAdmin(admin.ModelAdmin):
    inlines = (UartGroupEntryInline, )
