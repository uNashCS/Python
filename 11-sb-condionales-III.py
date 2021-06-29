############### Condionales Switch - no existe ###############

# Alternativas, como el uso de diccionarios, concatenación de operadaores de comparación
# Operadores Lógicos
# Operador in

# Incio de programa
edad = int(input("Introduce edad: "))

if 0<edad<100:                          # Evalua la primera cndición y se cumple sigue a la siguiente, caso contrario salta
    print("Es correcta")
else:
    print("Edad incorrecta")

salario_director = int(input("Ingresa salario del Director: "))
print("Salario del presidente es: ",salario_director)
salario_administrador = int(input("Ingresa el salario del administrador: "))
print("Salario del administrador es: ",salario_administrador)
salario_oficinista = int(input("Ingresa salario del Oficinista: "))
print("El salario del oficinista es: ",salario_oficinista)

if salario_director>salario_administrador>salario_oficinista:
    print("Salarios Correctos")
else:
    print("Error de salarios")