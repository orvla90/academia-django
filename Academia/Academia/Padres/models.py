from django.db import models
from django.urls import reverse

#from Pagos import models as pagosmodels

# Create your models here.
class Padres(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    telefono = models.CharField(max_length=30)
    dni = models.CharField(max_length=12)
    mail = models.CharField(max_length=100)
    #pagos = models.ForeignKey(pagosmodels.Pagos, on_delete=CASCADE, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    


