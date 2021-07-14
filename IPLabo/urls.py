from django.urls import path

from . import views

urlpatterns = [
    path('', views.list),
    path('add_pool/<ip_start>/<ip_end>/', views.add_range)
]
