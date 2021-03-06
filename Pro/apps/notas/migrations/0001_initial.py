# Generated by Django 3.0.2 on 2020-01-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id_notas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_de_materia', models.CharField(max_length=200)),
                ('n1', models.IntegerField(blank=True, null=True)),
                ('n2', models.FloatField(blank=True, null=True)),
                ('exa', models.FloatField(blank=True, null=True)),
                ('resultado', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('fecha_de_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion ')),
                ('nota_id', models.ManyToManyField(to='notas.Nota')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
                'ordering': ['nombre'],
            },
        ),
    ]
