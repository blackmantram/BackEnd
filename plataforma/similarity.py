from plataforma.models import *
from math import *
def to_python_object(cuestionarios):
        s = "{"  
        for cuestionario in cuestionarios:
          for pregunta in cuestionario['preguntas']:
              if  pregunta["pregunta"]["tipo_pregunta"]!='M':
                if pregunta["pregunta"]["dato"]!=0:
                 valor = [ x["valor"] for x in pregunta["pregunta"]["opciones"] if int(x["id"])==int(pregunta["pregunta"]["dato"]) ][0]
                 s = s + str(pregunta["pregunta"]["id"]) + ": ("+str(pregunta["pregunta"]["dato"])+ ","+ str(valor)+") , "
              else:  
                w = "["
                for opcion in pregunta["pregunta"]["opciones"]:
                  if opcion['dato']:
                    w=w+ "(" +  str(opcion["id"]) + "," + str(opcion["valor"])+") , "
                # if len(w)==1:
                #  break
                w=w+"],"
                if len(w)>3:
                  s = s + str(pregunta["pregunta"]["id"]) + ": "
                  s=s + w
        s=s[:len(s)-1]
        s = s+"}"
        return s
def get_dependencias(cuestionarios):
  dependencias={}
  for cuestionario in cuestionarios:

    for pregunta in cuestionario['preguntas']:

      if len(pregunta["dependencia_respuestas"])>0:
        pregunta_id = pregunta["pregunta"]["id"];
        cp=CuestionarioPregunta.objects.filter(cuestionario_id=cuestionario["id"],pregunta_id=pregunta_id)
        dependencias[pregunta_id]=cp[0].dependencia_respuestas.all()[0].pregunta.id

  return dependencias      

def python_object_to_cuestionario(respuestas,cuestionarios):
   respuestas=eval(respuestas)
   for cuestionario in cuestionarios:
          for pregunta in cuestionario['preguntas']:
              pregunta_id = pregunta["pregunta"]["id"]
              if  pregunta["pregunta"]["tipo_pregunta"]!='M':
                pregunta_id = pregunta["pregunta"]["id"]
                if pregunta_id in respuestas:
                   pregunta["pregunta"]["dato"]=respuestas[pregunta_id][0]
                else:
                  pregunta["pregunta"]["dato"]=0
              else:
                print pregunta_id

                if pregunta_id in respuestas: 
                  # print pregunta 
                  # print pregunta["pregunta"]["tipo_pregunta"]
                  # break
                  opciones = [x[0] for x in respuestas[pregunta_id]]
                  for opcion in pregunta["pregunta"]["opciones"]:
                    if opcion['id'] in opciones:
                      opcion['dato']=1
                    else:
                       opcion['dato']=0
           
   return cuestionarios


def to_cuestionario(object_1, object_2):
        respuesta = {}
        for i in object_1:
          pregunta = Pregunta.objects.get(pk=i)
          if isinstance(object_1[i],list):
             s=""
             for j in object_1[i]:
               respuesta_1 = OpcionesDeRespuesta.objects.get(pk=j[0])
               s=s+respuesta_1.respuesta+" , "
          else:
             respuesta_1 = OpcionesDeRespuesta.objects.get(pk=object_1[i][0])   
             s = respuesta_1.respuesta
          respuesta[pregunta.enunciado]=s
        return respuesta    

def similitud(o1, o2,preguntas_similitud, dependencias):
    s=0;
    n=0;
    similitudes={}
    for pregunta in o1:
      funcion_similitud=preguntas_similitud[pregunta]["similitud"]
      pregunta_B = preguntas_similitud[pregunta]["pregunta_B"]
      if pregunta_B in o2:
        #s = s + funcion_similitud(o1[pregunta],o2[pregunta_B])
        similitudes[pregunta]=funcion_similitud(o1[pregunta],o2[pregunta_B])
      else:
        similitudes[pregunta]=0
    for p in similitudes:
      if p not in dependencias.values():
        n=n+1
        s=s+similitudes[p]
        
    if n==0:
      n=1
      
    return s/n;


def s1(x, y):
  return 100*len(list(set({k[1] for k in x})&set({k[1] for k in y})))/len(x)

def s2(x,y):
  return (1-abs(int(x[1])-int(y[1]))/4.0)*100

def s3(x,y):
  return 100*(x[1]==y[1])

# Distancia Geodesica
def s4(a,b):
  a=a[1]
  b=b[1]
  R=6372.795477598
  distancia_maxima=400;
  ar=(float(a[0])*pi/180,float(a[1])*pi/180) # se convierte a radianes
  br=(float(b[0])*pi/180,float(b[1])*pi/180)
  distancia = R*acos(sin(ar[0])*sin(br[0])+cos(ar[0])*cos(br[0])*cos(ar[1]-br[1]))

  return (1-distancia/distancia_maxima)*100   

def similitud_detalle(o1, o2,preguntas_similitud):
    s=0;
    n=0;
    preguntas_respuestas=[]
    for pregunta in o1:
      funcion_similitud=preguntas_similitud[pregunta]["similitud"]
      pregunta_B = preguntas_similitud[pregunta]["pregunta_B"]
      texto_cuestionario = CuestionarioPregunta.objects.get(pregunta=pregunta).cuestionario.titulo
      texto_pregunta = Pregunta.objects.get(pk=pregunta).enunciado
      respuestas=[]

      if isinstance(o1[pregunta],list):
         if not pregunta_B in o2:
          o2[pregunta_B]=[]  
         intersect = list(set([z[1] for z in o1[pregunta]]) &set([z[1] for z in o2[pregunta_B]] ))    
         for resp in o1[pregunta]: 
           texto_respuesta=OpcionesDeRespuesta.objects.get(pk=resp[0]).respuesta 
           if resp[1] in intersect:
             respuesta={"respuesta1":texto_respuesta,"respuesta2":texto_respuesta, "afinidad":100 }
           else:
             respuesta={"respuesta1":texto_respuesta,"respuesta2":"", "afinidad":0 } 
           
           respuestas.append(respuesta)
      else:
       if pregunta_B in o2:  
        texto_respuesta_A=OpcionesDeRespuesta.objects.get(pk=o1[pregunta][0]).respuesta

        texto_respuesta_B=OpcionesDeRespuesta.objects.get(pk=o2[pregunta_B][0]).respuesta             
        
        respuesta={"respuesta1":texto_respuesta_A,"respuesta2":texto_respuesta_B, 
        "afinidad":funcion_similitud(o1[pregunta],o2[pregunta_B]) }
       else:
        texto_respuesta_A=OpcionesDeRespuesta.objects.get(pk=o1[pregunta][0]).respuesta
        respuesta={"respuesta1":texto_respuesta_A,"respuesta2":"", "afinidad": 0 }
       respuestas.append(respuesta)

      preguntas_respuestas.append({"cuestionario":texto_cuestionario,"pregunta":texto_pregunta,"respuestas":respuestas})
  
    return preguntas_respuestas





   




