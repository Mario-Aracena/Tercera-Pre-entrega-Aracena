"""
URL configuration for Entrega3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AlumnoTKD import views 

urlpatterns = [
    path('alumnos/', views.ListadoAlumnos.as_view(), name='listar_alumnos'),
    path('crear-alumno/', views.CrearAlumnos.as_view(), name='crear_alumnos'),
    path('editar-alumno/<int:pk>/', views.EditarAlumnos.as_view(), name='editar_alumnos'),
    path('eliminar-alumno/<int:pk>/', views.EliminarAlumnos.as_view(), name='eliminar_alumnos'),
    path('buscar-alumno/<int:pk>/', views.BuscarAlumnos.as_view(), name='buscar_alumnos'),
]
