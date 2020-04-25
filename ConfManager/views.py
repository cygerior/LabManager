import datetime
from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("""
    <h1>Welcome to Lab Configuration Manager</h1>
    <p>Configurations</p>
    """)


def view_config(request, id_config):
    if id_config > 100:
        raise Http404
    return HttpResponse("Vous avez demandé à voir la config #{}".format(id_config))


def date(request):
    return render(request, 'ConfManager/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'ConfManager/addition.html', locals())