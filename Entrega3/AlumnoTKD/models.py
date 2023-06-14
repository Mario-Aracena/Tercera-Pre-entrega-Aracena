from django.db import models

# Create your models here.

class Alumno(models.Model):
    Nombre = models.CharField(max_length=25)
    Apellido = models.CharField(max_length=25)
    Email = models.EmailField()


