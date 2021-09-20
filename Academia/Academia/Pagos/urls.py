from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='pagoshome'),
    path('listadopagos/', views.ListadoPagos.as_view(), name='listadopagos'),
    path('crearpago/', views.CrearPago.as_view(), name='crearpago'),
    path('editarpago/<pk>/', views.EditarPago.as_view(), name='editarpago'),
    path('eliminarpago/<pk>/', views.EliminarPago.as_view(), name='eliminarpago'),
    path('facturas/', views.hacerFacturas, name='facturas'),
]