# Generated by Django 3.0.3 on 2020-02-10 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0011_delete_materias'),
    ]

    operations = [
        migrations.CreateModel(
            name='profesor',
            fields=[
                ('id_profesor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_de_profesor', models.CharField(max_length=200)),
                ('apellido_de_profesor', models.CharField(max_length=200)),
                ('curso', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id_materia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_de_materia', models.CharField(max_length=200)),
                ('curso', models.CharField(max_length=200)),
                ('profesor', models.CharField(max_length=200)),
                ('estudiante_id', models.ManyToManyField(to='notas.Alumno')),
            ],
        ),
    ]
