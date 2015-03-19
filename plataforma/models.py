from django.db import models

class Rol(models.Model):
  nombre = models.CharField(max_length=200)
  

class Usuario(models.Model):
  nombres = models.CharField(max_length=200)
  apellido1 = models.CharField(max_length=200)
  apellido2 = models.CharField(max_length=200)
  numero_documento = models.CharField(max_length=200)
  rol = models.ForeignKey(Rol,default=None)
  

  