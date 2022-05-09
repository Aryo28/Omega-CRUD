from dataclasses import fields
from ipaddress import collapse_addresses
from django.forms import *
from .models import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats =['%A, %e %B, %Y']

class TimeInput(forms.TimeInput):
    input_type = 'time'
    input_formats = ['%I:%M %p']

class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        exclude = ('estatus',)
        widgets ={
            'fecha': DateInput(
                attrs={
                    'class': 'form-control datetimepicker-input ', 
                    'data-target': '#datetimepicker1',
                }
            ),
            'hora': TimeInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'HH:MM'
                }
            ),

            'unidad': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': ''
                }
            ),
            'domicilio': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'motivo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'grupo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'observaciones': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':3
                }
            )
        }
        
class EventoForm(forms.ModelForm):
    class Meta:
        model= Eventos
        exclude = ('estatus',)
        widgets={

            'fecha': DateInput(
                attrs={
                    'class': 'form-control ', 
                    'placeholder': 'DD/MM/AAAA'
                }
            ),
            'hora': TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'HH:MM'
                }
            ),
            'domicilio': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Domicilio'
                }
            ),
            'sector': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'origen': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'grupo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'unidad': TextInput(
                attrs={
                    'class': 'form-control',
                    'help_text': 'hola'
                    
                }
            ),
            'agentes': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo_evento': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
             'dependencia': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
             'accion': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
             'observaciones': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':3
                }
            )


        }
    
class MalEstacionadosForm(forms.ModelForm):
    ESTATUS = [
        ('ATENDIDO', 'ATENDIDO'),
        ('NO ATENDIDO', 'NO ATENDIDO'),
    ]

    estatus_servicio    = forms.ChoiceField(widget=forms.RadioSelect, choices=ESTATUS)

    class Meta:
        model = MalEstacionados
        exclude = ('estatus',)        


        widgets ={
            
             'fecha': DateInput(
                attrs={
                    'class': 'form-control ', 
                    'placeholder': 'DD/MM/AAAA'
                }
            ),
            'hora': TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'HH:MM'
                }
            ),
            'domicilio': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Domicilio'
                }
            ),
            'colonia': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sector': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'origen': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'grupo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'unidad': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'elemento': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'evento': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estatus_servicio':forms.RadioSelect(
                attrs={
                    'class': 'form-control'
                }
            ),
            'folio_infraccion': TextInput(
                attrs={
                    'class': 'form-control',
                    'max_length':8,
                                        
                }
            ),
            'numerales': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'id_origen': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'motivo_no_atencion': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
              'observaciones': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':3
                }
            )
            
        }

class ApoyoPreventivaForm(forms.ModelForm):

    class Meta:
        model = ApoyosPreventiva
        exclude = ('estatus',)

        widgets ={
            
             'fecha': DateInput(
                attrs={
                    'class': 'form-control ', 
                    'placeholder': 'DD/MM/AAAA'
                }
            ),
            'hora': TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'HH:MM'
                }
            ),
            'domicilio': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Domicilio'
                }
            ),
            'id_colonia': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'id_sector': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'id_grupo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'unidad': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'elemento': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'evento': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'folio_infraccion': TextInput(
                attrs={
                    'class': 'form-control',
                    'max_length':8,
                                        
                }
            ),
            'unidad_preventiva': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'observaciones': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':3
                }
            )
            
        }

class AccidentesForm(forms.ModelForm):

    ESTATUS = [
        ('ATENDIDO', 'ATENDIDO'),
        ('NO ATENDIDO', 'NO ATENDIDO'),
    ]

    estatus_accidente    = forms.ChoiceField(widget=forms.RadioSelect, choices=ESTATUS)

    class Meta:
        model = AccidenteVial
        exclude = ('estatus',)
    
        widgets ={
            
            'fecha': DateInput(
                attrs={
                    'class': 'form-control ', 
                    'placeholder': 'DD/MM/AAAA'
                }
            ),
            'hora': TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'HH:MM'
                }
            ),
             'folio_911': TextInput(
                attrs={
                    'CLASS': 'form-control'
                }
            ),
            'domicilio': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Domicilio'
                }
            ),
           
            'colonia': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'sector': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'grupo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'unidad': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'elemento': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'estatus_accidente':forms.RadioSelect(
                attrs={
                    'class': 'form-control',
                    'onblur': 'validar()',
                    
                }
            ),
            'jurisdiccion': Select(
                attrs={
                    'class': 'form-control',                 
                }
            ),
            'origen': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
              'observaciones': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':3
                }
            )
            
        }

