from django.forms import widgets
from rest_framework import serializers
from plataforma import models
from plataforma.models import Usuario
from plataforma.models import Rol
from plataforma.models import UsuarioRedes
from plataforma.models import RedSocial
from plataforma.models import Categoria
from plataforma.models import ProblemaSolucion
from plataforma.models import RespuestaProblemaSolucion
from plataforma.models import Tag
from plataforma.models import Cuestionario
from plataforma.models import CuestionarioPregunta
from plataforma.models import Pregunta
from plataforma.models import OpcionesDeRespuesta
from plataforma.models import CuestionarioRol
from plataforma.models import ProblemaSolucionOpcionRespuesta

class RedSocialSerializer(serializers.ModelSerializer):  
        class Meta:
            model = RedSocial      

class UsuarioRedesSerializer(serializers.ModelSerializer):
        class Meta:
            model = UsuarioRedes

class RolSerializer(serializers.ModelSerializer):
   class Meta:
        model = Rol       


                    
class UsuarioSerializer(serializers.ModelSerializer):
   tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag', required=False)
    
   def to_internal_value(self, data):
      if data.get("tags") is not None:   # si existen tags
        self.check_for_new_tags(data.get("tags")) #entonces revisa cuales tags son nuevos
      return super(UsuarioSerializer,self).to_internal_value(data)

   def check_for_new_tags(self,tags): # Crea en la base aquellos tags que no existan 
      for tag in tags:
        try:
             tag_object = Tag.objects.get(tag=tag)
        except:
             tag_object = Tag.objects.create(tag=tag)   
   class Meta:
        model = Usuario

class CategoriaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Categoria

class ProblemaSolucionSerializer(serializers.Serializer):
  
  id = serializers.IntegerField(read_only=True)                                             
  titulo = serializers.CharField(max_length=200)
  descripcion =serializers.CharField()
  fecha = serializers.DateTimeField(required=False, allow_null=True)
  tipo = serializers.ChoiceField([('P','PROBLEMA'),('S','SOLUCION')])

  tags = serializers.SlugRelatedField(many=True,queryset=Tag.objects.all(),slug_field='tag',required=False)
  usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
  categorias = serializers.PrimaryKeyRelatedField(many=True, queryset=Categoria.objects.all())
  categorias_completas = CategoriaSerializer(many=True,read_only=True, source="categorias")

  def to_internal_value(self, data):
        if data.get("tags") is not None:   # si existen tags
          self.check_for_new_tags(data.get("tags")) #entonces revisa cuales tags son nuevos
        return super(ProblemaSolucionSerializer,self).to_internal_value(data)

  def create(self, validated_data):  
      instance=ProblemaSolucion.objects.create(titulo=validated_data["titulo"],
        descripcion=validated_data["descripcion"],
        tipo=validated_data["tipo"],
        usuario=validated_data["usuario"]
        );
      instance.categorias = validated_data["categorias"]
      instance.tags = validated_data["tags"]
      instance.save()
      return instance

  def update(self, instance, validated_data):
      instance.titulo = validated_data.get('titulo', instance.titulo)
      instance.descripcion = validated_data.get('descripcion', instance.descripcion)
      instance.fecha = validated_data.get('fecha', instance.fecha)
      instance.tipo = validated_data.get('tipo', instance.tipo) 
      instance.categorias = validated_data.get('categorias', instance.categorias)
      instance.tags = validated_data.get('tags', instance.tags)
      instance.usuario = validated_data.get('usuario', instance.usuario)
      instance.save()
      return instance

  def check_for_new_tags(self,tags): # Crea en la base aquellos tags que no existan
    if tags is not None:
      for tag in tags:
        
        try:
             tag_object = Tag.objects.get(tag=tag)
        except:
             tag_object = Tag.objects.create(tag=tag)
         
 
class RespuestaProblemaSolucionSerializer(serializers.ModelSerializer):
   class Meta:
        model = RespuestaProblemaSolucion

class TagSerializer(serializers.ModelSerializer):
   class Meta:
        model = Tag

class OpcionesDeRespuestaSerializer(serializers.ModelSerializer,serializers.Serializer):
  class Meta:
        model = OpcionesDeRespuesta
        


class PreguntaSerializer(serializers.ModelSerializer):
   opciones = OpcionesDeRespuestaSerializer(many=True,read_only=True) 
   class Meta:
        model = Pregunta
        

class CuestionarioPreguntaSerializer(serializers.ModelSerializer):
  pregunta = PreguntaSerializer()
  class Meta:
    model = CuestionarioPregunta

  

class CuestionarioSerializer(serializers.ModelSerializer): 
   preguntas = CuestionarioPreguntaSerializer(source='cuestionariopregunta_set', many=True)  
   class Meta:
        model = Cuestionario      
        depth=4     

class CuestionarioRolSerializer(serializers.ModelSerializer):
  cuestionario = CuestionarioSerializer()
  class Meta:
    model = CuestionarioRol

class ProblemaSolucionOpcionRespuestaSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProblemaSolucionOpcionRespuesta    


