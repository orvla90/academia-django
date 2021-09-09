from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='homeprofesores'),
    path('listadoprofesores/', views.ListadoProfesores.as_view(), name="listadoprofesores"),
    path('crearprofesor/', views.CrearProfesor.as_view(), name="crearprofesor"),
    path('editarprofesor/<pk>', views.EditarProfesor.as_view(), name="editarprofesor"),
    path('eliminarprofesor/<pk>', views.EliminarProfesor.as_view(), name='eliminarprofesor'),
]