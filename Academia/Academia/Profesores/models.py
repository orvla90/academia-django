from django.db import models
from django.shortcuts import resolve_url

# Create your models here.
class Profesores(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    telefono = models.IntegerField()
    mail = models.CharField(max_length=100)

    def __str__(self):
        return f"{ self.nombre } { self.apellidos }"
    