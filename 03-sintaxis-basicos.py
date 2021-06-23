# Declaración de variables tipo INT
a=10                # Asiganación de valor "="
b=3

# Operador Módulo. Observar en Apuntes Función Módulo Sección 2.1
c=a%b
print(c)            # OUTPUT 1

# Operador exponente. Observar en Apuntes Función Módulo Sección 2.1
c=a**b
print(c)            # OUTPUT 1000

# Operador Division entera]. Observar en Apuntes Función Módulo Sección 2.1
c=a//b
print(c)            # OUTPUT 3

print(type(c))      # OUTPUT <class 'int'>

mensaje="""Esto es un mensaje
con tres
saltos
de linea"""
print(mensaje)

if a>b:
    print("Es mayor")
else:
    print("Es menor")