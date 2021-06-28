print("Programa de evaluación de notas de alumnos")
nota_alumno=input("Introduce nota: ")                       # input lee lo que introduzcamos como Str

def evaluacion(nota):
    valoracion="Aprobado"
    if(nota<5):                                             # Ámbito de una variable - no es alcazable fuera del ámbito
        valoracion="Suspenso"
    return valoracion                                       # Devuelve el valor

print(evaluacion(int(nota_alumno)))                         #int() para convertir en número lo introducido

