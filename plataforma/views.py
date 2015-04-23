from plataforma.models import *
from plataforma.serializers import *
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.views import APIView
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

class RedSocialListCreate(generics.ListCreateAPIView):
    queryset = RedSocial.objects.all()
    serializer_class = RedSocialSerializer
    
class RedSocialDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = RedSocial.objects.all()
    serializer_class = RedSocialSerializer 
     

class UsuarioRedesList(APIView):

    def get(self, request, pk, format=None):
        usuarioredes = UsuarioRedes.objects.filter(usuario_id=pk)
        serializer = UsuarioRedesSerializer(usuarioredes, many=True)
        return Response(serializer.data)  

class UsuarioRedesListCreate(generics.ListCreateAPIView):
    queryset = UsuarioRedes.objects.all()
    serializer_class = UsuarioRedesSerializer 
    
class UsuarioRedesDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = UsuarioRedes.objects.all()
    serializer_class = UsuarioRedesSerializer    

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer   

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer     

class ProblemaSolucionListCreate(generics.ListCreateAPIView):
    queryset = ProblemaSolucion.objects.all()
    serializer_class = ProblemaSolucionSerializer 

class ProblemaSolucionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ProblemaSolucion.objects.all()
    serializer_class = ProblemaSolucionSerializer  


class RespuestaProblemaSolucionListCreate(generics.ListCreateAPIView):
    queryset = RespuestaProblemaSolucion.objects.all()
    serializer_class = RespuestaProblemaSolucionSerializer 

class RespuestaProblemaSolucionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = RespuestaProblemaSolucion.objects.all()
    serializer_class = RespuestaProblemaSolucionSerializer 


