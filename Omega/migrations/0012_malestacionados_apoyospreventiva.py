# Generated by Django 4.0.1 on 2022-02-17 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Omega', '0011_remove_eventos_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MalEstacionados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
                ('domicilio', models.CharField(max_length=100)),
                ('unidad', models.CharField(max_length=50, null=True)),
                ('elemento', models.CharField(max_length=100, null=True)),
                ('observaciones', models.TextField(max_length=200)),
                ('estatus', models.CharField(default='ACTIVO', max_length=50)),
                ('id_colonia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Omega.colonias')),
                ('id_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Omega.grupos_operativos')),
                ('id_sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Omega.sectores')),
            ],
        ),
        migrations.CreateModel(
            name='ApoyosPreventiva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
                ('domicilio', models.CharField(max_length=100)),
                ('unidad', models.CharField(max_length=50, null=True)),
                ('elemento', models.CharField(max_length=100, null=True)),
                ('observaciones', models.TextField(max_length=200)),
                ('estatus', models.CharField(default='ACTIVO', max_length=50)),
                ('id_colonia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Omega.colonias')),
                ('id_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Omega.grupos_operativos')),
                ('id_sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Omega.sectores')),
            ],
        ),
    ]
