from django.shortcuts import render
from .models import ListadoAlumnos
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
# Create your views here.

def Home(request):
    
    return render(request, 'alumnos/home.html')

class ListadoAlumnos(ListView):
    model = ListadoAlumnos
    template_name = "alumnos/listado_alumnos.html"