from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='homepadres'),
    path('listadopadres/', views.ListadoPadres.as_view(), name="listadopadres"),
]