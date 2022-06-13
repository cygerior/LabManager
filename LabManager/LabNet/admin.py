from ipaddress import ip_address

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Reservation, Label, NetworkAddress, Network

admin.site.register(Reservation)
admin.site.register(Label)


class IpResource(resources.ModelResource):
    class Meta:
        model = NetworkAddress
        fields = ('id', 'ip', 'comment',)


admin.site.register(Network)


@admin.register(NetworkAddress)
class IpAdmin(ImportExportModelAdmin):
    resource_class = IpResource
    list_display = ('network', 'ip', 'label_list')
    list_filter = ('network', 'labels')
    ordering = ('network', 'ip')

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
        return redirect(reverse('index'))

    def add_range(self, request, ip_start, ip_end):
        NetworkAddress.add_range(ip_address(ip_start), ip_address(ip_end))
        return redirect(reverse('index'))

    change_list_template = "admin/LabNet/ippool/change_list.html"
