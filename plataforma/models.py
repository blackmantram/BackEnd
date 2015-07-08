from django.db import models
from django.conf.urls import url

class Rol(models.Model):
  nombre = models.CharField(max_length=200)
  descripcion = models.CharField(max_length=200, blank=True, null=True)
  imagen = models.CharField(max_length=200, blank=True, null=True)

class RedSocial(models.Model):
    nombre = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    icono = models.CharField(max_length=200, blank=True,default=None)
    
class Usuario(models.Model):
  nombres = models.CharField(max_length=200)
  apellido1 = models.CharField(max_length=200)
  apellido2 = models.CharField(max_length=200)
  numero_documento = models.CharField(max_length=200)
  correo = models.CharField(max_length=200, blank=True, null=True, default=None)
  nombre_institucion = models.CharField(max_length=200, blank=True,null=True, default=None)
  telefono_institucion = models.CharField(max_length=200, blank=True, null=True, default=None)
  ubicacion_institucion = models.CharField(max_length=200, blank=True,null=True, default=None)
  direccion_institucion = models.CharField(max_length=200, blank=True,null=True, default=None)
  correo_institucion = models.CharField(max_length=200, blank=True,null=True, default=None)
  NIT = models.CharField(max_length=200, blank=True, null=True,default=None)
  rol = models.ForeignKey(Rol,blank=False)
  redes = models.ManyToManyField(RedSocial, through='UsuarioRedes')

  

class UsuarioRedes(models.Model):    
    url = models.CharField(max_length=200)  
    usuario = models.ForeignKey(Usuario,blank=False)
    red_social = models.ForeignKey(RedSocial,blank=False)

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    nivel = models.IntegerField(default=0)
    categoria_padre = models.ForeignKey("self",null=True) 

class Tag(models.Model):
    tag = models.CharField(max_length=255, null=False)
    

class ProblemaSolucion(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    descripcion =models.TextField(null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
    tipo = models.CharField(max_length=1,choices=(('P','PROBLEMA'),('S','SOLUCION')),default='P',
                                                  null=False, blank=False)
    categorias = models.ManyToManyField(Categoria)
    tags = models.ManyToManyField(Tag)
    usuario = models.ForeignKey(Usuario,null=False)



class RespuestaProblemaSolucion(models.Model):
    titulo = models.CharField(max_length=200, null=True)
    descripcion =models.TextField(null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
    tipo = models.CharField(max_length=1,choices=(('P','PROBLEMA'),('S','SOLUCION')),default='P',
                                                  null=False, blank=False)
    usuario = models.ForeignKey(Usuario,null=False)





    