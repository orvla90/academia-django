from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='pagoshome'),
    path('listadopagos/', views.ListadoPagos.as_view(), name='listadopagos'),
]