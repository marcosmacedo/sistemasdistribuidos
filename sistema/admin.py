from django.contrib import admin

# Register your models here.
from .models import *

class VacunacionAdmin(admin.ModelAdmin):
    list_display = ('vacuna','persona', 'fecha', 'vacunatorio')
    autocomplete_fields = ['persona', 'vacunatorio']

class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class VacunatorioAdmin(admin.ModelAdmin):
    search_fields = ['nombre']


admin.site.register(Vacuna)
admin.site.register(Vacunacion, VacunacionAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Vacunatorio, VacunatorioAdmin)
