from django.urls import path

from ConfManager import views

app_name = 'conf_manager'
urlpatterns = [
    path('home', views.config_list, name='index'),
    path('reserve/<int:config_id>', views.reserve, name='reserve'),
    path('reserve/edit/<int:pk>', views.edit_reservation, name='edit_reservation'),
    path('release/<int:pk>', views.release, name='release'),
    path('config/<int:pk>', views.view_config, name='config'),
    path('rpc/add/<str:uri>/<int:out_count>', views.add_rpc, name='add_rpc')
]
