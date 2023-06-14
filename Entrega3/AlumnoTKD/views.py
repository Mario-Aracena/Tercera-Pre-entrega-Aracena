from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from AlumnoTKD.models import Alumno

class ListadoAlumnos(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = 'AlumnoTKD/listar_alumnotkd.html'

class CrearAlumnos(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Alumno
    permission_required = "AlumnoTKD.add_AlumnoTKD"
    template_name = 'AlumnoTKD/crear_alumnotkd.html'
    success_url = reverse_lazy('listar_alumnos')
    fields = '__all__'

class EditarAlumnos(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Alumno
    permission_required = "AlumnoTKD.change_AlumnoTKD"
    template_name = 'AlumnoTKD/editar_alumnotkd.html'
    fields = '__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('buscar_alumnos', kwargs={'pk':self.object.pk})


class EliminarAlumnos(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Alumno
    permission_required = "AlumnoTKD.delete_AlumnoTKD"
    template_name = 'AlumnoTKD/eliminar_alumnotkd.html'
    success_url = reverse_lazy('listar_alumnos')

class BuscarAlumnos(LoginRequiredMixin, DetailView):
    model = Alumno
    template_name = 'AlumnoTKD/buscar_alumnotkd.html'