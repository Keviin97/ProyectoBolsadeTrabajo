from django.shortcuts import render, get_object_or_404
from .forms import TrabajoForm, SolicitanteForm
from bolsadetrabajo.models import Trabajo, Solicitud, Solicitante
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect


@login_required
def trabajo_nuevo(request):
    if request.method == "POST":
        formulario = TrabajoForm(request.POST)
        if formulario.is_valid():
            trabajo = Trabajo.objects.create(nombre=formulario.cleaned_data['nombre'], requisitos = formulario.cleaned_data['requisitos'], conocimientos = formulario.cleaned_data['conocimientos'], beneficios = formulario.cleaned_data['beneficios'], fecha_publicacion = formulario.cleaned_data['fecha_publicacion'])
            messages.add_message(request, messages.SUCCESS, 'Trabajo guardado exitosamente!')
    else:
        formulario = TrabajoForm()
    return render(request, 'bolsadetrabajo/trabajo_editar.html', {'formulario': formulario})


def listar_trabajos(request):
    lista = Trabajo.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'bolsadetrabajo/listar_trabajos.html', {'lista': lista})


def listar_solicitantes(request):
    listado = Solicitante.objects.filter(fecha_nacimiento__lte=timezone.now()).order_by('fecha_nacimiento')
    return render(request, 'bolsadetrabajo/listar_solicitantes.html', {'listado': listado})


def detalle_trabajo(request, pk):
    post = get_object_or_404(Trabajo, pk=pk)
    return render(request, 'bolsadetrabajo/detalle_trabajo.html', {'post': post})


def detalle_solicitante(request, pk):
    post = get_object_or_404(Solicitante, pk=pk)
    return render(request, 'bolsadetrabajo/detalle_solicitante.html', {'post': post})

@login_required
def nuevo_solicitante(request):
    if request.method == "POST":
        form = SolicitanteForm(request.POST)
        if form.is_valid():
            post = Solicitante.objects.create(nombre=form.cleaned_data['nombre'], email = form.cleaned_data['email'], telefono = form.cleaned_data['telefono'], fecha_nacimiento = form.cleaned_data['fecha_nacimiento'], DPI = form.cleaned_data['DPI'], experiencia = form.cleaned_data['experiencia'])
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Solicitante guardado exitosamente!')
    else:
        form = SolicitanteForm()
    return render(request, 'bolsadetrabajo/editar_solicitante.html', {'form': form})

@login_required
def editar_trabajo(request, pk):
    post = get_object_or_404(Trabajo, pk=pk)
    if request.method == "POST":
        form = TrabajoForm(request.POST, instance=post)
        if form.is_valid():
            trabajo = Trabajo.objects.filter(pk=pk).update(nombre=form.cleaned_data['nombre'], requisitos = form.cleaned_data['requisitos'], conocimientos = form.cleaned_data['conocimientos'], beneficios = form.cleaned_data['beneficios'], fecha_publicacion = form.cleaned_data['fecha_publicacion'])
            messages.add_message(request, messages.SUCCESS, 'Trabajo actualizado exitosamente!')
            return redirect('detalle_trabajo', pk=post.pk)
    else:
        form = TrabajoForm(instance=post)
    return render(request, 'bolsadetrabajo/editar_trabajo.html', {'form': form})

@login_required
def editar_solicitante(request, pk):
    post = get_object_or_404(Solicitante, pk=pk)
    if request.method == "POST":
        form = SolicitanteForm(request.POST, instance=post)
        if form.is_valid():
            solicitante = Solicitante.objects.filter(pk=pk).update(nombre=form.cleaned_data['nombre'], email = form.cleaned_data['email'], telefono = form.cleaned_data['telefono'], fecha_nacimiento = form.cleaned_data['fecha_nacimiento'], DPI = form.cleaned_data['DPI'], experiencia = form.cleaned_data['experiencia'])
            messages.add_message(request, messages.SUCCESS, 'Solicitante actualizado exitosamente!')
            return redirect('detalle_solicitante', pk=post.pk)
    else:
        form = SolicitanteForm(instance=post)
    return render(request, 'bolsadetrabajo/editar_solicitante.html', {'form': form})

@login_required
def eliminar_solicitante(request, pk):
    post = get_object_or_404(Solicitante, pk=pk)
    post.delete()
    return redirect('listar_solicitantes')

@login_required
def eliminar_trabajo(request, pk):
    post = get_object_or_404(Trabajo, pk=pk)
    post.delete()
    return redirect('listar_trabajos')