from django.forms import widgets
from rest_framework import serializers
from plataforma.models import Usuario
from plataforma.models import Rol


class UsuarioSerializer(serializers.ModelSerializer):
   class Meta:
        model = Usuario

class RolSerializer(serializers.ModelSerializer):
   class Meta:
        model = Rol
        