from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from Alumnos.models import Alumnos

# Create your models here.
class Asistencia(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    alumno = models.ForeignKey(Alumnos, on_delete=CASCADE)
    horas = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.fecha} - {self.alumno} - {self.horas}h"