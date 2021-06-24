# Declaración de una función simple

def suma_simple_funcion():
    num1=5
    num2=7
    print("Único llamado")
    print(num1+num2)

# Llamado de la función
suma_simple_funcion()

# Creación de una función reutilizable
def suma_reut(num1, num2):
    print("Suma reutilizada")
    print(num1+num2)

suma_reut(4, 5)         # En el llamado se coloca los valores que se pide en la función creada
suma_reut(6, 8)         # Resultado diferente con la misma función
suma_reut(10, 11)
suma_reut(123123, 12312945845)

print("Imprime función Return")
def suma_return(num1,num2):
    resultado = num1+num2
    return resultado

# Función requiere de un detino para imprirmir el valor de la unción suma_return
print(suma_return(12, 12))


# Ejemplo de función reutilizable con función FOR

num=7
def multiplicacion(num1,num2):
    multi=num1*num2
    return multi

for i in range(10):
    res=multiplicacion(num, i+1)
    print("La multiplicación de :",multiplicacion(num, 1)," x ", i+1, "es:")
    print(res)
