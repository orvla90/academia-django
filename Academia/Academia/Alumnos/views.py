from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Alumnos
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
from django.db.models import Count
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
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
    success_url = reverse_lazy('listadoalumnos')

class EliminarAlumno(DeleteView):
    model = Alumnos
    template_name = 'alumnos/eliminaralumno.html'
    success_url = reverse_lazy('listadoalumnos')

def informacionAlumnos(request, *args, **kwargs):
    qs = Alumnos.objects.all()
    totalAlumnos = qs.count()
    if( totalAlumnos > 0 ):
        cursos = Alumnos.objects.values('curso', entries=Count('curso')).all()
        xdata = []
        ydata = []
        for curso in cursos:
            curso['porcentaje'] = curso['entries'] / totalAlumnos * 100
            xdata.append(curso['curso'])
            ydata.append(curso['entries'])
    
    # Datos para el grafico de prueba
    
    fig1, ax1 = plt.subplots()
    ax1.pie(ydata, labels=xdata, autopct='%1.2f%%')
    plt.savefig('Academia/static/img/piechart.png', dpi=100)
    # Terminan las pruebas

    context = {
        'totalalumnos':totalAlumnos,
        'cursos':cursos,
        }
    return render(request, 'alumnos/informacionalumnos.html', context=context)