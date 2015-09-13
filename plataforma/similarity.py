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

#{1: (4,1) , 2: [(3,3) , (2,2) ],3: (6,1) }
def similitud(o1, o2):
    funciones = {1: s2, 2: s1, 3: s2}
    s=0;
    n=0;
    for pregunta in o1:
      s = s + funciones[pregunta](o1[pregunta],o2[pregunta])
      n=n+1;
    return s/n;


def s1(x, y):
  return len(list(set(x)&set(y)))/len(x)

def s2(x,y):
  return 1-abs(x[1]-y[1])/4







   




