# Generated by Django 4.2 on 2023-06-13 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppE3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaestroTKD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCompleto', models.CharField(max_length=25)),
                ('GradoCinturon', models.IntegerField()),
                ('Emailmaestro', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TutorAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombretutor', models.CharField(max_length=30)),
                ('Emailtutor', models.EmailField(max_length=254)),
                ('Fonotutor', models.BigIntegerField(verbose_name=9)),
            ],
        ),
    ]
