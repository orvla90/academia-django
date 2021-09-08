from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='home2'),
    path('listado_alumnos/', views.ListadoAlumnos.as_view(), name="listadoalumnos"),
]