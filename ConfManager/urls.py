from django.urls import path

from ConfManager import views

app_name = 'conf_manager'
urlpatterns = [
    path('home', views.home, name='index'),
    path('config/<int:id_config>', views.view_config),
    path('date', views.date),
    path('add_rpc/<uri>/<int:out_count>', views.add_rpc),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]
