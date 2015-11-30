# -*- encoding: utf-8 -*-
from django.db import models
from django.conf.urls import url
from django.contrib.auth.models import User
## Modelo que representa el rol dentro del sistema (Empresario,Emprendedor, Programador...)
class Rol(models.Model):
  nombre = models.CharField(max_length=200)
  descripcion = models.CharField(max_length=200, blank=True, null=True)
  imagen = models.CharField(max_length=200, blank=True, null=True)
  cuestionarios = models.ManyToManyField('Cuestionario', through='CuestionarioRol')
  tipo_rol = models.CharField(max_length=2,choices=(('BC','Busca en comercio'),('BT','Turismo'),('O','Ofrece')),default='BC',null=False, blank=False)

## Modelo que representa una red social del usuario"  
class RedSocial(models.Model):
    nombre = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    icono = models.CharField(max_length=200, blank=True,default=None)

## Modelo para representar una palabra o frase como Tag 
class Tag(models.Model):
    tag = models.CharField(max_length=255, null=False)

## Modelo que contiene la información del usuario.        
class Usuario(models.Model):
  nombres = models.CharField(max_length=200)
  apellido1 = models.CharField(max_length=200)
  apellido2 = models.CharField(max_length=200,)
  numero_documento = models.CharField(max_length=200,blank=True, null=True, default=None)
  correo = models.CharField(max_length=200, blank=True, null=True, default=None,unique=True)
  nombre_institucion = models.CharField(max_length=200, blank=True,null=True, default=None)
  telefono_institucion = models.CharField(max_length=200, blank=True, null=True, default=None)
  ubicacion_institucion = models.CharField(max_length=200, blank=True,null=True, default=None)
  direccion_institucion = models.CharField(max_length=200, blank=True,null=True, default=None)
  correo_institucion = models.CharField(max_length=200, blank=True,null=True, default=None)
  NIT = models.CharField(max_length=200, blank=True, null=True,default=None)
  descripcion = models.TextField(null=True)
  municipio_id = models.IntegerField(null=False)
  rol = models.ForeignKey(Rol,blank=False)
  redes = models.ManyToManyField(RedSocial, through='UsuarioRedes')
  tags = tags = models.ManyToManyField(Tag)
  user = models.ForeignKey(User,null=True)

  
## Modelo que asocia las redes sociales de un usuario
class UsuarioRedes(models.Model):    
    url = models.CharField(max_length=200,blank=True, null=True, default=None) 
    usuario = models.ForeignKey(Usuario,blank=False)
    red_social = models.ForeignKey(RedSocial,blank=False)

## Modelo que representa la categoría a la cual puede pertenecer un problema.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    nivel = models.IntegerField(default=0)
    categoria_padre = models.ForeignKey("self",null=True) 

    
## Moldeo  que representa una búsqueda de un problema o solución creada por el usuario.

