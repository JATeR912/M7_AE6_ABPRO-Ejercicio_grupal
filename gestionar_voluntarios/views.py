from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import transaction, IntegrityError
from django.contrib import messages
from .models import Voluntario, Evento
from .forms import VoluntarioForm, EventoForm

def index(request):
    return render(request, 'index.html')
    
def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all().order_by('-id')
    return render(request, 'voluntarios/lista_voluntarios.html', {'voluntarios': voluntarios})

def detalle_voluntario(request, voluntario_id):
    voluntario = get_object_or_404(Voluntario, id=voluntario_id)
    return render(request, 'voluntarios/detalle_voluntarios.html', {'voluntario': voluntario})

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    voluntario = form.save()
                messages.success(request, "Voluntario creado correctamente.")
                return redirect('lista_voluntarios')
            except IntegrityError:
                messages.error(request, "Ocurrio un error al crear el voluntario.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = VoluntarioForm()
    return render(request, 'voluntarios/voluntarios_form.html', {'form': form, 'accion': 'Crear'})

def actualizar_voluntario(request, voluntario_id):
    voluntario = get_object_or_404(Voluntario, id=voluntario_id)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                messages.success(request, "Voluntario actualizado correctamente.")
                return redirect('lista_voluntarios')
            except IntegrityError:
                messages.error(request, "Ocurrió un error al actualizar el voluntario.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'voluntarios/voluntarios_form.html', {'form': form, 'accion': 'Actualizar'})

def voluntario_delete(request, voluntario_id):
    voluntario = get_object_or_404(Voluntario, id=voluntario_id)
    if request.method == 'POST':
        voluntario.delete()
        messages.success(request, "Voluntario eliminado.")
        return redirect('lista_voluntarios')
    return render(request, 'voluntarios/voluntarios_delete.html', {'voluntario': voluntario})


def lista_eventos(request):
    eventos = Evento.objects.all().order_by('-id')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'eventos/detalle_eventos.html', {'evento': evento})


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    evento = form.save()
                    evento.creador = request.user
                    evento.save()
                messages.success(request, "Evento creado correctamente.")
                return redirect('lista_eventos')
            except IntegrityError:
                messages.error(request, "Ocurrio un error al crear el evento.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = EventoForm()
    return render(request, 'eventos/eventos_form.html', {'form': form, 'accion': 'Crear'})

def actualizar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    evento.creador = request.user
                    evento.save()
                messages.success(request, "Evento actualizado correctamente.")
                return redirect('lista_eventos')
            except IntegrityError:
                messages.error(request, "Ocurrió un error al actualizar el evento.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/eventos_form.html', {'form': form, 'accion': 'Actualizar'})

def evento_delete(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, "Evento eliminado.")
        return redirect('lista_eventos')
    return render(request, 'eventos/eventos_delete.html', {'evento': evento})