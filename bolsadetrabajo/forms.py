from django import forms
from .models import Solicitante, Trabajo, Solicitud

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ('nombre', 'requisitos', 'conocimientos', 'beneficios', 'fecha_publicacion')

class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ('nombre', 'email','telefono','fecha_nacimiento','DPI','experiencia')