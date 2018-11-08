from django.db import models
from django.contrib import admin
from django.utils import timezone

class Solicitante(models.Model):
    nombre  =   models.CharField(max_length=150)
    email  =   models.EmailField(max_length=150)
    telefono  =   models.IntegerField()
    fecha_nacimiento = models.DateField()
    DPI  =   models.IntegerField()
    experiencia  =   models.CharField(max_length=500)

    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    nombre    = models.CharField(max_length=200)
    requisitos    = models.CharField(max_length=700)
    conocimientos    = models.CharField(max_length=700)
    beneficios      = models.CharField(max_length=700)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    solicitantes   = models.ManyToManyField(Solicitante, through='Solicitud')

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)

class SolicitudInLine(admin.TabularInline):
    model = Solicitud
    extra = 1

class SolicitanteAdmin(admin.ModelAdmin):
    inlines = (SolicitudInLine,)

class TrabajoAdmin (admin.ModelAdmin):
    inlines = (SolicitudInLine,)