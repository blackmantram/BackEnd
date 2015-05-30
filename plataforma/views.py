from plataforma.models import *
from plataforma.serializers import *
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets

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
    def get_queryset(self):
        queryset = super(ProblemaSolucionListCreate, self).get_queryset()
        
        token = self.request.QUERY_PARAMS.get('token', None)

        if self.kwargs.get('usuario') is not None:
          return queryset.filter(usuario=self.kwargs.get('usuario'))
        
        if token is not None:
          return queryset.filter(titulo__icontains=token)
          

        return queryset.filter()

class Sugerencias(viewsets.ViewSet):
    def list_sugerencias(self,request,token=None):

      token = self.request.QUERY_PARAMS.get('token', None)

      n_espacios = token.count(' ');
      resultados = ProblemaSolucion.objects.filter(titulo__icontains=token); 
  
      sugerencias=[]
      for resultado in resultados:
           posicion = resultado.titulo.upper().find(token.upper());
           if posicion>0:
            posicion = resultado.titulo.upper().find(token.upper());
           s=resultado.titulo
           if posicion==0 or not(resultado.titulo[posicion-1].isalpha()): 
              pos_espacios=[i for i, letter in enumerate(resultado.titulo[posicion:]) if letter == ' ']
              if pos_espacios:
                 if n_espacios==0:
                   if resultado.titulo[posicion+len(token)]==' ':
                     if len(pos_espacios)>1:
                       palabra = resultado.titulo[posicion:posicion+pos_espacios[1]]
                       
                     else:
                       palabra = resultado.titulo[posicion:]
                       
                   else: 
                     palabra = resultado.titulo[posicion:posicion+pos_espacios[0]]
                 else:
                   if n_espacios+1<len(pos_espacios): 
                     palabra = resultado.titulo[posicion:posicion+pos_espacios[n_espacios+1]]
                   else:
                     palabra = resultado.titulo[posicion:]
              else:
                palabra = resultado.titulo[posicion:]  

              try: 
                sugerencias.index(palabra)
                
              except ValueError:
                sugerencias.append(palabra)
                

      return Response(sugerencias[1:6]) 
          

        

class ProblemaSolucionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ProblemaSolucion.objects.all()
    serializer_class = ProblemaSolucionSerializer  


class RespuestaProblemaSolucionListCreate(generics.ListCreateAPIView):
    queryset = RespuestaProblemaSolucion.objects.all()
    serializer_class = RespuestaProblemaSolucionSerializer 

class RespuestaProblemaSolucionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = RespuestaProblemaSolucion.objects.all()
    serializer_class = RespuestaProblemaSolucionSerializer 


