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
        cuestionarios = request.data['cuestionarios']
        id_usuario = request.data['id_usuario']
        respuestas = to_python_object(cuestionarios)
        tipo = request.data['tipo']
        problema_solucion={'titulo':'perfil','descripcion':'perfil','tipo': tipo,'usuario': id_usuario, 'respuestas_cuestionario': respuestas,'categorias':[], 'tags':[] }
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
       num_registros=10;
       # z='  '       
       # busqueda = json.loads(z)
       busqueda = json.loads(self.request.QUERY_PARAMS.get("cuestionario", None))
       cuestionarios_json = busqueda["cuestionarios"];
       if(busqueda["tipo"]=="P"):
         tipo = "S"
       else:
         tipo = "P"   


       pagina = int(self.request.QUERY_PARAMS.get('pagina', None))
       cuestionario = eval(to_python_object(cuestionarios_json))
       similitudes = []
       preguntas={}

       
       for preg in cuestionario:
         p=PreguntasSimilitud.objects.get(pregunta_A=preg)
         if p.funcion.funcion=='s1':
           funcion=s1
         if p.funcion.funcion=='s2':
           funcion=s2  
         preguntas[preg]={'pregunta_B': p.pregunta_B.id,'similitud': funcion}
       
       
       problemas_soluciones=ProblemaSolucion.objects.filter(tipo=tipo);
       for ps in problemas_soluciones:
         similitudes.append((ps.id,similitud(cuestionario,eval(ps.respuestas_cuestionario),preguntas)))
      
       total = len(ProblemaSolucion.objects.filter(tipo=tipo))
       min_registro = (pagina-1)*num_registros
       max_registro =  pagina*num_registros


       so = sorted(similitudes, key=lambda d: d[1], reverse=True)[min_registro:max_registro]
       ids = [id[0] for id in so]
        
       
       problemas_soluciones=ProblemaSolucion.objects.filter(id__in=ids).values()
       ps=[]
       for i in range(0,len(so)):
          usuario = Usuario.objects.filter(pk=problemas_soluciones[i]["usuario_id"]).values()[0]
          nivel_afinidad = so[i]
          ps.append({"problema_solucion": problemas_soluciones[i], "usuario":usuario, "nivel_afinidad": nivel_afinidad[1] })
       respuesta = {"problemas_soluciones": ps, "total":total}
       return Response(respuesta)

    def detail(self,request):
      busqueda = json.loads(self.request.QUERY_PARAMS.get("cuestionario", None))
      cuestionarios_json = busqueda["cuestionarios"];
      id_ps = int(self.request.QUERY_PARAMS.get('id_ps', None))
      cuestionario = eval(to_python_object(cuestionarios_json))
      similitudes = []
      preguntas={}
      
       
      for preg in cuestionario:
         p=PreguntasSimilitud.objects.get(pregunta_A=preg)
         if p.funcion.funcion=='s1':
           funcion=s1
         if p.funcion.funcion=='s2':
           funcion=s2  
         preguntas[preg]={'pregunta_B': p.pregunta_B.id,'similitud': funcion}
      
      ps = problemas_soluciones=ProblemaSolucion.objects.get(pk=id_ps);
      print cuestionario 
      print preguntas
      respuesta={"respuesta":similitud_detalle(cuestionario,eval(ps.respuestas_cuestionario),preguntas)}
      
      return Response(respuesta)
      






