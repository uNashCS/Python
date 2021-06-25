miTupla=(1,2,3,4,5,6,"Cris")            # Recomendado usar paréntesis
miTupla2=1,2,3,4,5,6,"Cris"             # Empaquetado de tupla
miListTuple=list(miTupla)
print(miTupla[:])
print(miListTuple)
miTuplaList=tuple(miListTuple)
print(miTuplaList)

print("Cris" in miTuplaList)
print(miTuplaList.count(1))

miTupla3=("Cris",20,12,1995)
nombre,dia,mes,anio=miTupla3            # Por orden asigan los elementos de la tupla a las variables
print(nombre)                           # Desempaquetado de tupla
print(dia)
print(mes)
print(anio)