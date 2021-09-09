from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Alumnos
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
# Create your views here.

def Home(request):
    
    return render(request, 'alumnos/home.html')

class ListadoAlumnos(ListView):
    model = Alumnos
    template_name = "alumnos/listado_alumnos.html"

class CrearAlumno(CreateView):
    model = Alumnos
    template_name = 'alumnos/crearalumno.html'
    fields = ['nombre', 'apellidos', 'curso', 'padre', 'telefono', 'mail', 'profesor']
    success_url = reverse_lazy('listadoalumnos')

class EditarAlumno(UpdateView):
    model = Alumnos
    template_name = 'alumnos/editaralumno.html'
    fields = ['nombre', 'apellidos', 'curso', 'padre', 'telefono', 'mail', 'profesor']

class EliminarAlumno(DeleteView):
    model = Alumnos
    template_name = 'alumnos/eliminaralumno.html'
    success_url = reverse_lazy('listadoalumnos')