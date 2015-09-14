# coding=utf-8 

from plataforma.models import *
from plataforma.serializers import *
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from plataforma.similarity import *
import json
from plataforma.models import PreguntasSimilitud
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
        print request.data
        cuestionarios = request.data['cuestionarios']
        id_usuario = request.data['id_usuario']
       # print cuestionarios
        respuestas = to_python_object(cuestionarios)
        print eval(respuestas)
        print respuestas
        tipo = request.data['tipo']
        problema_solucion={'titulo':'perfil','descripcion':'perfil','tipo': tipo,'usuario': id_usuario, 'respuestas_cuestionario': respuestas,'categorias':[], 'tags':[] }
        print problema_solucion
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

class AfinidadList(viewsets.ViewSet):
    def list(self,request):
       #print self.request.QUERY_PARAMS.get('cuestionario', None)
       #busqueda = json.loads(self.request.QUERY_PARAMS.get('cuestionario', None))
       
       z='{"cuestionarios":[{"id":1,"preguntas":[{"id":5,"pregunta":{"id":1,"opciones":[{"id":5,"respuesta":"Software","orden":1,"valor":2,"pregunta":1,"dato":false},{"id":4,"respuesta":"Redes Sociales","orden":2,"valor":1,"pregunta":1,"dato":false}],"enunciado":"¿Qué necesitas?","imagen":null,"tipo_pregunta":"U","dato":"4"},"orden":1,"cuestionario":1,"dependencia_respuestas":[],"enable":true},{"id":6,"pregunta":{"id":2,"opciones":[{"id":3,"respuesta":"Instagram","orden":1,"valor":3,"pregunta":2,"dato":true},{"id":1,"respuesta":"Facebook","orden":2,"valor":1,"pregunta":2,"dato":true},{"id":2,"respuesta":"Twitter","orden":3,"valor":2,"pregunta":2,"dato":true}],"enunciado":"¿Qué redes sociales necesitas?","imagen":null,"tipo_pregunta":"M","dato":0},"orden":2,"cuestionario":1,"dependencia_respuestas":[],"enable":true}],"titulo":"¿Qué buscas?","descripcion":null,"imagen":"boton-que.png","fecha":null,"enable":true},{"id":2,"preguntas":[{"id":7,"pregunta":{"id":3,"opciones":[{"id":6,"respuesta":"menos de $500.000","orden":1,"valor":1,"pregunta":3,"dato":false},{"id":7,"respuesta":"Entre $500.000 a $1.0000","orden":2,"valor":2,"pregunta":3,"dato":false},{"id":8,"respuesta":"Entre $1.000.000 y $5.000.000","orden":3,"valor":3,"pregunta":3,"dato":false},{"id":9,"respuesta":"Más de $5.000.000","orden":4,"valor":4,"pregunta":3,"dato":false}],"enunciado":"¿Cuál es tu presupuesto?","imagen":null,"tipo_pregunta":"U","dato":"6"},"orden":0,"cuestionario":2,"dependencia_respuestas":[],"enable":true}],"titulo":"¿Cuál es tu presupuesto?","descripcion":null,"imagen":"boton-cuanto.png","fecha":null,"enable":true},{"id":3,"preguntas":[{"id":8,"pregunta":{"id":4,"opciones":[{"id":10,"respuesta":"Chía","orden":1,"valor":1,"pregunta":4,"dato":false},{"id":11,"respuesta":"Girardot","orden":2,"valor":2,"pregunta":4,"dato":false},{"id":12,"respuesta":"Mosquera","orden":3,"valor":3,"pregunta":4,"dato":false}],"enunciado":"¿Dónde estás Ubicado?","imagen":null,"tipo_pregunta":"L","dato":"12"},"orden":0,"cuestionario":3,"dependencia_respuestas":[],"enable":true}],"titulo":"¿Dónde te encuentras?","descripcion":null,"imagen":"boton-donde.png","fecha":null,"enable":true}],"tipo":"P"}'       
       busqueda = json.loads(z)
       cuestionarios_json = busqueda["cuestionarios"];
       tipo = busqueda["tipo"];
       #pagina = self.request.QUERY_PARAMS.get('pagina', None)
       cuestionario = eval(to_python_object(cuestionarios_json))
       print cuestionario
       similitudes = []
       preguntas={}
       
       for preg in cuestionario:
         p=PreguntasSimilitud.objects.get(pregunta_A=preg)
         print p.funcion.funcion
         if p.funcion.funcion=='s1':
           funcion=s1
         if p.funcion.funcion=='s2':
           funcion=s2  
         preguntas[preg]={'pregunta_B': p.pregunta_B.id,'similitud': funcion}
       
       
       problemas_soluciones=ProblemaSolucion.objects.all();
       for ps in problemas_soluciones:
         similitudes.append((ps.id,similitud(cuestionario,eval(ps.respuestas_cuestionario),preguntas)))
      
       so = sorted(similitudes, key=lambda d: d[1], reverse=True)[0:10]
       ids = [id[0] for id in so]
        
       total = len(ProblemaSolucion.objects.all())
       problemas_soluciones=ProblemaSolucion.objects.filter(id__in=ids).values()
       ps=[]
       for i in range(0,9):
          #usuario = Usuario.objects.get(pk=problemas_soluciones[i]["usuario_id"]).values()
          usuario = "xxx"
          nivel_afinidad = so[i]
          ps.append({"problema_solucion": problemas_soluciones[i], "usuario":usuario, "nivel_afinidad": nivel_afinidad[1] })
       respuesta = {"problemas_soluciones": ps, "total":total}
       return Response(respuesta)
       #return Response(problemas_soluciones) 






