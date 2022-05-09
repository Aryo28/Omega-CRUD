# Generated by Django 4.0.1 on 2022-02-17 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Omega', '0016_alter_malestacionados_estatus_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malestacionados',
            name='elemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='malestacionados',
            name='folio_infraccion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='malestacionados',
            name='motivo_no_atencion',
            field=models.CharField(blank=True, choices=[('FALSA ALARMA', 'FALSA ALARMA'), ('PUNTO ROJO', 'PUNTO ROJO'), ('FUERA DE JURISDICCION', 'FUERA DE JURISDICCION'), ('SERVICIO CANCELADO', 'SERVICIO CANCELADO'), ('NO PROPORCIONA DATOS', 'NO PROPORCIONA DATOS'), ('PERSONAL INSUFICIENTE', 'PERSONAL INSUFICIENTE')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='malestacionados',
            name='numerales',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
