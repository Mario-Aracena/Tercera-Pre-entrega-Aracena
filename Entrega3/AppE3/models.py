from django.db import models

# Create your models here.
class Alumno(models.Model):
    Nombre = models.CharField(max_length=25)
    Grado = models.CharField(max_length=15)

class MaestroTKD(models.Model):
    Nombre = models.CharField(max_length=25)
    Grado = models.CharField(max_length=15)
    Email = models.EmailField()

class TutorAlumno(models.Model):
    Nombre = models.CharField(max_length=30)
    Email = models.EmailField()
    Fono =models.IntegerField(default=10)
