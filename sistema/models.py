from django.db import models
from django.contrib.auth.models import AbstractUser


class Persona(models.Model):
    class Meta: 
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
    documento = models.CharField('Documento', max_length=50)
    cedulaDeIdentidad = "ci"
    pasaporte = "pass"
    dni = "dni"
    tiposDeDocumentoElec = (
        (cedulaDeIdentidad, 'Cédula de Identidad'),
        (pasaporte, 'Pasaporte'),
        (dni, 'Documento Nacional de Identificación (Arg)'),
    )
    tipoDeDocumento = models.CharField(
        'Tipo de documento',
        max_length=5,
        choices=tiposDeDocumentoElec,
        default=cedulaDeIdentidad,
    )
    nombre = models.CharField('Nombre', max_length=200)
    direccion = models.CharField('Dirección', max_length=200)
    numeroTelefono = models.CharField('Número de Teléfono', max_length=200)

    def __str__(self):
        return self.nombre

class Vacuna(models.Model):
    class Meta: 
        verbose_name = "Vacuna"
        verbose_name_plural = "Vacunas"
    nombre = models.CharField('Nombre', max_length=200)
    laboratorio = models.CharField('Laboratorio', max_length=200)

    def __str__(self):
        return self.nombre + ' de ' + self.laboratorio

class Vacunatorio(models.Model):
    class Meta: 
        verbose_name = "Vacunatorio"
        verbose_name_plural = "Vacunatorios"
    nombre = models.CharField('Nombre', max_length=200)
    direccion = models.CharField('Dirección', max_length=200)

    def __str__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

class Vacunacion(models.Model):
    class Meta: 
        verbose_name = "Vacunacion"
        verbose_name_plural = "Vacunacion"
    vacuna = models.ForeignKey(Vacuna, on_delete=models.PROTECT)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    fecha = models.DateTimeField('Día')
    vacunatorio = models.ForeignKey(Vacunatorio, on_delete=models.PROTECT)

    def __str__(self):
        return self.persona.nombre + ' - ' + self.vacuna.nombre 

class Usuario(AbstractUser):
    vacunatorio = models.ForeignKey(Vacunatorio, on_delete=models.PROTECT, null=True, blank=False)
    class Meta: 
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
