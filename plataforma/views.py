# coding=utf-8 

from plataforma.models import *
from rest_framework import status
from plataforma.serializers import *
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token


from plataforma.similarity import *
from plataforma.emails import *
from django.db.models import Q
import json
from plataforma.models import PreguntasSimilitud
import logging 

class BusquedaCreateRetrieve(viewsets.ViewSet):
    def get(self,request,pk):
      ps = ProblemaSolucion.objects.get(pk=pk)
      cs = Cuestionario.objects.all().filter(rol=ps.usuario.rol,cuestionariorol__tipo=ps.tipo)
      c = CuestionarioSerializer(cs,many=True)
      respuestas=ps.respuestas_cuestionario
      cuestionario = python_object_to_cuestionario(respuestas,c.data)
      ps_serial = ProblemaSolucionSerializer(ps)
      soluciones = RespuestaProblemaSolucion.objects.filter(busqueda_id=pk)
      soluciones_id=[x.respuesta_id for x in soluciones]
      respuesta = ps_serial.data
      respuesta["cuestionario"]= cuestionario
      respuestas_asociadas=[]
      ps_afinidades= cuestionario_afinidad(cuestionario,ProblemaSolucion.objects.filter(pk__in=soluciones_id),1,10)
      i=0
      for solucion in soluciones:
        obj = {"id_busqueda_respuesta": solucion.id}
        if solucion.respuesta is None:
          obj["activo"]=0
          ps={"problema_solucion": {"titulo":solucion.titulo,"descripcion":solucion.descripcion,"fecha":solucion.fecha,"tipo":solucion.tipo}}
        else:
          obj["activo"]=1
          ps=ps_afinidades["problemas_soluciones"][i]
          i=i+1
        obj.update(ps)  
        respuestas_asociadas.append(obj)

      respuesta["respuestas_asociadas"]= respuestas_asociadas
      return Response(respuesta)
    def create(self,request):

      return Response("ok")
      



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
   # permission_classes = (IsAuthenticated,)

    def create(self, request):
      if 'password' not in request.data:
        password=''
      else: 
        password=request.data['password']    
      if 'correo' not in request.data:
        correo=''
      else:
        correo=request.data['correo']   
      if password=='' or correo=='':
         return Response({'error':'los campos correo y password requeridos'},
                              status=status.HTTP_400_BAD_REQUEST)
             
        
      user = UserSerializer(data={'username':correo,'email':correo,'password': password})
      usuario = UsuarioSerializer(data=request.data)
      if user.is_valid():
        if usuario.is_valid(): 
         correo =correo
         nombre = request.data['nombres']+' '+request.data['apellido1']+' '+request.data['apellido2'] 
         user=user.save()
         user.set_password(password);
         user.save()
         token, created = Token.objects.get_or_create(user=user)
         usuario=usuario.save()
         usuario.user = user
         usuario.save()         
         enviar_correo(correo, {"usuario":nombre.upper()})
        else:
         return Response(usuario.errors,
                              status=status.HTTP_400_BAD_REQUEST)  
      else:
        return Response(user.errors,
                              status=status.HTTP_400_BAD_REQUEST)

      return Response({'key': token.key}, status=status.HTTP_201_CREATED)

    
    
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer  
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return Usuario.objects.get(user_id=self.request.user.id)



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

class RespuestaProblemaSolucionCreate(generics.CreateAPIView):
    queryset = RespuestaProblemaSolucion.objects.all()
    serializer_class = RespuestaProblemaSolucionSerializer 
    

class RespuestaProblemaSolucionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RespuestaProblemaSolucion.objects.all()
    serializer_class = RespuestaProblemaSolucionSerializer

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
    def post(self, request, *args, **kwargs):
       #print request.stream.body
       if "cuestionario" in request.data:
         request.data["respuestas_cuestionario"]=eval(to_python_object(request.data["cuestionario"]))
         #return Response("ok")
       return super(ProblemaSolucionListCreate, self).post(request, *args, **kwargs)
     
        

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
       busqueda = request.data["cuestionario"]
       cuestionarios_json = busqueda["cuestionarios"];
       if(busqueda["tipo"]=="P"):
         tipo = 'S'
       else:
         tipo = 'P'   

       problemas_soluciones=ProblemaSolucion.objects.filter(tipo=tipo);
       pagina = int(request.data["pagina"])

       respuesta=cuestionario_afinidad(cuestionarios_json,problemas_soluciones,pagina,num_registros)
       # dependencias=get_dependencias(cuestionarios_json)
       # cuestionario = eval(to_python_object(cuestionarios_json))
       # similitudes = []
       # preguntas={}
 
       # for preg in cuestionario:
       #   p=PreguntasSimilitud.objects.get(pregunta_A=preg)
       #   funcion =  eval(p.funcion.funcion) 
       #   preguntas[preg]={'pregunta_B': p.pregunta_B.id,'similitud': funcion}
       
       
       
       # for ps in problemas_soluciones:
       #   similitudes.append((ps.id,similitud(cuestionario,eval(ps.respuestas_cuestionario),preguntas,dependencias)))
      
       # total = len(ProblemaSolucion.objects.filter(tipo=tipo))
       # min_registro = (pagina-1)*num_registros
       # max_registro =  pagina*num_registros
       # so = sorted(similitudes, key=lambda d: d[1], reverse=True)[min_registro:max_registro]
       # ids = [id[0] for id in so]
        
       # ps=[]
       # for i in range(0,len(so)):
       #    problema_solucion=ProblemaSolucion.objects.filter(id=ids[i]).values()[0]
       #    usuario = Usuario.objects.filter(pk=problema_solucion["usuario_id"]).values()[0]
       #    nivel_afinidad = so[i]
       #    ps.append({"problema_solucion": problema_solucion, "usuario":usuario, "nivel_afinidad": nivel_afinidad[1] })
       # respuesta = {"problemas_soluciones": ps, "total":total}
       return Response(respuesta)

    def detail(self,request):
      busqueda = request.data["cuestionario"]
      cuestionarios_json = busqueda["cuestionarios"];
      id_ps = int(request.data['id_ps'])
      cuestionario = eval(to_python_object(cuestionarios_json))
      similitudes = []
      preguntas={}
      
       
      for preg in cuestionario:
         p=PreguntasSimilitud.objects.get(pregunta_A=preg)
         funcion =  eval(p.funcion.funcion) 
         preguntas[preg]={'pregunta_B': p.pregunta_B.id,'similitud': funcion}
      
      ps = problemas_soluciones=ProblemaSolucion.objects.get(pk=id_ps);
      respuesta={"respuesta":similitud_detalle(cuestionario,eval(ps.respuestas_cuestionario),preguntas)}
      
      return Response(respuesta)
      


class ConversacionView(viewsets.ViewSet):
    def get_conversation(self,request):
       
      busqueda_id = self.request.QUERY_PARAMS.get('busqueda_id', None)
      respuesta_id = self.request.QUERY_PARAMS.get('respuesta_id', None)
      if busqueda_id==None or respuesta_id==None:
       return Response({'error':'enviar las variables busqueda_id y respuesta_id en la url'},
                              status=status.HTTP_400_BAD_REQUEST)

      conversacion=Conversacion.objects.filter(busqueda_id=busqueda_id,respuesta_id=respuesta_id)
      if len(conversacion)==0:
       conversacion=None 
       try:
        conversacion=Conversacion.objects.create(busqueda_id=busqueda_id,respuesta_id=respuesta_id)
       except:
        return Response({'error':'busqueda_id o respuesta_id inválidas'},
                              status=status.HTTP_400_BAD_REQUEST)
          
      else:
        conversacion=conversacion[0]

      conversacion_serializer = ConversacionMensajesSerializer(conversacion)
      return Response(conversacion_serializer.data)  

    def get_conversation_pk(self,request,pk):
      conversacion=Conversacion.objects.get(pk=pk)
      conversacion_serializer = ConversacionMensajesSerializer(conversacion)
      return Response(conversacion_serializer.data)  

    def message_read(self,request,pk):
     try:
      mensaje=Mensaje.objects.get(pk=pk)
      mensaje.visto=True
      mensaje.save()
      return Response("ok")
     except:
        return Response({'error':'id no válido'},
                              status=status.HTTP_400_BAD_REQUEST)
      


    
    def list(self,request,usuario):
      conversaciones = Conversacion.objects.filter(Q(busqueda__usuario_id=usuario)|Q(busqueda__usuario_id=usuario))
      cs = ConversacionSerializer(conversaciones,many=True)
      cs = cs.data
      i=0
      for conversacion in cs:
        conversacion["mensajes_sin_leer"]=len(conversaciones[i].mensajes.filter(visto=0,destinatario=usuario))
        i=i+1
      return Response(cs)

    def create_message(self,request):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        

