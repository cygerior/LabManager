from ipaddress import ip_address

from django.shortcuts import render

from LabNet.models import Ip


def list(request):
    return render(request, 'LabNet/list.html', {'iplist': Ip.objects.all()})


def add_range(request, ip_start, ip_end):
    Ip.add_range(ip_address(ip_start), ip_address(ip_end))
    return render(request, 'LabNet/add_range.html', locals())
