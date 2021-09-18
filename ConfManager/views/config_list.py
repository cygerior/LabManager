from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from ConfManager.models import Configuration, Reservation


def config_list(request):
    return render(request, 'ConfManager/config_list.html', {'config_list': Configuration.objects.all()})


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'comment', 'release_date']


def edit_reservation(request, pk):
    rsv = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=rsv)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('conf_manager:index'))
    else:
        form = ReservationForm(instance=rsv)

    return render(request, 'ConfManager/reserve.html', {
        'form': form,
        'rsv': rsv
    })


def reserve(request, config_id):
    rsv = Reservation(configuration_id=config_id)
    try:
        rsv.save()
    except IntegrityError:
        return HttpResponseRedirect(reverse('conf_manager:index'))

    return HttpResponseRedirect(reverse('conf_manager:edit_reservation', kwargs={'pk': rsv.id}))


def release(request, pk):
    try:
        rsv = Reservation.objects.get(pk=pk)
        rsv.delete()
    except ObjectDoesNotExist:
        pass
    finally:
        return HttpResponseRedirect(reverse('conf_manager:index'))