class ProblemaSolucion(models.Model):
    """Representa un Problema Solución"""
    titulo = models.CharField(max_length=200, null=False)
    descripcion =models.TextField(null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
    tipo = models.CharField(max_length=1,choices=(('P','PROBLEMA'),('S','SOLUCION')),default='P',
                                                  null=False, blank=False)
    categorias = models.ManyToManyField(Categoria)
    tags = models.ManyToManyField(Tag)
    usuario = models.ForeignKey(Usuario,null=False)
    respuestas_cuestionario = models.CharField(max_length=255, null=True)
    # respuestas_asociadas = models.ManyToManyField('ProblemaSolucion', through='RespuestaProblemaSolucion')
    # it determines tag matching with other problem_solution   
    def tags_match_with(self, otro_problema_solucion):
      return [ (tag, 1) if tag in  otro_problema_solucion.tags.all() else (tag,0) for tag in self.tags.all() ]


## Este modelo representa un resultado de una búsqueda o solución 

class RespuestaProblemaSolucion(models.Model):
    busqueda = models.ForeignKey(ProblemaSolucion,null=False,related_name='busqueda')
    respuesta= models.ForeignKey(ProblemaSolucion,null=True,related_name='respuesta')
    titulo = models.CharField(max_length=200, null=False)
    descripcion =models.TextField(null=True)
    fecha = models.DateTimeField(null=False,blank=False)
    tipo = models.CharField(max_length=1,choices=(('P','PROBLEMA'),('S','SOLUCION')),default='P',
                                                  null=False, blank=False)
  

## Este modelo representa la pregunta dentro del cuestionario que se le realiza a un usuario para
# caracterizar el problema o solución en el momento de plantear una búsqueda.
   
class Pregunta(models.Model):
  enunciado = models.CharField(max_length=200, null=True)
  imagen = models.CharField(max_length=200, blank=True, null=True)
  tipo_pregunta = models.CharField(max_length=1,choices=(('U','UNICA RESPUESTA'),
    ('M','MULTIPLE RESPUESTA'),('L','LISTA')),default='U',
                                                  null=False, blank=False)


## Modelo que representa un cuestionario , del cual pertenecen varias preguntas.

class Cuestionario(models.Model):
    titulo = models.CharField(max_length=200, null=True)
    descripcion =models.TextField(null=True)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
    preguntas = models.ManyToManyField(Pregunta, through='CuestionarioPregunta')


## Este modelo asocia cada rol con un cuestionario.

class CuestionarioRol(models.Model):
    orden = models.IntegerField()
    cuestionario = models.ForeignKey(Cuestionario)
    rol = models.ForeignKey(Rol)
    tipo = models.CharField(max_length=1,choices=(('P','PROBLEMA'),('S','SOLUCION')),default='P',
                                                  null=False, blank=False)
    class Meta:
      ordering = ['orden']


## Modelo que representa una posible respuesta para una pregunta.
class OpcionesDeRespuesta(models.Model):
  respuesta = models.CharField(max_length=200, null=True)
  orden = models.IntegerField()
  valor = models.CharField(max_length=200, null=True)
  pregunta = models.ForeignKey(Pregunta, null=False, related_name='opciones')
  class Meta:
    ordering = ['orden']


## Modelo que asocia una pregunta y un cuestionario.
class CuestionarioPregunta(models.Model):
  orden = models.IntegerField()
  pregunta = models.ForeignKey(Pregunta)
  cuestionario = models.ForeignKey(Cuestionario)
  dependencia_respuestas = models.ManyToManyField(OpcionesDeRespuesta)
  class Meta:
    ordering = ['orden']


## Modelo que asocia una respuesta con un problema. Actualmente no se está utilizando este modelo.
class ProblemaSolucionOpcionRespuesta(models.Model):
  opcion_respuesta = models.ForeignKey(OpcionesDeRespuesta,null=False)
  problema_solucion = models.ForeignKey(ProblemaSolucion,null=False)

## Modelo que contiene la información de una función de similitud.
class Similitud(models.Model):
  funcion = models.CharField(max_length=50, null=True)
  descripcion =models.TextField(null=True)
    
  
## Modelo que asocia una dos preguntas a través de una función de similitud. 
class PreguntasSimilitud(models.Model):
  pregunta_A = models.ForeignKey(Pregunta,null=False,related_name='pregunta_problema')
  pregunta_B = models.ForeignKey(Pregunta,null=False,related_name='pregunta_solucion')
  funcion = models.ForeignKey(Similitud,null=False)


## Modelo que representa la conversación entre 2 usuarios acerca de un problema solución.
class Conversacion(models.Model):
    busqueda = models.ForeignKey(ProblemaSolucion,null=False,related_name='busqueda_')
    respuesta= models.ForeignKey(ProblemaSolucion,null=True,related_name='respuesta_')
    
## Modelo que contiene la información de un mensaje enviado de un usuario a otro en una conversación.    
class Mensaje(models.Model):
    mensaje = models.TextField(null=True)
    fecha = models.DateTimeField(auto_now=True, null=False)
    usuario_busqueda = models.ForeignKey(Usuario,null=True,related_name='usuario_busqueda')
    usuario_respuesta = models.ForeignKey(Usuario,null=True,related_name='usuario_respuesta')
    destinatario = models.ForeignKey(Usuario,null=True,related_name='usuario_destinatario')
    visto = models.BooleanField(default=False)
    conversacion = models.ForeignKey(Conversacion,null=False,related_name="mensajes")

## Modelo que permite almacenar variables gloabales del sistema
class Variable(models.Model):
  variable = models.CharField(max_length=200, null=False)
  valor = models.IntegerField()
  descripcion = models.TextField(null=True)
  
 



  
   








    