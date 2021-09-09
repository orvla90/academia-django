from django.http.response import Http404
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from .models import Padres
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404

# Create your views here.
def Home(request):
    try:
        encontrar_padre = Padres.onjects.get(pk=1)
    except Padres.DoesNotExist:
        raise Http404()
    context = {'Padre': encontrar_padre}
    return render(request, 'padres/home.html', context)

class ListadoPadres(ListView):
    model = Padres
    template_name = 'Padres/listadopadres.html'

class CrearPadre(CreateView):
    model = Padres
    template_name = 'Padres/crearpadre.html'
    fields = ['nombre', 'apellidos', 'dni', 'telefono', 'mail']
    success_url = reverse_lazy('listadopadres')

class EditarPadre(UpdateView):
    model = Padres
    template_name = 'Padres/editarpadre.html'
    fields = ['nombre', 'apellidos', 'dni', 'telefono', 'mail']
    success_url = reverse_lazy('listadopadres')

class EliminarPadre(DeleteView):
    model = Padres
    template_name = 'Padres/eliminarpadre.html'
    success_url = reverse_lazy('listadopadres')