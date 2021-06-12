from django.contrib import admin

# Register your models here.
from .models import *

class VacunacionAdmin(admin.ModelAdmin):
    list_display = ('vacuna','persona', 'fecha', 'vacunatorio')

admin.site.register(Vacuna)
admin.site.register(Vacunacion, VacunacionAdmin)
admin.site.register(Persona)
admin.site.register(Vacunatorio)
