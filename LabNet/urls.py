from django.urls import path

from . import views

app_name = 'lab_net'
urlpatterns = [
    path('', views.list, name='index'),
    path('add_pool', views.post_add_pool, name='add_pool'),
    path('reserve/<int:ip_id>', views.reserve, name='reserve'),
    path('reserve/edit/<int:pk>', views.edit_reservation, name='edit_reservation'),
    path('release/<int:pk>', views.release, name='release')
]
