from django.db import models

# Create your models here.
class Alumno(models.Model):
    NombreCompleto = models.CharField(max_length=25)
    GradoCinturon = models.IntegerField()

class MaestroTKD(models.Model):
    NombreCompleto = models.CharField(max_length=25)
    GradoCinturon = models.IntegerField()
    Emailmaestro = models.EmailField()

class TutorAlumno(models.Model):
    Nombretutor = models.CharField(max_length=30)
    Emailtutor = models.EmailField()
    Fonotutor =models.BigIntegerField(9)
