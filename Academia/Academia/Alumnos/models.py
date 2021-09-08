from django.db import models
from django.db.models.deletion import CASCADE
import datetime
from Padres import models as padresmodels

# Create your models here.
class Alumnos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    padre = models.ForeignKey(padresmodels.Padres, default=1, on_delete=CASCADE)
