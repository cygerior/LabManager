from django.urls import path

import ConfManager.views.addition
import ConfManager.views.home

urlpatterns = [
    path('home', ConfManager.views.home),
    path('config/<int:id_config>', ConfManager.views.view_config),
    path('date', ConfManager.views.date),
    path('addition/<int:nombre1>/<int:nombre2>/', ConfManager.views.addition)
]
