# Listas
misNumeros=[1,2,3,4,5,6,7,8,9]
misNombres=["Juan","Pepe","Cris","Naty"]

print(misNombres[:])                # Para impresión de toda la lista
print(misNombres[0])                # Imprime el primer elemento
print(misNombres[-4])               # Si se indica índice negativo, cuenta desde el final -1 como el último elemento
print(misNombres[1:2])              # Porción de lista con el [:3] o [0:3] despliega los tres primeros elementos
print()
print(misNumeros[2:])               # Imprime desde el indice indicado hasta el final
misNombres.append("Antonio")        # Agrega elementos al final de la lista .append
print(misNombres[:])

misNombres.insert(2, "Pedro")       # Agrega elemenos en el índice indicado .insert
print(misNombres[:])

misNombres.extend(misNumeros[:])    # Agrega otra lista .extend
print(misNombres[:])

print(misNombres.index("Juan"))     # Imprime el índice del primer elemento indicado

print("Pepe" in misNombres)         # Imprime si el elemento se encuentra en la Lista indicada
a="Pepe" in misNombres              # Almacena el valor boolean en una variable
print(a)

misNombres.remove("Juan")           # Elimina un elemento de la lista
print(misNombres[:])

misNombres.pop()                    # Elimina el último elemento
print(misNombres[:])

misListas=misNombres+misNumeros     # Suma las dos listas como concatenadores
print(misListas[:])

misPaises=["Ecuador","Colomabia","Peru","Brasil"]*3     #Repite mi lista 3 veces o las que se indique
print(misPaises[:])

a=len(misPaises)
print(a)