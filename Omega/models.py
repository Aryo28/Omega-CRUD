from random import choices
from django.db import models
from django import forms
from django.urls import reverse
from django.forms import model_to_dict
# Create your models here.

# ********** TABLAS REFERENCIALES ****************************************
class Jurisdiccion(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Sectores(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.clave)

class Origen_reporte(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Colonias(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre

    def natural_key(self):
        return (self.nombre)

class Grupos_operativos(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")

    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Corporaciones(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Tipo_accidente(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Daños_accidente(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Causa_accidente(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Servicio_vehiculo(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Tipo_servicio_vehiculo(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Clasificacion_vehiculo(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)

class Marca_vehiculo(models.Model):
    clave = models.CharField(max_length=50 , blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    estatus = models.CharField(max_length=50, default="ACTIVO")
    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre)
#***************************************************************


#******************BITACORA********************************
class Bitacora(models.Model):
    
    MOTIVOS = [
        ('INFRACCION', 'INFRACCION'),
        ('ALIMENTOS', 'ALIMENTOS'),
        ('CARRUSEL', 'CARRUSEL'),
        ('OTRO', 'OTRO')
    ]
    
    fecha_registro      = models.DateTimeField(auto_now_add=True, null=True)
    fecha               = models.DateField(null=True)
    hora                = models.TimeField(null=True)
    unidad              = models.CharField(max_length=50, null= True)
    grupo               = models.ForeignKey(Grupos_operativos, on_delete=models.CASCADE)
    domicilio           = models.CharField(max_length=100)
    motivo              = models.CharField(max_length=50, choices = MOTIVOS)
    observaciones       = models.TextField(max_length=200)
    estatus             = models.CharField(max_length=50, default="ACTIVO")

#***********************EVENTOS Y APOYOS****************************************
    
class Eventos(models.Model):

    TIPO_EVENTO = [
        ('CARRERA', 'CARRERA'),
        ('CARAVANA', 'CARAVANA'),
        ('DEPORTIVO', 'DEPORTIVO'),
        ('DESFILE', 'DESFILE'),
        ('INCENDIO', 'INCENDIO'),
        ('MANIOBRAS (GRUAS, CONSTRUCCION)', 'MANIOBRAS (GRÚAS, CONSTRUCCIÓN)'),
        ('MARATON', 'MARATÓN'),
        ('MUSICAL', 'MUSICAL'),
        ('MANIFESTACION', 'MANIFESTACIÓN'),
        ('LABOR SOCIAL', 'LABOR SOCIAL'),
        ('OBRAS DEL MUNICIPIO', 'OBRAS DEL MUNICIPIO'),
        ('PASEO CICLISTA', 'PASEO CICLISTA'),
        ('POLICIACO', 'POLICIACO'),
        ('PUNTOS FIJOS ESCUELAS', 'PUNTOS FIJOS ESCUELAS'),
        ('PUNTOS FIJOS','PUNTOS FIJOS'),
        ('RELIGIOSO', 'RELIGIOSO'),
        ('SEMAFORO DESCOMPUESTO', 'SEMÁFORO DESCOMPUESTO'),
        ('SIMULACRO', 'SIMULACRO'),
        ('SOCIAL', 'SOCIAL'),
        ('OPERATIVO', 'OPERATIVO')
    ]

    DEPENDENCIAS =[
        ('ALUMBRADO PÚBLICO', 'ALUMBRADO PÚBLICO'),
        ('ATENCIÓN CIUDADANA', 'ATENCIÓN CIUDADANA'),
        ('AUTOTRANSPORTE', 'AUTOTRANSPORTE'),
        ('BOMBEROS', 'BOMBEROS'),
        ('C4', 'C4'),
        ('CFE', 'CFE'),
        ('CIUDADANO', 'CIUDADANO'),
        ('COLISEO CENTENARIO', 'COLISEO CENTENARIO'),
        ('DESARROLLO SOCIAL', 'DESARROLLO SOCIAL'),
        ('DIF', 'DIF'),
        ('DIRECCION DE CULTURA', 'DIRECCIÓN DE CULTURA'),
        ('DIRECCION DEL DEPORTE', 'DIRECCIÓN DEL DEPORTE'),
        ('GOBIERNO DEL ESTADO', 'GOBIERNO DEL ESTADO'),
        ('INSPECCION MUNICIPAL', 'INSPECCIÓN MUNICIPAL'),
        ('MEDIO AMBIENTE', 'MEDIO AMBIENTE'),
        ('OBRAS PUBLICAS DEL ESTADO', 'OBRAS PÚBLICAS DEL ESTADO'),
        ('OBRAS PUBLICAS DEL MUNICIPIO', 'OBRAS PÚBLICAS DEL MUNICIPIO'),
        ('PARQUES Y JARDINES', 'PARQUES Y JARDINES'),
        ('PLAZA MAYOR', 'PLAZA MAYOR'),
        ('POLICIA FEDERAL', 'POLICIA FEDERAL'),
        ('PRESIDENCIA', 'PRESIDENCIA'),
        ('PRIVADA', 'PRIVADA'),
        ('PROTECCION CIVIL', 'PROTECCIÓN CIVIL'),
        ('SEDENA', 'SEDENA'),
        ('SEGURIDAD PUBLICA', 'SEGURIDAD PÚBLICA'),
        ('SERVICIOS PUBLICOS', 'SERVICIOS PÚBLICOS'),
        ('SIMAS', 'SIMAS'),
        ('SISTEMA DE MANTENIMIENTO VIAL', 'SISTEMA DE MANTENIMIENTO VIAL'),
        ('TRIBUNALES', 'TRIBUNALES'),
        ('TSM', 'TSM'),
        ('VIALIDAD', 'VIALIDAD'),
        ('PARTICULAR', 'PARTICULAR'),
    ]


    ACCION = [
        ('APOYO OPERATIVO', 'APOYO OPERATIVO'),
        ('BACHEO', 'BACHEO'),
        ('BLOQUEO', 'BLOQUEO'),
        ('MANTENIMIENTO SEMAFOROS', 'MANTENIMIENTO SEMÁFOROS'),
        ('COLOCACION POSTES', 'COLOCACIÓN POSTES'),
        ('COLOCACION SEÑALAMIENTOS', 'COLOCACIÓN SEÑALAMIENTOS'),
        ('CONCIERTO', 'CONCIERTO'),
        ('CONSTRUCCION DE PUENTES', 'CONSTRUCCIÓN DE PUENTES'),
        ('CUSTODIA', 'CUSTODIA'),
        ('DESAGUE', 'DESAGUE'),
        ('DESFILE ', 'DESFILE '),
        ('DRENAJE', 'DRENAJE'),
        ('ENTREGA DE APOYOS', 'ENTREGA DE APOYOS'),
        ('EVENTO MASIVO', 'EVENTO MASIVO'),
        ('FUGA DE AGUA', 'FUGA DE AGUA'),
        ('FUGA DE GAS', 'FUGA DE GAS'),
        ('INAUGURACION OBRAS', 'INAUGURACIÓN OBRAS'),
        ('INCENDIO', 'INCENDIO'),
        ('INFORMACION','INFORMACIÓN'),
        ('INSTALACION DE SEMAFOROS', 'INSTALACIÓN DE SEMÁFOROS'),
        ('INUNDACION', 'INUNDACIÓN'),
        ('LAVADO DE PUENTES', 'LAVADO DE PUENTES'),
        ('LIMPIEZA', 'LIMPIEZA'),
        ('MANTENIMIENTO DE CAMARAS', 'MANTENIMIENTO DE CÁMARAS'),
        ('MANTENIMIENTO DE LUMINARIAS', 'MANTENIMIENTO DE LUMINARIAS'),
        ('OPERATIVO ALCOHOLIMETRO', 'OPERATIVO ALCOHOLÍMETRO'),
        ('ORDENAMIENTO VIAL', 'ORDENAMIENTO VIAL'),
        ('EVENTO DEPORTIVO', 'EVENTO DEPORTIVO'),
        ('PASEO COLON', 'PASEO COLON'),
        ('PASEO MORELOS', 'PASEO MORELOS'),
        ('PINTURA', 'PINTURA'),
        ('PODA ARBOLES', 'PODA ARBOLES'),
        ('PREVENCION', 'PREVENCIÓN'),
        ('RECARPETEO', 'RECARPETEO'),
        ('RECORRIDO COLONIA', 'RECORRIDO COLONIA'),
        ('RECREATIVO', 'RECREATIVO'),
        ('REEMPLAZO DE SEÑALAMIENTOS', 'REEMPLAZO DE SEÑALAMIENTOS'),
        ('TRASLADO URGENCIA', 'TRASLADO URGENCIA'),
        ('VEHICULO DESCOMPUESTO', 'VEHICULO DESCOMPUESTO'),
        ('VIGILANCIA VIAL', 'VIGILANCIA VIAL'),
        ('PERSONA ENFERMA', 'PERSONA ENFERMA'),
        ('SEMÁFORO DESCOMPUESTO', 'SEMÁFORO DESCOMPUESTO'),
    ]


    fecha_registro      = models.DateTimeField(auto_now_add=True, null=True)
    fecha               = models.DateField(null=True)
    hora                = models.TimeField(null=True)
    domicilio           = models.CharField(max_length=100)
    sector              = models.ForeignKey(Sectores, on_delete=models.CASCADE)
    origen              = models.ForeignKey(Origen_reporte, on_delete=models.CASCADE)
    grupo               = models.ForeignKey(Grupos_operativos, on_delete=models.CASCADE)
    unidad              = models.CharField(max_length=50, null= True)
    agentes             = models.CharField(max_length=100, null= True)
    tipo_evento         = models.CharField(max_length=100, choices = TIPO_EVENTO)
    dependencia         = models.CharField(max_length=100, choices = DEPENDENCIAS)
    accion              = models.CharField(max_length=100, choices = ACCION)
    observaciones       = models.TextField(max_length=200)
    estatus             = models.CharField(max_length=50, default="ACTIVO")



#************************MAL ESTACIONADOS*******************************
class MalEstacionados(models.Model):

    EVENTO = [
        ('VEHICULO ABDANDONADO', 'VEHICULO ABDANDONADO'),
        ('ACTIVACION DE CODIGO ROJO', 'ACTIVACION DE CODIGO ROJO'),
        ('VEHICULO EXCESO DE DIMENSIONES', 'VEHICULO EXCESO DE DIMENSIONES'),
        ('VEHICULO DESCOMPUESTO', 'VEHICULO DESCOMPUESTO'),
        ('VEHICULO COCHERA', 'VEHICULO COCHERA'),
        ('VEHICULO EN BANQUETA','VEHICULO EN BANQUETA'),
        ('VEHICULO EN EXCLUSIVO','VEHICULO EN EXCLUSIVO'),
        ('VEHICULO EN SENTIDO CONTRARIO','VEHICULO EN SENTIDO CONTRARIO'),
        ('VEHICULO INVADE LINEA PEATONAL','VEHICULO INVADE LINEA PEATONAL'),
        ('VEHICULO EN LUGAR DISCAPACITADOS','VEHICULO EN LUGAR DISCAPACITADOS'),
        ('VEHICULO MAL ESTACIONADO','VEHICULO MAL ESTACIONADO'),
        ('VEHICULO EXCESO DE VELOCIDAD','VEHICULO EXCESO DE VELOCIDAD'),
    ]


    MOTIVO_NO_ATENCION = [
        ('FALSA ALARMA', 'FALSA ALARMA'),
        ('PUNTO ROJO', 'PUNTO ROJO'),
        ('FUERA DE JURISDICCION', 'FUERA DE JURISDICCION'),
        ('SERVICIO CANCELADO', 'SERVICIO CANCELADO'),
        ('NO PROPORCIONA DATOS','NO PROPORCIONA DATOS'),
        ('PERSONAL INSUFICIENTE','PERSONAL INSUFICIENTE'),        
    ]

    ESTATUS = [
        ('ATENDIDO', 'ATENDIDO'),
        ('NO ATENDIDO', 'NO ATENDIDO'),
    ]


    fecha_registro      = models.DateTimeField(auto_now_add=True, null=True)
    fecha               = models.DateField(null=True)
    hora                = models.TimeField(null=True)
    domicilio           = models.CharField(max_length=100)
    colonia             = models.ForeignKey(Colonias, on_delete=models.CASCADE)
    sector              = models.ForeignKey(Sectores, on_delete=models.CASCADE)
    grupo               = models.ForeignKey(Grupos_operativos, on_delete=models.CASCADE)
    unidad              = models.CharField(max_length=50, null= True)
    elemento            = models.CharField(max_length=100, null= True, blank=True)
    evento              = models.CharField(max_length=100, choices = EVENTO)
    estatus_servicio    = models.CharField(max_length=50, choices = ESTATUS)
    folio_infraccion    = models.CharField(max_length=50, null= True, blank=True)
    numerales           = models.CharField(max_length=100, null= True, blank=True)
    origen              = models.ForeignKey(Origen_reporte, on_delete=models.CASCADE)
    motivo_no_atencion  = models.CharField(max_length=100, choices = MOTIVO_NO_ATENCION, blank=True, null= True)
    observaciones       = models.TextField(max_length=200)
    estatus             = models.CharField(max_length=50, default="ACTIVO")


#******************APOYOS A PREVENTIVA**************************************
class ApoyosPreventiva(models.Model):

    EVENTO = [
        ('INCIDENTE POR INFRACCION', 'INCIDENTE POR INFRACCION'),
        ('APOYO A PREVENTIVA', 'APOYO A PREVENTIVA'),

    ]


    fecha_registro      = models.DateTimeField(auto_now_add=True, null=True)
    fecha               = models.DateField(null=True)
    hora                = models.TimeField(null=True)
    domicilio           = models.CharField(max_length=100)
    id_colonia          = models.ForeignKey(Colonias, on_delete=models.CASCADE)
    id_sector           = models.ForeignKey(Sectores, on_delete=models.CASCADE)
    id_grupo            = models.ForeignKey(Grupos_operativos, on_delete=models.CASCADE)
    unidad              = models.CharField(max_length=50, null= True)
    elemento            = models.CharField(max_length=100, null= True, blank=True)
    evento              = models.CharField(max_length=100, choices = EVENTO)
    folio_infraccion    = models.CharField(max_length=50,  null= True, blank=True)
    unidad_preventiva   = models.CharField(max_length=50, null= True)
    observaciones       = models.TextField(max_length=200)
    estatus             = models.CharField(max_length=50, default="ACTIVO")


#***************************************************************************************


#***************************ACCIDENTES VIALES******************************************


#Datos del Accidente

class AccidenteVial(models.Model):

    ESTATUS = [
        ('ATENDIDO', 'ATENDIDO'),
        ('NO ATENDIDO', 'NO ATENDIDO'),
    ]
    fecha_registro      = models.DateTimeField(auto_now_add=True, null=True)
    fecha               = models.DateField(null=True)
    hora                = models.TimeField(null=True)
    folio_911           = models.IntegerField(null=True, blank=True)
    domicilio           = models.CharField(max_length=100)
    colonia             = models.ForeignKey(Colonias, on_delete=models.CASCADE)
    sector              = models.ForeignKey(Sectores, on_delete=models.CASCADE)
    grupo               = models.ForeignKey(Grupos_operativos, on_delete=models.CASCADE)
    unidad              = models.CharField(max_length=50, null= True)
    elemento            = models.CharField(max_length=100, null= True, blank=True)  
    estatus_accidente   = models.CharField(max_length=50, choices = ESTATUS)
    jurisdiccion        = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE)
    origen              = models.ForeignKey(Origen_reporte, on_delete=models.CASCADE)
    observaciones       = models.TextField(max_length=200)
    estatus             = models.CharField(max_length=50, default="ACTIVO")

#Accidente Atendido

class AccidenteVialAtendido(models.Model):

    fecha_registro      = models.DateTimeField(auto_now_add=True, null=True)
    id_accidente        = models.ForeignKey(AccidenteVial, on_delete=models.CASCADE, null=True, blank=True)
    peritos             = models.CharField(max_length=50, blank=True, null=True)
    policia_estatal     = models.CharField(max_length=50, blank=True, null= True)
    policia_federal     = models.CharField(max_length=50, blank= True, null= True)
    policia_preventiva  = models.CharField(max_length=50, blank= True, null= True)
    gurdia_nacional     = models.CharField(max_length=50, blank= True, null= True)
    proteccion_civil    = models.CharField(max_length=50, blank= True, null= True)
    bomberos            = models.CharField(max_length=50, blank= True, null=True)
    grua                = models.CharField(max_length=50, blank= True, null= True)
    cruz_roja           = models.CharField(max_length=50, blank= True, null= True)
    tipo_accidente      = models.ForeignKey(Tipo_accidente, on_delete=models.CASCADE)
    tipo_daños          = models.ForeignKey(Daños_accidente, on_delete=models.CASCADE)
    causa_accidente     = models.ForeignKey(Causa_accidente, on_delete =models.CASCADE)
    lesionados_fem      = models.IntegerField(null=True, blank= True)
    lesionados_masc     = models.IntegerField(null=True, blank= True)
    fallecidos_fem      = models.IntegerField(null=True, blank= True)
    fallecidos_masc     = models.IntegerField(null =True, blank= True)
    estatus             = models.CharField(max_length=50, default="ACTIVO")

#Accidente NO atendido

class AccidenteVialNoAtendido(models.Model):
    MOTIVO =[
        ('FALSA ALARMA', 'FALSA ALARMA'),
        ('FUERA DE JURISDICCION', 'FUERA DE JURISDICCION'),
        ('INVOLUCRADOS SE RETIRARON', 'INVOLUCRADOS SE RETIRARON'),
        ('UNIDAD SE RETIRA DEL LUGAR', 'UNIDAD SE RETIRA DEL LUGAR'),
        ('NO SE PROPORCIONAN DATOS', 'NO SE PROPORCIONAN DATOS'),
        ('PERSONAL INSUFICIENTE', 'PERSONAL INSUFICIENTE'),
        ('PUNTO ROJO', 'PUNTO ROJO'),
    ]

    id_accidente        = models.ForeignKey(AccidenteVial, on_delete=models.CASCADE, null= True, blank=True)
    motivo_no_atencion  = models.CharField(max_length=50, choices = MOTIVO)
    estatus             = models.CharField(max_length=50, default="ACTIVO")



#Participantes de ACCIDENTES

class AccidenteConductores(models.Model):


    SEXO_CONDUCTOR = [
        ('MASCULINO', 'MASCULINO'),
        ('FEMENINO', 'FEMENINO')
    ]

    LICENCIA = [
        ('VIGENTE', 'VIGENTE'),
        ('VENCIDA', 'VENCIDA'),
        ('SIN LICENCIA', 'SIN LICENCIA')
    ]

    fecha_registro                = models.DateTimeField(auto_now_add=True, null=True)
    id_accidente                  = models.ForeignKey(AccidenteVial, on_delete=models.CASCADE, null= True, blank=True)
    nombre_conductor              = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno_conductor    = models.CharField(max_length=50, blank=True, null=True)
    apellido_materno_conductor    = models.CharField(max_length=50, blank=True, null=True)
    domicilio_conductor           = models.CharField(max_length=200, blank=True, null=True)
    sexo_conductor                = models.CharField(max_length=200, blank=True, null=True, choices = SEXO_CONDUCTOR)  
    edad_conductor                = models.IntegerField(blank=True, null=True)
    licencia_conductor            = models.CharField(max_length=50, blank=True, null= True, choices = LICENCIA)
    servicio_vehiculo             = models.ForeignKey(Servicio_vehiculo, on_delete=models.CASCADE, null= True, blank=True)
    tipo_servicio_vehiculo        = models.ForeignKey(Tipo_servicio_vehiculo, on_delete=models.CASCADE, null= True, blank=True)
    clasificacion_vehiculo        = models.ForeignKey(Clasificacion_vehiculo, on_delete=models.CASCADE, null= True, blank=True)
    marca_vehiculo                = models.ForeignKey(Marca_vehiculo, on_delete=models.CASCADE, null= True, blank=True)
    tipo_vehiculo                 = models.CharField(max_length=50, null= True, blank=True)
    modelo_vehiculo               = models.IntegerField(null= True, blank=True)
    placas_vehiculo               = models.CharField(max_length=50, null= True, blank=True)
    color_vehiculo                = models.CharField(max_length=50, null= True, blank=True)
    estatus                       = models.CharField(max_length=50, default="ACTIVO")

#*************************************************************************************

#Vehiculos al Corralon

class VehiculosCorralon(models.Model):
    fecha_registro              = models.DateTimeField(auto_now_add=True, null=True)
    fecha                       = models.DateField(null=True)
    hora                        = models.TimeField(null=True)
    ubicacion_vehiculo          = models.CharField(max_length=100) 
    marca_vehiculo              = models.ForeignKey(Marca_vehiculo, on_delete=models.CASCADE, null= True, blank=True)
    tipo_vehiculo               = models.CharField(max_length=50, null= True, blank=True)
    modelo_vehiculo             = models.IntegerField(null= True, blank=True)
    placas_vehiculo             = models.CharField(max_length=50, null= True, blank=True)
    color_vehiculo              = models.CharField(max_length=50, null= True)
    serie_vehiculo              = models.CharField(max_length=50, null= True, blank=True)
    folio_infraccion            = models.CharField(max_length=50, null= True)
    numerales                   = models.CharField(max_length=100, null= True)
    inventario                  = models.CharField(max_length=100, null= True)
    grua                        = models.CharField(max_length=100, null= True)
    unidad                      = models.CharField(max_length=50, null= True)
    elemento                    = models.CharField(max_length=100, null= True, blank=True) 
    folio_911                   = models.IntegerField(null=True)
    observaciones               = models.TextField(max_length=200)
    estatus                     = models.CharField(max_length=50, default="ACTIVO") 
#*************************************************************************************

#Detenidos

class Detenidos(models.Model):
    fecha_registro              = models.DateTimeField(auto_now_add=True, null=True)
    fecha                       = models.DateField(null=True)
    hora                        = models.TimeField(null=True)
    nombre_detenido             = models.CharField(max_length=50, null=True)
    domicilio_detenido          = models.CharField(max_length=200, blank=True, null=True)
    edad_detenido               = models.IntegerField(null=True)
    folio_911                   = models.IntegerField(null=True)
    folio_remision              = models.IntegerField(null=True, blank= True)
    ubicacion_vehiculo          = models.CharField(max_length=100)
    marca_vehiculo              = models.ForeignKey(Marca_vehiculo, on_delete=models.CASCADE, null= True, blank=True)
    tipo_vehiculo               = models.CharField(max_length=50, null= True, blank=True)
    placas_vehiculo             = models.CharField(max_length=50, null= True, blank=True)
    color_vehiculo              = models.CharField(max_length=50, null= True , blank= True)
    serie_vehiculo              = models.CharField(max_length=50, null= True, blank=True)
    folio_infraccion            = models.CharField(max_length=50, null= True, blank= True)
    numerales                   = models.CharField(max_length=100, null= True, blank=True)
    inventario                  = models.CharField(max_length=100, null= True, blank = True)
    grua                        = models.CharField(max_length=100, null= True , blank= True)
    unidad                      = models.CharField(max_length=50, null= True)
    elemento                    = models.CharField(max_length=100, null= True, blank=True) 
    observaciones               = models.TextField(max_length=200)
    estatus                     = models.CharField(max_length=50, default="ACTIVO") 
    