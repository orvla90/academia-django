from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Pagos
from django.urls.base import reverse_lazy
# Create your views here.
def home(request):
    return render(request, 'Pagos/home.html')

class ListadoPagos(ListView):
    model = Pagos
    template_name = 'Pagos/listadopagos.html'

class CrearPago(CreateView):
    model = Pagos
    template_name = 'Pagos/crearpago.html'
    fields = ['fecha', 'cantidad', 'padre']
    success_url = reverse_lazy('listadopagos')

class EditarPago(UpdateView):
    model = Pagos
    template_name = 'Pagos/editarpago.html'
    fields = ['fecha', 'cantidad', 'padre']
    success_url = reverse_lazy('listadopagos')

class EliminarPago(DeleteView):
    model = Pagos
    template_name = 'Pagos/eliminarpago.html'
    success_url = reverse_lazy('listadopagos')