from plataforma.models import Rol
from plataforma.models import Usuario
from plataforma.serializers import RolSerializer
from plataforma.serializers import UsuarioSerializer
from rest_framework import generics


class RolListCreate(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    
class RolDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Rol.objects.all()
    serializer_class = RolSerializer    
    
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer        