from django.db import models

# Create your models here.
class ListadoAlumnos(models.Model):
    first_name = models.CharField(max_length=30)