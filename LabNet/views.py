from ipaddress import ip_address

from django.shortcuts import render

from LabNet.models import IpPool


# Create your views here.

def list(request):
    return render(request, 'LabNet/List.html', {'iplist': IpPool.objects.all()})


def add_range(request, ip_start, ip_end):
    IpPool.add_range(ip_address(ip_start), ip_address(ip_end))
    return render(request, 'LabNet/add_range.html', locals())
