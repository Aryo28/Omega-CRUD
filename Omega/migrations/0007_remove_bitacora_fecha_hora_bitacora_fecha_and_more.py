# Generated by Django 4.0.1 on 2022-02-07 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Omega', '0006_alter_bitacora_fecha_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitacora',
            name='fecha_hora',
        ),
        migrations.AddField(
            model_name='bitacora',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='hora',
            field=models.TimeField(null=True),
        ),
    ]
