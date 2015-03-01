from django.forms import widgets
from rest_framework import serializers
from landing_page.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
   class Meta:
        model = Usuario
        fields = ('nombre', 'correo', 'turismo', 'comercio', 'turista')