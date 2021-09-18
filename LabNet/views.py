from ipaddress import ip_address

from django.db import IntegrityError
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from LabNet.forms import AddPoolForm
from LabNet.models import Ip, Reservation


def list(request):
    return render(request, 'LabNet/list.html', {
        'iplist': Ip.objects.all(),'has_permission': True})


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


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'comment', 'release']


def edit_reservation(request, pk):
    rsv = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=rsv)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lab_net:index'))
    else:
        form = ReservationForm(instance=rsv)

    return render(request, 'LabNet/reserve.html', {
        'form': form,
        'rsv': rsv
    })


def reserve(request, ip_id):
    rsv = Reservation(ip_id=ip_id, user_id=request.user.id)
    try:
        rsv.save()
    except IntegrityError:
        return HttpResponseRedirect(reverse('lab_net:index'))

    return HttpResponseRedirect(reverse('lab_net:edit_reservation', kwargs={'pk': rsv.id}))


def release(request, pk):
    rsv = get_object_or_404(Reservation, pk=pk)
    rsv.delete()
    return HttpResponseRedirect(reverse('lab_net:index'))
