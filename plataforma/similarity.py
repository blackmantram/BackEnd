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
   




