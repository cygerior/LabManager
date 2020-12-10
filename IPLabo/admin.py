from django.contrib import admin
from import_export import resources

from .models import *

# Register your models here.

from import_export.admin import ImportExportModelAdmin


class IpResource(resources.ModelResource):

    class Meta:
        model = IpPool
        fields = ('id', 'ip', 'comment',)


class IpAdmin(ImportExportModelAdmin):
    resource_class = IpResource


admin.site.register(IpPool, IpAdmin)
