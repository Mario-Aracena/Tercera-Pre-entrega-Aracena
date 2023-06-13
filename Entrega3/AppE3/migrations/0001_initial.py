# Generated by Django 4.2.1 on 2023-06-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('Grado', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MaestroTKD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('Grado', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TutorAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Fono', models.IntegerField(default=10)),
            ],
        ),
    ]