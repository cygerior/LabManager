from django.urls import path

from ConfManager import views

app_name = 'conf_manager'

urlpatterns = [
    path('home', views.config_list, name='index'),
    path('reserve/<int:config_id>', views.reserve, name='reserve'),
    path('reserve/edit/<int:pk>', views.edit_reservation, name='edit_reservation'),
    path('release/<int:pk>', views.release, name='release'),
    path('config/<int:pk>', views.view_config, name='config'),
    path('rpc/add/<str:uri>/<int:output_start>/<int:output_end>', views.add_rpc, name='add_rpc'),
    path('rpc/add', views.add_rpc_form, name='add_rpc_form'),
    path('rpc/del/<int:pk>', views.del_rpc, name='del_rpc'),
    path('rpc', views.PowerListView.as_view(), name='rpc_list'),
]
