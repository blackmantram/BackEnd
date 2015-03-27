from django.db import models
from django.conf.urls import url

class Rol(models.Model):
  nombre = models.CharField(max_length=200)

class RedSocial(models.Model):
    nombre = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    icono = models.CharField(max_length=200, blank=True,default=None)
    
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
  correo_institucion = models.CharField(max_length=200, blank=True,default=None)
  NIT = models.CharField(max_length=200, blank=True,default=None)
  rol = models.ForeignKey(Rol,blank=False)
  redes = models.ManyToManyField(RedSocial, through='UsuarioRedes')
  

class UsuarioRedes(models.Model):    
    url = models.CharField(max_length=200)  
    usuario = models.ForeignKey(Usuario,blank=False)
    red_social = models.ForeignKey(RedSocial,blank=False)