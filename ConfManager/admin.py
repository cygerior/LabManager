from django.contrib import admin
from .models import *


class RackInline(admin.TabularInline):
    model = RackSlot
    extra = 1


class RackAdmin(admin.ModelAdmin):
    inlines = (RackInline, )


class BoardAdmin(admin.ModelAdmin):
    inlines = (RackInline,)


class PowerSupplyInline(admin.TabularInline):
    model = PowerSupply
    extra = 1


@admin.register(PowerController)
class PowerControllerAdmin(admin.ModelAdmin):
    inlines = (PowerSupplyInline, )


admin.site.register(Board, BoardAdmin)
admin.site.register(BoardType)
admin.site.register(Configuration)
admin.site.register(Resource)
admin.site.register(Reservation)
admin.site.register(Rack, RackAdmin)

admin.site.register(Label)


