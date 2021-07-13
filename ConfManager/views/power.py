from django.shortcuts import render

from ConfManager.models import PowerController


def add_rpc(request, uri, out_count):
    rpc = PowerController.new(uri, out_count)
    return render(request, 'ConfManager/add_rpc.html', locals())
