# Generated by Django 3.0.3 on 2020-02-10 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0013_delete_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_profesor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_de_profesor', models.CharField(max_length=200)),
                ('apellido_de_profesor', models.CharField(max_length=200)),
                ('curso', models.CharField(max_length=200)),
            ],
        ),
    ]