from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='homeprofesores'),
    path('listadoprofesores/', views.ListadoProfesores.as_view(), name="listadoprofesores"),
]