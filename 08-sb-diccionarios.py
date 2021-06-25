miDiccionario={"Ecuador":"Quito","Colombia":"Bogotá","Perú":"Lima","Brasil":"Brasilia"}
print(miDiccionario["Ecuador"])
print(miDiccionario)

miDiccionario["Venezuela"]="Mexico"         #Erroneo para kodificar
print(miDiccionario)

miDiccionario["Venezuela"]="Caracas"        # Valor corregido, sobreescribir
print(miDiccionario)

del miDiccionario["Perú"]                   # Elminar un clave:valor
print(miDiccionario)

miTupla=(1,2,3)
miDiccionario2={miTupla[0]:"Ecuador",miTupla[1]:"Colombia",miTupla[2]:"Perú"}
print(miDiccionario2)
print(miDiccionario2[2])

miDiccionario3={10:"Cris",20:"Cami",30:"Naty",40:"Madre",50:"Padre",60:["Heriberto","Carlos","Hernesto"]}
miDiccionario3["SubDic"]=miDiccionario2     # Agrega otro diccionario al diccionario3

print(miDiccionario3)

print(miDiccionario3.keys())                #Imprime claves
print(miDiccionario3.values())              # Imprime valores
print(len(miDiccionario3))                  # Imprime longitud del diccionario