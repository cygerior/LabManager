from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *

admin.site.register(Label)


class IpResource(resources.ModelResource):
    class Meta:
        model = IpPool
        fields = ('id', 'ip', 'comment',)


@admin.register(IpPool)
class IpAdmin(ImportExportModelAdmin):
    resource_class = IpResource
    list_display = ('ip', 'label_list', 'comment')
    list_filter = ('labels',)
    ordering = ('ip',)

    def get_urls(self):
        urls = super().get_urls()

        my_urls = [
            path(
                'evilUrl/',
                self.admin_site.admin_view(self.do_evil_view)
            )
        ]
        return my_urls + urls

    def do_evil_view(self, request):
        print('doing evil')
        return redirect('/lab_manager/admin/LabNet/ippool/')

    def add_range(self, request, ip_start, ip_end):
        IpPool.add_range(ip_address(ip_start), ip_address(ip_end))
        return render(request, 'LabNet/add_range.html', locals())

    change_list_template = "admin/LabNet/ippool/change_list.html"