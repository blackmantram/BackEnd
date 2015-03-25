from django.db import models

class Rol(models.Model):
  nombre = models.CharField(max_length=200)
  

class Usuario(models.Model):
  nombres = models.CharField(max_length=200)
  apellido1 = models.CharField(max_length=200)
  apellido2 = models.CharField(max_length=200)
  numero_documento = models.CharField(max_length=200)
  correo = models.CharField(max_length=200, blank=True,default=None)
  nombre_institucion = models.CharField(max_length=200, blank=True,default=None)
  telefono_institucion = models.CharField(max_length=200, blank=True,default=None)
  ubicacion_institucion = models.CharField(max_length=200, blank=True,default=None)
  direccion_institucion = models.CharField(max_length=200, blank=True,default=None)
  NIT = models.CharField(max_length=200, blank=True,default=None)
  rol = models.ForeignKey(Rol,default=None)
  

  