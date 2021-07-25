from django.urls import path

from . import views

app_name = 'lab_net'
urlpatterns = [
    path('', views.list, name='index'),
    path('add_pool/<ip_start>/<ip_end>/', views.add_range)
]
