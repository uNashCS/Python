# Operadores lógicos AND y OR
# Inicio de programa

print("Programa de BECAS 2021")
distancia=int(input("Ingresa la distancia de tu casa a la escuela (km): "))
print("Vives a: ",distancia, " km")
numero_hermanos=int(input("Introduce el número de hermanos que tienes: "))
print("Vives con:",numero_hermanos, " hermanos.")
salario_anual=int(input("Introduce el salrio anual: "))
print("El salario anual es: ",salario_anual, "dólares.")

if distancia>40 and numero_hermanos >2 or salario_anual <=20000:
    print(("Estás calificado para una beca."))
else:
    print(("No cumples con la totalidad de los requerimientos."))

print("")
print("Asiganturas Optativas - 2021")
print("Informática - Eletrónica - Redes - CISCO")
asignatura=input("Escribe la asigantura escogida: ")

if asignatura.lower() in ("infomática","electrónica","redes","cisco"):
    print("Asignatura elegida: ", asignatura)
else:
    print("La asignatura: \"",asignatura,"\" no existe")