from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),


    #Bitacora URLS's
    path('index-bitacora/',BitacoraCreate.as_view(), name='bitacora/index'), #Create
    path('update-bitacora/<int:pk>/', BitacoraUpdate.as_view(), name='bitacora/update'), #Edit
    path('bitacora/bitacora-data', BitacoraList.as_view(), name='bitacora/list'),
    path('data-bitacora/', BitacoraData.as_view(), name='bitacora/data'), #Data Display
    path('show-bitacora/<int:pk>/',BitacoraShow.as_view(), name='bitacora/show'), #Object Show
    path('delete-bitacora/<int:pk>/', BitacoraDelete.as_view(), name="bitacora/delete"), #Delete
    path('activate-bitacora/<int:pk>/', BitacoraActivate.as_view(), name='bitacora/activate'), #Activate Element/Estatus

    #Eventos y Apoyos URL's
    path('index-eventos/', EventosCreate.as_view(), name='eventos/index'), #Create
    path('update-eventos/<int:pk>/', EventosUpdate.as_view(), name='eventos/update'), #Edit
    path('eventos/eventos-data', EventosList.as_view(), name='eventos/list'),
    path('data-eventos/', EventosData.as_view(), name='eventos/data'), #Data Display
    path('show-eventos/<int:pk>/',EventosShow.as_view(), name='eventos/show'), #ShowObject Show
    path('delete-eventos/<int:pk>/', EventosDelete.as_view(), name='eventos/delete'), #Inactivate Element/Estatus
    path('activate-eventos/<int:pk>/', EventosActivate.as_view(), name='eventos/activate'), #Activate Element/Estatus

    #Mal Estacionados URL's
    path('index-mal-estacionados/', MalEstacionadosCreate.as_view(), name='mal-estacionados/index'), #Create
    path('update-mal-estacionados/<int:pk>/', MalEstacionadosUpdate.as_view(), name='mal-estacionados/update'), #Edit
    path('mal-estacionados/mal-estacionados-data', MalEstacionadosList.as_view(), name='mal-estacionados/list'),
    path('data-mal-estacionados/', MalEstacionadosData.as_view(), name='mal-estacionados/data'), #Data Display
    path('show-mal-estacionados/<int:pk>/',MalEstacionadosShow.as_view(), name='mal-estacionados/show'), #ShowObject Show
    path('delete-mal-estacionados/<int:pk>/', MalEstacionadosDelete.as_view(), name='mal-estacionados/delete'), #Inactivate Element/Estatus
    path('activate-mal-estacionados/<int:pk>/', MalEstacionadosActivate.as_view(), name='mal-estacionados/activate'), #Activate Element/Estatus


    #Apoyos a Preventiva URL's 
    path('index-apoyo-preventiva/', PreventivaCreate.as_view(), name='preventiva/index'), #Create
    path('update-preventiva/<int:pk>/', PreventivaUpdate.as_view(), name='preventiva/update'), #Update
    path('preventiva/apoyos-preventiva-data/', PreventivaList.as_view(), name='preventiva/list'), #List
    path('data-apoyo-preventiva/', PreventivaData.as_view(), name='preventiva/data'), #Data
    path('show-preventiva/<int:pk>/', PreventivaShow.as_view(), name='preventiva/show'), #Show
    path('delete-preventiva/<int:pk>/',PreventivaDelete.as_view(), name='preventiva/delete'), #Delete
    path('activate-preventiva/<int:pk>/',PreventivaActivate.as_view(), name='preventiva/activate'), #Activate

    #Accidentes Viales URL's

    #Create
    path('index-accidentes/', AccidentesCreate.as_view(), name='accidentes/index'), #Create
    path('<int:accidente_id>/accidente-atendido/', AccidentesAtendidoCreate.as_view(), name='accidentesAtendido/index'), #Create Atendido
    path('<int:accidente_id>/accidente-NoAtendido/', AccidentesNoAtendidoCreate.as_view(), name='accidentesNoAtendido/index'), #Create No Atendido
    path('<int:accidente_id>/conductor-accidente/', ConductorAccidente.as_view(), name='conductor/index'), #Create Conductores

    #Update
    path('update-accidentes/<int:pk>/', AccidentesEdit.as_view(), name='accidentes/update'), #Update
    path('update-accidente-atendido/<int:pk>/', AccidentesAtendidoEdit.as_view(), name='accidentesAtendido/update'), #Update
    path('update-conductores-accidente/<int:pk>/', ConductorAccidenteEdit.as_view(), name='conductoresAccidente/edit'),
    path('update-accidente-no-atendido/<int:pk>/', AccidentesNoAtendidoEdit.as_view(), name='accidentesNoAtendido/update'),

    #Display data
    path('accidentes/accidentes-data', AccidentesList.as_view(), name='accidentes/list'),
    path('accidentes-data/', AccidentesData.as_view(), name='accidentes/data'), #Data Display
    path('show-accidente/<int:pk>/', AccidenteShow.as_view(), name='accidentes/show'), #Show

    #Delete - Activate
    path('delete-accidentes/<int:pk>/', AccidentesDelete.as_view(), name='accidentes/delete'), #Delete
    path('activate-accidentes/<int:pk>/', AccidentesActivate.as_view(), name='accidentes/activate'),#Activate

    #Vehiculos al Corralon URL's
    path('index-vehiculos-corralon/', VehiculosCorralonCreate.as_view(), name='corralon/index'), #Create
    path('update-vehiculos-corralon/<int:pk>/', VehiculosCorralonUpdate.as_view(), name='corralon/update'), #Update
    path('corralon/vehiculos-corralon-data/', VehiculosCorralonList.as_view(), name= 'corralon/list'), #List
    path('data-vehiculos-corralon/', VehiculosCorralonData.as_view(), name='corralon/data'), #Data Display
    path('show-vehiculos-corralon/<int:pk>/', VehiculosCorralonShow.as_view(), name='corralon/show'), #Show
    path('delete-vehiculos-corralon/<int:pk>/', VehiculosCorralonDelete.as_view(), name='corralon/delete'), #Delete
    path('activate-vehiculos-corralon/<int:pk>/',VehiculosCorralonActivate.as_view(), name='corralon/activate'), #Activate
    
    #Detenidos URL's
    path('index-detenidos/', DetenidosCreate.as_view(), name='detenidos/index'), #Create
    path('update-detenidos/<int:pk>/', DetenidosUpdate.as_view(), name='detenidos/update'), #Update
    path('detenidos/detenidos-data/', DetenidosList.as_view(), name='detenidos/list'),
    path('data-detenidos/', DetenidosData.as_view(), name='detenidos/data'),
    path('show-detenidos/<int:pk>/', DetenidosShow.as_view(), name='detenidos/show'),#Show
    path('delete-detenidos/<int:pk>/', DetenidosDelete.as_view(), name='detenidos/delete'),#Delete
    path('activate-detenidos/<int:pk>/', DetenidosActivate.as_view(), name='detenidos/activate'),#Activate



]   