# Generated by Django 4.0.1 on 2022-02-17 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Omega', '0012_malestacionados_apoyospreventiva'),
    ]

    operations = [
        migrations.RenameField(
            model_name='malestacionados',
            old_name='id_colonia',
            new_name='colonia',
        ),
        migrations.RenameField(
            model_name='malestacionados',
            old_name='id_grupo',
            new_name='grupo',
        ),
        migrations.RenameField(
            model_name='malestacionados',
            old_name='id_sector',
            new_name='sector',
        ),
    ]
