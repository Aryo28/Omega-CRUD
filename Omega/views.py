import json
from django.core import serializers
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView


# Create your views here.


class Inicio(TemplateView): #Inicio CBV
    template_name = 'vistas/menu.html'


def inicio(request):
    return render(request, 'vistas/inicio.html')


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


#************************************************Bitacora*************************************
class BitacoraCreate(CreateView): #Create CBV
    model = Bitacora
    template_name = 'vistas/bitacora/index.html'
    form_class = BitacoraForm
    success_url =  reverse_lazy('bitacora/data')

class BitacoraUpdate(UpdateView): #Edit CBV
    model = Bitacora
    template_name = 'vistas/bitacora/modalEdit.html'
    form_class = BitacoraForm
    success_url = reverse_lazy('bitacora/data')

class BitacoraList(ListView): #Data Display
    context_object_name = 'data'
    template_name = 'vistas/bitacora/data.html'

    def get_queryset(self): 
        myset ={
                'filtrar_carrusel': Bitacora.objects.filter(motivo = 'CARRUSEL').count(),
                'filtrar_infracciones': Bitacora.objects.filter(motivo = 'INFRACCION').filter(estatus='ACTIVO').count(),
                'prueba_filtro': Bitacora.objects.filter(observaciones = 'PUERTA A BODEGA').count(),
            }
        return myset

class BitacoraData(ListView): #Ajax
    model = Bitacora

    def get(self,request, *args, **kwargs):
        if is_ajax(request=request):
            context = Bitacora.objects.filter().order_by('-id')
            return HttpResponse(serialize('json', context), content_type='application/json')
        else:
            return redirect('bitacora/list')

class BitacoraShow(DetailView): #Data Show CBV
    model = Bitacora
    template_name = 'vistas/bitacora/show.html'
    context_object_name = 'registro'
    pk_url_kwargs = 'id'

class BitacoraDelete(DeleteView): #Delete/Inactivate CBV
    model = Bitacora
    template_name = 'vistas/bitacora/bitacora_confirm_delete.html'
    
    def post(self, request, pk, *args, **kwargs):
        object = Bitacora.objects.get(id = pk)
        object.estatus = 'INACTIVO'
        object.save()
        return redirect('bitacora/data')

class BitacoraActivate(DetailView): #Activate Element CBV
    model = Bitacora
    template_name = 'vistas/bitacora/bitacora_activate_confirm.html'
    context_object_name = 'object'
    pk_url_kwargs = 'id'

    def post(self, request, pk, *args, **kwargs):
        elementToactivate = Bitacora.objects.get(id=pk)
        elementToactivate.estatus = 'ACTIVO'
        elementToactivate.save()
        return redirect('bitacora/data')

#********************************************************************************************

#***************************************Eventos*************************************************
class EventosCreate(CreateView): #Create CBV
    model = Eventos
    template_name = 'vistas/EventosApoyos/index.html'
    form_class = EventoForm
    success_url = reverse_lazy('eventos/data')

class EventosUpdate(UpdateView): #Edit CBV
    model = Eventos
    template_name = 'vistas/EventosApoyos/modalEdit.html'
    form_class = EventoForm
    success_url = reverse_lazy('eventos/data')

class EventosList(ListView): #Data Display
    context_object_name = 'data'
    template_name = 'vistas/EventosApoyos/data.html'

    def get_queryset(self): 
        myset ={
                'labor_social': Eventos.objects.filter(tipo_evento = 'LABOR SOCIAL').filter(estatus='ACTIVO').count(),
                'puntos_fijos': Eventos.objects.filter(tipo_evento = 'PUNTOS FIJOS').filter(estatus='ACTIVO').count(),
            }
        return myset  

class EventosData(ListView): #Ajax
    model = Eventos

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            context = Eventos.objects.all().order_by('id')
            return HttpResponse(serialize('json', context), content_type='application/json')
        else:
            return redirect('eventos/list')




class EventosShow(DetailView): #Data Show CBV
    model = Eventos
    template_name = 'vistas/EventosApoyos/show.html'
    context_object_name = 'registro'
    pk_url_kwargs = 'id'

class EventosDelete(DeleteView): #Delete/Inactivate CBV
    model = Eventos
    template_name = 'vistas/EventosApoyos/eventos_confirm_delete.html'
    
    def post(self, request, pk, *args, **kwargs):
        object = Eventos.objects.get(id = pk)
        object.estatus = 'INACTIVO'
        object.save()
        return redirect('eventos/data')

