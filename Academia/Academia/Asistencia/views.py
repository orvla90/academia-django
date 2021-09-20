from django.db.models import fields
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Asistencia
from django_pandas.io import read_frame


# Create your views here.
def home(request, *args, **kwargs):
    asistencia = read_frame(Asistencia.objects.all(), fieldnames=['fecha', 'alumno', 'horas'])
    asistencia['mes'] = asistencia['fecha'].map(lambda x: f"{x.year} {x.month}")
    asistencia = asistencia.loc[:,['mes', 'alumno', 'horas']]
    asistencia = asistencia.groupby(by=['mes', 'alumno']).sum().reset_index()



    context = {'asistencia':asistencia.to_html(index=False)}
    return render(request, 'asistencia/asistencia.html', context=context)

class CrearAsistencia(CreateView):
    model = Asistencia
    template_name = 'asistencia/crearAsistencia.html'
    fields = '__all__'
    success_url = reverse_lazy('asistenciaHome')