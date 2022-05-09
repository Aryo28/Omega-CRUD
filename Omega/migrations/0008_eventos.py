# Generated by Django 4.0.1 on 2022-02-09 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Omega', '0007_remove_bitacora_fecha_hora_bitacora_fecha_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
                ('domicilio', models.CharField(max_length=100)),
                ('unidad', models.CharField(max_length=50, null=True)),
                ('agentes', models.CharField(max_length=100, null=True)),
                ('tipo_evento', models.CharField(choices=[('CARRERA', 'CARRERA'), ('CARAVANA', 'CARAVANA'), ('DEPORTIVO', 'DEPORTIVO'), ('DESFILE', 'DESFILE'), ('INCENDIO', 'INCENDIO'), ('MANIOBRAS (GRUAS, CONSTRUCCION)', 'MANIOBRAS (GRÚAS, CONSTRUCCIÓN)'), ('MARATON', 'MARATÓN'), ('MUSICAL', 'MUSICAL'), ('MANIFESTACION', 'MANIFESTACIÓN'), ('LABOR SOCIAL', 'LABOR SOCIAL'), ('OBRAS DEL MUNICIPIO', 'OBRAS DEL MUNICIPIO'), ('PASEO CICLISTA', 'PASEO CICLISTA'), ('POLICIACO', 'POLICIACO'), ('PUNTOS FIJOS ESCUELAS', 'PUNTOS FIJOS ESCUELAS'), ('PUNTOS FIJOS', 'PUNTOS FIJOS'), ('RELIGIOSO', 'RELIGIOSO'), ('SEMAFORO DESCOMPUESTO', 'SEMÁFORO DESCOMPUESTO'), ('SIMULACRO', 'SIMULACRO'), ('SOCIAL', 'SOCIAL'), ('OPERATIVO', 'OPERATIVO')], max_length=100)),
                ('dependencia', models.CharField(choices=[('ALUMBRADO PÚBLICO', 'ALUMBRADO PÚBLICO'), ('ATENCIÓN CIUDADANA', 'ATENCIÓN CIUDADANA'), ('AUTOTRANSPORTE', 'AUTOTRANSPORTE'), ('BOMBEROS', 'BOMBEROS'), ('C4', 'C4'), ('CFE', 'CFE'), ('CIUDADANO', 'CIUDADANO'), ('COLISEO CENTENARIO', 'COLISEO CENTENARIO'), ('DESARROLLO SOCIAL', 'DESARROLLO SOCIAL'), ('DIF', 'DIF'), ('DIRECCION DE CULTURA', 'DIRECCIÓN DE CULTURA'), ('DIRECCION DEL DEPORTE', 'DIRECCIÓN DEL DEPORTE'), ('GOBIERNO DEL ESTADO', 'GOBIERNO DEL ESTADO'), ('INSPECCION MUNICIPAL', 'INSPECCIÓN MUNICIPAL'), ('MEDIO AMBIENTE', 'MEDIO AMBIENTE'), ('OBRAS PUBLICAS DEL ESTADO', 'OBRAS PÚBLICAS DEL ESTADO'), ('OBRAS PUBLICAS DEL MUNICIPIO', 'OBRAS PÚBLICAS DEL MUNICIPIO'), ('PARQUES Y JARDINES', 'PARQUES Y JARDINES'), ('PLAZA MAYOR', 'PLAZA MAYOR'), ('POLICIA FEDERAL', 'POLICIA FEDERAL'), ('PRESIDENCIA', 'PRESIDENCIA'), ('PRIVADA', 'PRIVADA'), ('PROTECCION CIVIL', 'PROTECCIÓN CIVIL'), ('SEDENA', 'SEDENA'), ('SEGURIDAD PUBLICA', 'SEGURIDAD PÚBLICA'), ('SERVICIOS PUBLICOS', 'SERVICIOS PÚBLICOS'), ('SIMAS', 'SIMAS'), ('SISTEMA DE MANTENIMIENTO VIAL', 'SISTEMA DE MANTENIMIENTO VIAL'), ('TRIBUNALES', 'TRIBUNALES'), ('TSM', 'TSM'), ('VIALIDAD', 'VIALIDAD'), ('PARTICULAR', 'PARTICULAR')], max_length=100)),
                ('accion', models.CharField(choices=[('APOYO OPERATIVO', 'APOYO OPERATIVO'), ('BACHEO', 'BACHEO'), ('BLOQUEO', 'BLOQUEO'), ('MANTENIMIENTO SEMAFOROS', 'MANTENIMIENTO SEMÁFOROS'), ('COLOCACION POSTES', 'COLOCACIÓN POSTES'), ('COLOCACION SEÑALAMIENTOS', 'COLOCACIÓN SEÑALAMIENTOS'), ('CONCIERTO', 'CONCIERTO'), ('CONSTRUCCION DE PUENTES', 'CONSTRUCCIÓN DE PUENTES'), ('CUSTODIA', 'CUSTODIA'), ('DESAGUE', 'DESAGUE'), ('DESFILE ', 'DESFILE '), ('DRENAJE', 'DRENAJE'), ('ENTREGA DE APOYOS', 'ENTREGA DE APOYOS'), ('EVENTO MASIVO', 'EVENTO MASIVO'), ('FUGA DE AGUA', 'FUGA DE AGUA'), ('FUGA DE GAS', 'FUGA DE GAS'), ('INAUGURACION OBRAS', 'INAUGURACIÓN OBRAS'), ('INCENDIO', 'INCENDIO'), ('INFORMACION', 'INFORMACIÓN'), ('INSTALACION DE SEMAFOROS', 'INSTALACIÓN DE SEMÁFOROS'), ('INUNDACION', 'INUNDACIÓN'), ('LAVADO DE PUENTES', 'LAVADO DE PUENTES'), ('LIMPIEZA', 'LIMPIEZA'), ('MANTENIMIENTO DE CAMARAS', 'MANTENIMIENTO DE CÁMARAS'), ('MANTENIMIENTO DE LUMINARIAS', 'MANTENIMIENTO DE LUMINARIAS'), ('OPERATIVO ALCOHOLIMETRO', 'OPERATIVO ALCOHOLÍMETRO'), ('ORDENAMIENTO VIAL', 'ORDENAMIENTO VIAL'), ('EVENTO DEPORTIVO', 'EVENTO DEPORTIVO'), ('PASEO COLON', 'PASEO COLON'), ('PASEO MORELOS', 'PASEO MORELOS'), ('PINTURA', 'PINTURA'), ('PODA ARBOLES', 'PODA ARBOLES'), ('PREVENCION', 'PREVENCIÓN'), ('RECARPETEO', 'RECARPETEO'), ('RECORRIDO COLONIA', 'RECORRIDO COLONIA'), ('RECREATIVO', 'RECREATIVO'), ('REEMPLAZO DE SEÑALAMIENTOS', 'REEMPLAZO DE SEÑALAMIENTOS'), ('TRASLADO URGENCIA', 'TRASLADO URGENCIA'), ('VEHICULO DESCOMPUESTO', 'VEHICULO DESCOMPUESTO'), ('VIGILANCIA VIAL', 'VIGILANCIA VIAL'), ('PERSONA ENFERMA', 'PERSONA ENFERMA'), ('SEMÁFORO DESCOMPUESTO', 'SEMÁFORO DESCOMPUESTO')], max_length=100)),
                ('observaciones', models.TextField(max_length=200)),
                ('estatus', models.CharField(default='ACTIVO', max_length=50)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Omega.grupos_operativos')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Omega.origen_reporte')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Omega.sectores')),
            ],
        ),
    ]