from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from Padres import models as padresmodels
from Profesores import models as profesoresmodels

# Create your models here.
opcionescurso = [('1P', '1 Primaria'),
                ('2P', '2 Primaria'),
                ('3P', '3 Primaria'),
                ('4P', '4 Primaria'),
                ('5P', '5 Primaria'),
                ('6P', '6 Primaria'),
                ('1E', '1 ESO'),
                ('2E', '2 ESO'),
                ('3E', '3 ESO'),
                ('4E', '4 ESO'),
                ('1B', '1 Bachillerato'),
                ('2B', '2 Bachillerato'),
                ('OT', 'Otro')]

class Alumnos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    curso = models.CharField(max_length=2, choices=opcionescurso, default='OT')
    padre = models.ForeignKey(padresmodels.Padres, default=1, on_delete=CASCADE)
    profesor = models.ForeignKey(profesoresmodels.Profesores, default=1, on_delete=CASCADE)
    telefono = models.CharField(max_length=100, default='')
    mail = models.CharField(max_length=100, default='')
    fechaInscripcion = models.DateField(default=now())

    def __str__(self):
        return f"{ self.nombre } { self.apellidos }"