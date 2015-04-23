from django.forms import widgets
from rest_framework import serializers
from plataforma.models import Usuario
from plataforma.models import Rol
from plataforma.models import UsuarioRedes
from plataforma.models import RedSocial
from plataforma.models import Categoria
from plataforma.models import ProblemaSolucion
from plataforma.models import RespuestaProblemaSolucion




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
   # rol = RolSerializer(read_only=True)
   class Meta:
        model = Usuario

class CategoriaSerializer(serializers.ModelSerializer):
   # rol = RolSerializer(read_only=True)
   class Meta:
        model = Categoria

class ProblemaSolucionSerializer(serializers.ModelSerializer):
   class Meta:
        model = ProblemaSolucion

class RespuestaProblemaSolucionSerializer(serializers.ModelSerializer):
   class Meta:
        model = RespuestaProblemaSolucion



       

        

