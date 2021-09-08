from django.shortcuts import render
from django.views.generic import ListView
from .models import Padres
# Create your views here.
def Home(request):
    return render(request, 'padres/home.html')

class ListadoPadres(ListView):
    model = Padres
    template_name = 'Padres/listadopadres.html'
    