class EventosActivate(DetailView): #Activate Element CBV
    model = Eventos
    template_name = 'vistas/EventosApoyos/eventos_activate_confirm.html'
    context_object_name = 'object'
    pk_url_kwargs = 'id'

    def post(self, request, pk, *args, **kwargs):
        elementToactivate = Eventos.objects.get(id=pk)
        elementToactivate.estatus = 'ACTIVO'
        elementToactivate.save()
        return redirect('eventos/data')

#*****************************************************************


#**************************Mal Estacionados*******************************************

class MalEstacionadosCreate(CreateView): #Create CBV
    model = MalEstacionados
    template_name = 'vistas/malEstacionados/index.html'
    form_class = MalEstacionadosForm
    success_url= reverse_lazy('mal-estacionados/data')

class MalEstacionadosList(ListView): #Data Display CBV
    context_object_name = 'data'
    template_name = 'vistas/malEstacionados/data.html'

    def get_queryset(self): #Multi Querysets
        myset = {
            'atendido':MalEstacionados.objects.filter(estatus_servicio = 'ATENDIDO').filter(estatus = 'ACTIVO').order_by('-id').count(),
            'noAtendido':MalEstacionados.objects.filter(estatus_servicio = 'NO ATENDIDO').filter(estatus = 'ACTIVO').order_by('-id').count(),
        }
        return myset

class MalEstacionadosUpdate(UpdateView): #Edit CBV
    model = MalEstacionados
    template_name = 'vistas/malEstacionados/modalEdit.html'
    form_class = MalEstacionadosForm
    success_url = reverse_lazy('mal-estacionados/data')

class MalEstacionadosData(ListView): #Ajax
    model = MalEstacionados

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            context = MalEstacionados.objects.all().order_by('id')
            return HttpResponse(serialize('json', context, use_natural_foreign_keys=True, use_natural_primary_keys=True),
                content_type='application/json')
        else:
            return redirect('mal-estacionados/list')

class MalEstacionadosShow(DetailView): #Show
    model = MalEstacionados
    template_name = 'vistas/malEstacionados/show.html'
    context_object_name = 'registro'
    pk_url_kwargs = 'id'

class MalEstacionadosDelete(DeleteView): #Delete/Inactivate CBV
    model = MalEstacionados
    template_name = 'vistas/malEstacionados/malEstacionados_confirm_delete.html'
    
    def post(self, request, pk, *args, **kwargs):
        object = MalEstacionados.objects.get(id = pk)
        object.estatus = 'INACTIVO'
        object.save()
        return redirect('mal-estacionados/data')

class MalEstacionadosActivate(DetailView): #Activate Element CBV
    model = MalEstacionados
    template_name = 'vistas/malEstacionados/malEstacionados_activate.html'
    context_object_name = 'object'
    pk_url_kwargs = 'id'

    def post(self, request, pk, *args, **kwargs):
        elementToactivate = MalEstacionados.objects.get(id=pk)
        elementToactivate.estatus = 'ACTIVO'
        elementToactivate.save()
        return redirect('mal-estacionados/data')

#****************************************************************************************

#*****************************APOYOS A PREVENTIVA***************************************

class PreventivaCreate(CreateView): #Create
    model = ApoyosPreventiva
    template_name = 'vistas/apoyosPreventiva/index.html'
    form_class = ApoyoPreventivaForm
    success_url = reverse_lazy('preventiva/data')
    
class PreventivaUpdate(UpdateView): #Update
    model = ApoyosPreventiva
    template_name = 'vistas/apoyosPreventiva/modalEdit.html'
    form_class = ApoyoPreventivaForm
    success_url = reverse_lazy('preventiva/data')

class PreventivaList (ListView): #Data Display
    context_object_name = 'data'
    template_name = 'vistas/apoyosPreventiva/data.html'

    def get_queryset(self):
        myset ={
            'infracciones': ApoyosPreventiva.objects.filter(estatus = 'ACTIVO').filter(evento='INCIDENTE POR INFRACCION').count()
        }
        return myset

class PreventivaData (ListView): #Ajax 
    model = ApoyosPreventiva

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            context = ApoyosPreventiva.objects.all().order_by('id')
            return HttpResponse(serialize('json', context, use_natural_foreign_keys=True, use_natural_primary_keys=True),
                content_type='application/json')
        else:
            return redirect('preventiva/list') 

