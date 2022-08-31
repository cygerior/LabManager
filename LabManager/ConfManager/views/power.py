from django import forms, views
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.forms import ModelForm, Form
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from ConfManager.models import PowerController


class PowerAddForm(forms.Form):
    uri = forms.CharField(max_length=100)
    count = forms.IntegerField(min_value=1)


def add_rpc_form(request):
    if request.method == 'POST':
        form = PowerAddForm(request.POST)
        if form.is_valid():
            PowerController.new(form.cleaned_data['uri'], form.cleaned_data['count'])
            return HttpResponseRedirect(reverse('conf_manager:rpc_list'))
    else:
        form = PowerAddForm()

    return render(request, 'ConfManager/add_rpc_form.html', {
        'form': form,
    })


def add_rpc(request, uri, out_count):
    rpc = PowerController.new(uri, out_count)
    return render(request, 'ConfManager/add_rpc.html', locals())


class PowerListView(ListView):
    model = PowerController
