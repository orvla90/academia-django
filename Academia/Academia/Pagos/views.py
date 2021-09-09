from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Pagos
# Create your views here.
def home(request):
    return render(request, 'Pagos/home.html')

class ListadoPagos(ListView):
    model = Pagos
    template_name = 'Pagos/listadopagos.html'