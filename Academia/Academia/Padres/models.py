from django.db import models

# Create your models here.
class Padres(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=12)
    mail = models.CharField(max_length=100)

