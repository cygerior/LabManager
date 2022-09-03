from ConfManager.models import PowerController
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView


class PowerAddForm(forms.Form):
    uri = forms.CharField(max_length=100)
    output_start = forms.IntegerField(min_value=1)
    output_end = forms.IntegerField(min_value=1)


def add_rpc_form(request):
    if request.method == 'POST':
        form = PowerAddForm(request.POST)
        if form.is_valid():
            return add_rpc(request, **form.cleaned_data)
    else:
        form = PowerAddForm()

    return render(request, 'ConfManager/add_rpc_form.html', {
        'form': form,
    })


def del_rpc(_request, pk):
    controller = get_object_or_404(PowerController, pk=pk)
    controller.delete()
    return HttpResponseRedirect(reverse('conf_manager:rpc_list'))


def add_rpc(_request, uri, output_start, output_end):
    PowerController.new(uri, output_start, output_end)
    return HttpResponseRedirect(reverse('conf_manager:rpc_list'))


class PowerListView(ListView):
    model = PowerController


class PowerListView(ListView):
    model = PowerController
