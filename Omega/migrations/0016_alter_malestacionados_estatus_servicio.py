# Generated by Django 4.0.1 on 2022-02-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Omega', '0015_malestacionados_apoyospreventiva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malestacionados',
            name='estatus_servicio',
            field=models.CharField(choices=[('ATENDIDO', 'ATENDIDO'), ('NO ATENDIDO', 'NO ATENDIDO')], max_length=50),
        ),
    ]