class AccidentesAtendidoForm(forms.ModelForm):

    class Meta:
     model = AccidenteVialAtendido
     exclude = ('estatus', 'id_accidente')

     widgets ={

        'peritos': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'policia_estatal': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'policia_federal': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'policia_preventiva': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'gurdia_nacional': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'proteccion_civil': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'bomberos': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'grua': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
         'cruz_roja': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
         'tipo_accidente': Select(
            attrs={
                'class': 'form-control',
            }
        ),
         'tipo_daños': Select(
            attrs={
                'class': 'form-control',
            }
        ),
         'causa_accidente': Select(
            attrs={
                'class': 'form-control',
            }
        ),
        'lesionados_fem': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'lesionados_masc': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        'fallecidos_fem': TextInput(
            attrs={
                'class': 'form-control',
                
            }
        ),
         'fallecidos_masc': TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    }

class AccidentesNoAtendidoForm(forms.ModelForm):

    class Meta:
        model = AccidenteVialNoAtendido
        exclude = ('estatus', 'id_accidente',)
    
        widgets = {
            'motivo_no_atencion' : Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }

class ConductorAccidenteForm(forms.ModelForm):
    class Meta:
        model = AccidenteConductores
        exclude = ('estatus', 'id_accidente',)

        widgets = {

            'nombre_conductor': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
              'apellido_paterno_conductor': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido_materno_conductor': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'domicilio_conductor': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'sexo_conductor': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
             'edad_conductor': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'licencia_conductor': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'servicio_vehiculo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
             'tipo_servicio_vehiculo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
             'clasificacion_vehiculo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
             'marca_vehiculo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo_vehiculo': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'modelo_vehiculo': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'placas_vehiculo': TextInput(
                attrs={
                    'class': 'form-control',
                    'onblur': 'validateText()'
                }
            ),
              'color_vehiculo': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }

class VehiculosCorralonForm(forms.ModelForm):
    class Meta:
        model = VehiculosCorralon
        exclude = ('estatus',)

        widgets ={
             
            'fecha': DateInput(
                attrs={
                    'class': 'form-control ', 
                    'placeholder': 'DD/MM/AAAA'
                }
            ),
            'hora': TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'HH:MM'
                }
            ),
            'ubicacion_vehiculo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Domicilio'
                }
            ),
            'marca_vehiculo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo_vehiculo': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'modelo_vehiculo': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'placas_vehiculo': TextInput(
                attrs={
                    'class': 'form-control',
                    'onblur': 'validateText()'
                }
            ),
              'color_vehiculo': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'serie_vehiculo':TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'folio_infraccion': TextInput(
                attrs={
                    'class': 'form-control',
                    'max_length':8,
                                        
                }
            ),
             'numerales': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
             'inventario': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
             'grua': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ), 'unidad': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'elemento': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'folio_911': TextInput(
                attrs={
                    'CLASS': 'form-control'
                }
            ),
            'observaciones': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':3
                }
            )
        }

class DetenidosForm(forms.ModelForm):
    class Meta:
        model = Detenidos
        exclude = ('estatus',)

        widgets = {
            'fecha': DateInput(
                attrs={
                    'class': 'form-control ', 
                    'placeholder': 'DD/MM/AAAA'
                }
            ),
            'hora': TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'HH:MM'
                }
            ),
            'nombre_detenido': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'domicilio_detenido': TextInput(
                attrs={
                    'class': 'form-control',
                   
                }
            ),
             'edad_detenido': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'folio_911': TextInput(
                attrs={
                    'CLASS': 'form-control'
                }
            ),
            'folio_remision': TextInput(
                attrs={
                    'CLASS': 'form-control'
                }
            ),
            'ubicacion_vehiculo': TextInput(
                attrs={
                    'class': 'form-control',
                   
                }
            ),
            'marca_vehiculo': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo_vehiculo': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'placas_vehiculo': TextInput(
                attrs={
                    'class': 'form-control',
                    'onblur': 'validateText()'
                }
            ),
              'color_vehiculo': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'serie_vehiculo':TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'folio_infraccion': TextInput(
                attrs={
                    'class': 'form-control',
                    'max_length':8,
                                        
                }
            ),
             'numerales': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
             'inventario': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
             'grua': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ), 'unidad': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'elemento': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'observaciones': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':3
                }
            )

        }