from django.contrib import admin
from bolsadetrabajo.models import Solicitante, SolicitanteAdmin, Trabajo, TrabajoAdmin

admin.site.register(Solicitante, SolicitanteAdmin)
admin.site.register(Trabajo, TrabajoAdmin)
