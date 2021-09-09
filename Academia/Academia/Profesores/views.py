from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Profesores

# Create your views here.
def Home(request):
    return(render(request, 'Profesores/home.html'))

class ListadoProfesores(ListView):
    model = Profesores
    template_name = 'Profesores/ListadoProfesores.html'