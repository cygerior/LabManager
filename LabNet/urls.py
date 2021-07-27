from django.urls import path

from . import views

app_name = 'lab_net'
urlpatterns = [
    path('', views.list, name='index'),
    path('add_pool', views.post_add_pool, name='add_pool')
]
