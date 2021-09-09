from django.db import models
import datetime

from django.db.models.deletion import CASCADE
from Padres import models as padresmodels
# Create your models here.

class Pagos(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField(default=datetime.datetime.now())
    cantidad = models.FloatField(default=0.0)
    padre = models.ForeignKey(padresmodels.Padres, on_delete=CASCADE)

    def __str__(self):
        return f"{ self.padre } - { self.cantidad }"