class PreventivaShow(DetailView): #Show
    model = ApoyosPreventiva
    template_name = 'vistas/apoyosPreventiva/show.html'
    context_object_name = 'registro'
    pk_url_kwargs = 'id'

class PreventivaDelete(DeleteView): #Delete
    model = ApoyosPreventiva
    template_name = 'vistas/apoyosPreventiva/preventiva_confirm_delete.html'

    def post(self, request, pk, *args, **kwargs):
        object = ApoyosPreventiva.objects.get(id = pk)
        object.estatus = 'INACTIVO'
        object.save()
        return redirect('preventiva/data')

class PreventivaActivate(DetailView): #Activate Element
    model = ApoyosPreventiva
    template_name = 'vistas/apoyosPreventiva/preventiva_activate_confirm.html'
    context_object_name = 'object'
    pk_url_kwargs = 'id'

    def post(self, request, pk, *args, **kwargs):
        elementToactivate = ApoyosPreventiva.objects.get(id=pk)
        elementToactivate.estatus = 'ACTIVO'
        elementToactivate.save()
        return redirect('preventiva/data')

#******************************************************************************************


#*********************************ACCIDENTES VIALES*************************************

# Crear nuevos registros
class AccidentesCreate(CreateView):
    model = AccidenteVial
    template_name = 'vistas/accidentes_viales/index.html'
    form_class = AccidentesForm
    
    def form_valid(self, form):  #Redireccionar de acuerdo al estatus y enviar ID por URL
        self.object = form.save()
        self.object.estatus = form.cleaned_data['estatus_accidente']
        accidente_id = self.object.id
        if(self.object.estatus == 'ATENDIDO'):
            return HttpResponseRedirect(reverse('accidentesAtendido/index', args=(accidente_id,)))
        if(self.object.estatus == 'NO ATENDIDO'):
             return HttpResponseRedirect(reverse('accidentesNoAtendido/index', args=(accidente_id,)))

class AccidentesAtendidoCreate(CreateView): #Create-acc atendido
    model = AccidenteVialAtendido
    template_name = 'vistas/accidentes_viales/atendidos/index.html'
    form_class = AccidentesAtendidoForm

    def get_context_data(self, **kwargs): #Obtener parametros de URL 
        context = super(AccidentesAtendidoCreate, self).get_context_data(**kwargs)
        context['accidenteID'] = self.kwargs['accidente_id']
        return context  

    def form_valid(self, form ):   #Guardar nuevo objeto y actualizar el campo de id_accidente 
        self.object = form.save()
        self.object.id_accidente_id = self.kwargs['accidente_id']
        self.object.save()
        return HttpResponseRedirect(reverse('conductor/index', args=(self.kwargs['accidente_id'],)) )       
   
class AccidentesNoAtendidoCreate(CreateView): #Create-acc No atendido
    model = AccidenteVialNoAtendido
    template_name = 'vistas/accidentes_viales/noAtendidos/index.html'
    form_class = AccidentesNoAtendidoForm

    
    def get_context_data(self, **kwargs): #Obtener parametros de URL 
        context = super(AccidentesNoAtendidoCreate, self).get_context_data(**kwargs)
        return context  

    def form_valid(self, form ):   #Guardar nuevo objeto y actualizar el campo de id_accidente 
        self.object = form.save()
        self.object.id_accidente_id = self.kwargs['accidente_id']
        self.object.save()
        return HttpResponseRedirect(reverse('accidentes/index')) 

class ConductorAccidente(CreateView): #Create-acc conductor
    model = AccidenteConductores
    template_name = 'vistas/accidentes_viales/conductorAccidente/index.html'
    form_class = ConductorAccidenteForm
    
    def get_context_data(self, **kwargs): #Obtener parametros de URL 
        context = super(ConductorAccidente, self).get_context_data(**kwargs)
        context['accidenteID'] = self.kwargs['accidente_id']
        return context  

    def form_valid(self, form):
        self.object = form.save()
        self.object.id_accidente_id = self.kwargs['accidente_id']
        self.object.save()
        return HttpResponseRedirect(reverse('conductor/index', args=(self.kwargs['accidente_id'],)) )

#Display de registros
class AccidentesList (ListView): #Data Display
    context_object_name = 'data'
    template_name = 'vistas/accidentes_viales/data.html'

    def get_queryset(self):
        myset ={    
            'atendidos': AccidenteVial.objects.filter(estatus = 'ACTIVO').filter(estatus_accidente='ATENDIDO').count(),
            'noAtendidos': AccidenteVial.objects.filter(estatus = 'ACTIVO').filter(estatus_accidente='NO ATENDIDO').count()
        }
        return myset

