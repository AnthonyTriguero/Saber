# Generated by Django 2.0.6 on 2020-01-23 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0007_remove_nota_resultado'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='estudiante_id',
            field=models.ManyToManyField(to='notas.Alumno'),
        ),
    ]