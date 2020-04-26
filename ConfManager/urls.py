from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('config/<int:id_config>', views.view_config),
    path('date', views.date),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]