class AccidentesData (ListView): #Ajax 
    model = AccidenteVial

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            context = AccidenteVial.objects.all().order_by('id')
            return HttpResponse(serialize('json', context, use_natural_foreign_keys=True, use_natural_primary_keys=True),
                content_type='application/json')
        else:
            return redirect('accidentes/list') 

class AccidenteShow(TemplateView): #Show con templateView 

    template_name = 'vistas/accidentes_viales/show.html'

    '''
    Querys de mulitples modelos en una sola vista, filtrando por el id del accidente
    El Id del accidente se obtiene de la URL (self.kwargs['pk'])
    '''

    def get_context_data(self, **kwargs): 
        context = super(AccidenteShow, self).get_context_data(**kwargs)
        context['accidente'] = AccidenteVial.objects.filter(id = self.kwargs['pk'])
        context['accidenteAtendido'] = AccidenteVialAtendido.objects.filter(id_accidente_id = self.kwargs['pk'])
        context['accidenteConductor'] = AccidenteConductores.objects.filter(id_accidente_id = self.kwargs['pk'])
        context['accidenteNoAtendido'] = AccidenteVialNoAtendido.objects.filter(id_accidente_id = self.kwargs['pk'])
        return context

#Edicion de Registror      
class AccidentesEdit(UpdateView): #Update accidente
    model = AccidenteVial
    template_name = 'vistas/accidentes_viales/modalEdit.html'
    form_class = AccidentesForm  
        

    def form_valid(self, form, **kwargs):  #Redireccionar de acuerdo al estatus y enviar ID por URL
        self.object = form.save()
        self.object.estatus = form.cleaned_data['estatus_accidente']
        pk = self.object.id
        return HttpResponseRedirect(reverse('accidentes/data'))  

class AccidentesAtendidoEdit(UpdateView): #Update accidente atendido
    model = AccidenteVialAtendido
    template_name = 'vistas/accidentes_viales/atendidos/atendidoEdit.html'
    form_class = AccidentesAtendidoForm
    
    def get_object(self, **kwargs): #Obtener registro usando el id del accidente y no del registro
        return AccidenteVialAtendido.objects.filter(id_accidente = self.kwargs['pk']).first()

    def get_context_data(self, **kwargs): #Obtener parametros de URL 
        context = super(AccidentesAtendidoEdit, self).get_context_data(**kwargs)
        context['accidenteID'] = self.kwargs['pk']
        return context  

    def form_valid(self, form ):   #Guardar nuevo objeto y actualizar el campo de id_accidente 
        self.object = form.save()
        self.object.id_accidente_id = self.kwargs['pk']
        self.object.save()
        return HttpResponseRedirect(reverse('accidentes/data'))

class ConductorAccidenteEdit(UpdateView):
    model = AccidenteConductores
    template_name = 'vistas/accidentes_viales/conductorAccidente/index.html'
    form_class = ConductorAccidenteForm
    success_url = reverse_lazy('accidentes/data')


    def get_object(self,**kwargs):
        return AccidenteConductores.objects.filter(id_accidente_id = self.kwargs['pk']).first()

class AccidentesNoAtendidoEdit(UpdateView):
    model = AccidenteVialNoAtendido
    template_name = 'vistas/accidentes_viales/noAtendidos/noAtendidoEdit.html'
    form_class = AccidentesNoAtendidoForm
    success_url = reverse_lazy('accidentes/data')

    def get_object(self, **kwargs): #Obtener registro usando el id del accidente y no del registro
        return AccidenteVialNoAtendido.objects.filter(id_accidente = self.kwargs['pk']).first()
    
# Delete y Activate
class AccidentesDelete(DetailView):
    model = AccidenteVial
    template_name = 'vistas/accidentes_viales/accidentes_confirm_delete.html'

    def post(self, request, pk, *args, **kwargs):
        object = AccidenteVial.objects.get(id = pk)
        object.estatus = 'INACTIVO'
        object.save()
        return redirect('accidentes/data')

class AccidentesActivate(DetailView):
    model = AccidenteVial
    template_name = 'vistas/accidentes_viales/accidentes_confirm_activate.html'
        
    def post(self, request, pk, *args, **kwargs):
        elementToactivate = AccidenteVial.objects.get(id=pk)
        elementToactivate.estatus = 'ACTIVO'
        elementToactivate.save()
        return redirect('accidentes/data')

#**********************************************************************************************


