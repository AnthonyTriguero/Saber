# Generated by Django 2.0.6 on 2020-01-23 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0006_nota'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='resultado',
        ),
    ]
