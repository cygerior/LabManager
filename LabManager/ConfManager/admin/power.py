from django.contrib import admin

from ConfManager.forms.multi_port import MultiPortForm
from ConfManager.models import PowerController


@admin.register(PowerController)
class PowerControllerAdmin(admin.ModelAdmin):
    form = MultiPortForm
