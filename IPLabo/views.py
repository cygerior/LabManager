from ipaddress import ip_address

from django.shortcuts import render
from IPLabo.models import IpPool


# Create your views here.

def list(request):
    return render(request, 'IPLabo/List.html', {'iplist': IpPool.objects.all()})


def add_range(request, ip_start, ip_end):
    IpPool.add_range(ip_address(ip_start), ip_address(ip_end))
    return render(request, 'IPLabo/add_range.html', locals())