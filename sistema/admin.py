from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *

class VacunacionAdmin(admin.ModelAdmin):
    list_display = ('vacuna','persona', 'fecha', 'vacunatorio')
    autocomplete_fields = ['persona', 'vacunatorio']

class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class VacunatorioAdmin(admin.ModelAdmin):
    search_fields = ['nombre']


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "vacunatorio":
            if not request.user.is_superuser:
                kwargs["queryset"] = Vacunatorio.objects.filter(id=request.user.vacunatorio.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(vacunatorio=request.user.vacunatorio)

    def limitar_propio_vacunatorio(self, request):
        if request.user.is_superuser:
            return {}    
        return {'nombre': request.user.vacunatorio.nombre}

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipoDeDocumento', 'documento', 'direccion')

class VacunatorioAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion')

class VacunaAdmin(admin.ModelAdmin):
    list_display = ('nombre','laboratorio')

class VacunacionUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('vacunatorio',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'vacunatorio'),}),)

    ordering = ('last_name', 'first_name',)

    class Meta:
        model = Usuario


admin.site.register(Vacuna, VacunaAdmin)
admin.site.register(Vacunacion, VacunacionAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Vacunatorio, VacunatorioAdmin)
admin.site.register(Usuario, VacunacionUserAdmin)
