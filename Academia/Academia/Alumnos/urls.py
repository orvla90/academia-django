from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='alumnoshome'),
    path('listadoalumnos/', views.ListadoAlumnos.as_view(), name="listadoalumnos"),
    path('crearalumno/', views.CrearAlumno.as_view(), name='crearalumno'),
    path('editaralumno/<pk>', views.EditarAlumno.as_view(), name='editaralumno'),
    path('eliminaralumno/<pk>', views.EliminarAlumno.as_view(), name='eliminaralumno'),
]