from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Pagos
from django.urls.base import reverse_lazy
from django_pandas.io import read_frame
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

def hacerFacturas(request):
    pagos = Pagos.objects.all()
    df = read_frame(pagos, fieldnames=['fecha', 'cantidad', 'padre', 'numeroFactura'])
    years = df.sort_values('fecha').reset_index()
    primeraFactura = years.iloc[0]
    fechaPrimeraFactura = primeraFactura['fecha'].year
    numeroFacturas = 1
    years['numeroFactura'][0] = f"{numeroFacturas}-{fechaPrimeraFactura}"
    if(len(years) > 1):
        for factura in years.index[1:]:
            if(years['fecha'][factura].year == fechaPrimeraFactura):
                numeroFacturas += 1
                years['numeroFactura'][factura] = f"{numeroFacturas}-{fechaPrimeraFactura}"
            else:
                fechaPrimeraFactura = years['fecha'][factura].year
                numeroFacturas = 1
                years['numeroFactura'][factura] = f"{numeroFacturas}-{fechaPrimeraFactura}"
    years.to_excel('Academia/static/files/facturas.xlsx')
    return(render(request, 'Pagos/facturas.html', context={'df':years.to_html(index=False)}))

