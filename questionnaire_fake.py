from plataforma.models import *
import random

problemas = ProblemaSolucion.objects.all()
rol=2
for ps in problemas:
  cuestionario={}
  respuestas_todas=[]
    
  cuestionarios = CuestionarioRol.objects.filter(rol_id=rol)
  for cx in   cuestionarios:
    preguntas = CuestionarioPregunta.objects.filter(cuestionario_id=cx.cuestionario_id).order_by('orden')
    for c in preguntas:
        respuestas = OpcionesDeRespuesta.objects.filter(pregunta=c.pregunta_id)
        revisar=True;
        if len(c.dependencia_respuestas.all())>0:
         if any(x == c.dependencia_respuestas.all()[0] for x in respuestas_todas):
            revisar=True
         else:
            revisar=False   
        p = Pregunta.objects.get(pk=c.pregunta_id)  
        if revisar:
         if p.tipo_pregunta!='M': 

            r=random.choice(respuestas)
            cuestionario[p.id]=(r.id, r.valor)
            respuestas_todas.append(r)
         else:
            resp = []
            rand = random.randint(2,len(respuestas)+1)
            z = [r for r in respuestas]
            for i in range(1,rand):
                w=random.choice(z)
                resp.append(w)
                respuestas_todas.append(w)
                z.remove(w)
            valores=[(k.id,k.valor) for k in resp]
            cuestionario[p.id]=valores
          
  print ps.id
  ps.respuestas_cuestionario = cuestionario
  ps.save()

            



