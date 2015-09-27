from plataforma.models import *
from plataforma.serializers import *
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
import logging

class RolListCreate(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    
class RolDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Rol.objects.all()
    serializer_class = RolSerializer  

class RolCuestionariosRetrieve(generics.ListAPIView):

    queryset = Cuestionario.objects.all()
    serializer_class = CuestionarioSerializer  

    def get_queryset(self):
        queryset = super(RolCuestionariosRetrieve, self).get_queryset()
        tipo = self.request.QUERY_PARAMS.get('tipo', None)

        if tipo is None:
           return queryset.filter(rol=self.kwargs.get('pk'))
 
        return queryset.filter(rol=self.kwargs.get('pk'),cuestionariorol__tipo=tipo)

class RolCuestionariosSave(viewsets.ViewSet):

    def create(self, request):
        cuestionarios = request.data['cuestionarios']
        id_usuario = request.data['id_usuario']
        s = "{"
        
          # try: 
        for cuestionario in cuestionarios:
          for pregunta in cuestionario['preguntas']:
              if  pregunta["pregunta"]["tipo_pregunta"]!='M':
                if pregunta["pregunta"]["dato"]!=0:
                 valor = [ x["valor"] for x in pregunta["pregunta"]["opciones"] if int(x["id"])==int(pregunta["pregunta"]["dato"]) ][0]
               #respuesta=ProblemaSolucionOpcionRespuestaSerializer(data={'opcion_respuesta': pregunta["pregunta"]["dato"], 'problema_solucion': ps.data["id"]})
                 #s = s + pregunta["pregunta"]["id"] + ": ("+  pregunta["pregunta"]["dato"] + ","+ str(valor)+")"
                 s = s + str(pregunta["pregunta"]["id"]) + ": ("+pregunta["pregunta"]["dato"]+ ","+ str(valor)+") , "
              else:  
                s = s + str(pregunta["pregunta"]["id"]) + ": "
                w = "["
                for opcion in pregunta["pregunta"]["opciones"]:
                  if opcion['dato']:
                    w=w+ "(" +  str(opcion["id"]) + "," + str(opcion["valor"])+") , "
                
                w=w[:len(w)-2]
                w=w+"],"

                s=s + w
        #            #respuesta=ProblemaSolucionOpcionRespuestaSerializer(data={'opcion_respuesta': opcion["id"], 'problema_solucion': ps.data["id"]})
                   
        #     #if respuesta.is_valid():
        #      # respuesta.save()
        # except ValueError:
        #   return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)          
        s=s[:len(s)-1]
        s = s+"}"
        problema_solucion={'titulo':'perfil','descripcion':'perfil','tipo': 'P','usuario': id_usuario, 'respuestas_cuestionario': s,'categorias':[], 'tags':[] }
        ps = ProblemaSolucionSerializer(data=problema_solucion)
        ps.is_valid()
        ps.save()
        return Response({'status': 'cuestionario guardado'})      
    

    
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
    def get_queryset(self):
        queryset = super(CategoriaListCreate, self).get_queryset()
        
        nivel = self.request.QUERY_PARAMS.get('nivel', None)
        padre = self.request.QUERY_PARAMS.get('categoria_padre', None)
      
        if nivel is not None:
          if padre is not None:
            return queryset.filter(nivel=nivel,categoria_padre_id=padre)            
          else:
            return queryset.filter(nivel=nivel)
         

          

        return queryset.filter()  

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
                

      return Response(sugerencias[0:5]) 
          
    def list_sugerencias_tags(self,request,token=None):

      token = self.request.QUERY_PARAMS.get('token', None)

      n_espacios = token.count(' ');
      resultados = Tag.objects.filter(tag__icontains=token); 
      
      
  
      sugerencias=[]
      for resultado in resultados:
           posicion = resultado.tag.upper().find(token.upper());
           if posicion>0:
            posicion = resultado.tag.upper().find(token.upper());
           s=resultado.tag
           if posicion==0 or not(resultado.tag[posicion-1].isalpha()): 
              pos_espacios=[i for i, letter in enumerate(resultado.tag[posicion:]) if letter == ' ']
              if pos_espacios:
                 if n_espacios==0:
                   if resultado.tag[posicion+len(token)]==' ':
                     if len(pos_espacios)>1:
                       palabra = resultado.tag[posicion:posicion+pos_espacios[1]]                    
                     else:
                       palabra = resultado.tag[posicion:] 
                       
                   else: 
                     palabra = resultado.tag[posicion:posicion+pos_espacios[0]]

                 else:
                   if n_espacios+1<len(pos_espacios): 
                     palabra = resultado.tag[posicion:posicion+pos_espacios[n_espacios+1]]
                   else:
                     palabra = resultado.tag[posicion:]
              else:
                palabra = resultado.tag[posicion:]  


              try: 
                sugerencias.index(palabra)
                
              except ValueError:
                sugerencias.append(palabra)
                

      return Response(sugerencias[0:5]) 

        

class ProblemaSolucionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ProblemaSolucion.objects.all()
    serializer_class = ProblemaSolucionSerializer  


class RespuestaProblemaSolucionListCreate(generics.ListCreateAPIView):
    queryset = RespuestaProblemaSolucion.objects.all()
    serializer_class = RespuestaProblemaSolucionSerializer 

class RespuestaProblemaSolucionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = RespuestaProblemaSolucion.objects.all()
    serializer_class = RespuestaProblemaSolucionSerializer 

class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer 

class TagDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer 


class CuestionarioRetrieve(generics.RetrieveAPIView):
    queryset = Cuestionario.objects.all()
    serializer_class = CuestionarioSerializer      


class CuestionarioList(generics.ListAPIView):
    queryset = Cuestionario.objects.all()
    serializer_class = CuestionarioSerializer 



