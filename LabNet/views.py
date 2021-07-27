from ipaddress import ip_address

from django.shortcuts import render

from LabNet.forms import AddPoolForm
from LabNet.models import Ip


def list(request):
    return render(request, 'LabNet/list.html', {'iplist': Ip.objects.all()})


def add_range(request, ip_start, ip_end):
    Ip.add_range(ip_address(ip_start), ip_address(ip_end))
    return render(request, 'LabNet/add_range.html', locals())


def post_add_pool(request):
    if request.method == 'POST':
        form = AddPoolForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Ip.add_range(ip_address(cd['ip_start']), ip_address(cd['ip_end']))
    else:
        form = AddPoolForm()
    return render(request, 'LabNet/add_range.html', {
        'form': form
    })
