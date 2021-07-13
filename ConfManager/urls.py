from django.urls import path

from ConfManager import views

urlpatterns = [
    path('home', views.home),
    path('config/<int:id_config>', views.view_config),
    path('date', views.date),
    path('add_rpc/<uri>/<int:out_count>', views.add_rpc),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]
