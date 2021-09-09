from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from .models import Profesores
from django.views.generic.edit import CreateView, DeleteView, UpdateView


# Create your views here.
def Home(request):
    return(render(request, 'Profesores/home.html'))

class ListadoProfesores(ListView):
    model = Profesores
    template_name = 'Profesores/ListadoProfesores.html'

class CrearProfesor(CreateView):
    model = Profesores
    template_name = 'Profesores/crearprofesor.html'
    fields = ['nombre', 'apellidos', 'telefono', 'mail']
    success_url = reverse_lazy('listadoprofesores')

class EditarProfesor(UpdateView):
    model = Profesores
    template_name = 'Profesores/editarprofesor.html'
    fields = ['nombre', 'apellidos', 'telefono', 'mail']
    success_url = reverse_lazy('listadoprofesores')

class EliminarProfesor(DeleteView):
    model = Profesores
    template_name = 'Profesores/eliminarprofesor.html'
    success_url = reverse_lazy('listaprofesores')