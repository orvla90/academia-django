from datetime import timezone
from django.db import models
from django.utils import timezone

from django.db.models.deletion import CASCADE
from Padres import models as padresmodels
# Create your models here.

class Pagos(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField(default=timezone.now())
    cantidad = models.FloatField(default=0.0)
    padre = models.ForeignKey(padresmodels.Padres, on_delete=CASCADE)
    numeroFactura = models.IntegerField(default=0)

    
    def __str__(self):
        return f"{ self.padre } - { self.cantidad }"

    def setNumeroFactura(self, nuevoNumero):
        self.numeroFactura = nuevoNumero

    def ponerNumeroFactura(self):
        totalFacturas = Pagos.objects.all()
        facturasAnuales = 0
        for factura in totalFacturas:
            print(self.fecha)
            if(factura.fecha.year == self.fecha.year):
                facturasAnuales += 1
        if(facturasAnuales > 0):
            self.setNumeroFactura(facturasAnuales + 1)
        else:
            self.setNumeroFactura(1)

    