#*****************************Vehiculos al Corralon*******************************************
class VehiculosCorralonCreate(CreateView):
    model = VehiculosCorralon
    template_name = 'vistas/vehiculos_corralon/index.html'
    form_class = VehiculosCorralonForm
    success_url = reverse_lazy('corralon/data')

class VehiculosCorralonList(ListView):
    context_object_name = 'data'
    template_name = 'vistas/vehiculos_corralon/data.html'

    def get_queryset(self):
        myset ={    
            'activo': VehiculosCorralon.objects.filter(estatus = 'ACTIVO').count(),
            'inactivo': VehiculosCorralon.objects.filter(estatus = 'INACTIVO').count()
        }
        return myset

class VehiculosCorralonUpdate(UpdateView): #Edit CBV
    model = VehiculosCorralon
    template_name = 'vistas/vehiculos_corralon/modalEdit.html'
    form_class = VehiculosCorralonForm
    success_url = reverse_lazy('corralon/data')

class VehiculosCorralonData(ListView): #Ajax
    model = VehiculosCorralon

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            context = VehiculosCorralon.objects.all().order_by('id')
            return HttpResponse(serialize('json', context, use_natural_foreign_keys=True, use_natural_primary_keys=True),
                content_type='application/json')
        else:
            return redirect('corralon/list')

class VehiculosCorralonShow(DetailView):
    model = VehiculosCorralon
    template_name = 'vistas/vehiculos_corralon/show.html'
    context_object_name = 'object'
    pk_url_kwargs = 'id'

class VehiculosCorralonDelete(DetailView):
    model = VehiculosCorralon
    template_name = 'vistas/vehiculos_corralon/corralon_confirm_delete.html'

    def post(self, request, pk, *args, **kwargs):
        object = VehiculosCorralon.objects.get(id = pk)
        object.estatus = 'INACTIVO'
        object.save()
        return redirect('corralon/data')

class VehiculosCorralonActivate(DetailView):
    model = VehiculosCorralon
    template_name = 'vistas/vehiculos_corralon/corralon_confirm_activate.html'

    def post(self, request, pk, *args, **kwargs):
        object = VehiculosCorralon.objects.get(id = pk)
        object.estatus = 'ACTIVO'
        object.save()
        return redirect('corralon/data')

#*************************************************************************************************

#*********************************Detenidos*******************************************************
class DetenidosCreate(CreateView):
    model = Detenidos
    template_name = 'vistas/detenidos/index.html'
    form_class = DetenidosForm
    success_url = reverse_lazy('detenidos/data')

class DetenidosUpdate(UpdateView):
    model = Detenidos
    form_class = DetenidosForm
    template_name = 'vistas/detenidos/edit.html'
    success_url = reverse_lazy('detenidos/data')

class DetenidosData(ListView):
    model = Detenidos

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            context = Detenidos.objects.all().order_by('id')
            return HttpResponse(serialize('json', context, use_natural_foreign_keys=True, use_natural_primary_keys=True),
                content_type='application/json')
        else:
            return redirect('detenidos/list')

class DetenidosList(ListView):
    context_object_name = 'data'
    template_name = 'vistas/detenidos/data.html'

    def get_queryset(self):
        myset ={    
            'activo': Detenidos.objects.filter(estatus = 'ACTIVO').count(),
            'inactivo': Detenidos.objects.filter(estatus = 'INACTIVO').count()
        }
        return myset

class DetenidosShow(DetailView):
    model = Detenidos
    template_name = 'vistas/detenidos/show.html'
    context_object_name ='object'
    pk_url_kwargs = 'id'

class DetenidosDelete(DetailView):
    model = Detenidos
    template_name = 'vistas/detenidos/detenidos_confirm_delete.html'

    def post(self, request, pk, *args, **kwargs):
        object = Detenidos.objects.get(id = pk)
        object.estatus = 'INACTIVO'
        object.save()
        return redirect('detenidos/data')

class DetenidosActivate(DetailView):
    model = Detenidos
    template_name = 'vistas/detenidos/detenidos_confirm_activate.html'

    def post(self, request, pk, *args, **kwargs):
        object = Detenidos.objects.get(id = pk)
        object.estatus = 'ACTIVO'
        object.save()
        return redirect('detenidos/data')

#*****************************************************************************************************



'''    
class AccidentesAtendidoEdit(UpdateView):

Puede servir en el futuro
if 'next' in request.POST:
    return redirect(request.POST.get('next'))
else:
'''







   