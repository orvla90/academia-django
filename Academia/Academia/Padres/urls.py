from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='homepadres'),
    path('listadopadres/', views.ListadoPadres.as_view(), name="listadopadres"),
    path('crearpadre/', views.CrearPadre.as_view(), name="crearpadre"),
    path('editarpadre/<pk>', views.EditarPadre.as_view(), name='editarpadre'),
    path('eliminarpadre/<pk>', views.EliminarPadre.as_view(), name="eliminarpadre"),
]