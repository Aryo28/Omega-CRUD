# Generated by Django 4.0.1 on 2022-04-30 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Omega', '0022_vehiculoscorralon_detenidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculoscorralon',
            name='folio_911',
            field=models.IntegerField(null=True),
        ),
    ]
