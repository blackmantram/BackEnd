from plataforma.models import *
def to_python_object(cuestionarios):
        s = "{"  
        for cuestionario in cuestionarios:
          for pregunta in cuestionario['preguntas']:
              if  pregunta["pregunta"]["tipo_pregunta"]!='M':
                if pregunta["pregunta"]["dato"]!=0:
                 valor = [ x["valor"] for x in pregunta["pregunta"]["opciones"] if int(x["id"])==int(pregunta["pregunta"]["dato"]) ][0]
               #respuesta=ProblemaSolucionOpcionRespuestaSerializer(data={'opcion_respuesta': pregunta["pregunta"]["dato"], 'problema_solucion': ps.data["id"]})
                 #s = s + pregunta["pregunta"]["id"] + ": ("+  pregunta["pregunta"]["dato"] + ","+ str(valor)+")"
                 s = s + str(pregunta["pregunta"]["id"]) + ": ("+str(pregunta["pregunta"]["dato"])+ ","+ str(valor)+") , "
              else:  
                s = s + str(pregunta["pregunta"]["id"]) + ": "
                w = "["
                for opcion in pregunta["pregunta"]["opciones"]:
                  if opcion['dato']:
                    w=w+ "(" +  str(opcion["id"]) + "," + str(opcion["valor"])+") , "
                
                w=w[:len(w)-2]
                w=w+"],"

                s=s + w
        s=s[:len(s)-1]
        s = s+"}"
        return s

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

def similitud(o1, o2,preguntas_similitud):
    s=0;
    n=0;
    for pregunta in o1:
      funcion_similitud=preguntas_similitud[pregunta]["similitud"]
      pregunta_B = preguntas_similitud[pregunta]["pregunta_B"]
      if pregunta_B in o2:
        s = s + funcion_similitud(o1[pregunta],o2[pregunta_B])
        n=n+1;
    return s/n;


def s1(x, y):
  return 100*len(list(set(x)&set(y)))/len(x)

def s2(x,y):
  return (1-abs(x[1]-y[1])/4.0)*100
   

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
        respuestas.append(respuesta)
       else:
        texto_respuesta_A=OpcionesDeRespuesta.objects.get(pk=o1[pregunta][0][0]).respuesta
        respuesta={"respuesta1":texto_respuesta_A,"respuesta2":"", "afinidad": 0 }

      preguntas_respuestas.append({"cuestionario":texto_cuestionario,"pregunta":texto_pregunta,"respuestas":respuestas})
  
    return preguntas_respuestas





   




