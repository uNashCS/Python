print("Verificación de acceso: ")
edad_user=int(input("Introduce edad del usuario: "))
if edad_user<18:
    print("Acceso denegado")
elif(edad_user>100):
    print("Edad incorrecta")
else:
    print("Acceso concedido")

print("El programa ha finalizado")

nota_alumno=int(input("Ingresa la nota: "))

if(nota_alumno<5):
    print("Insuficiente")

elif(nota_alumno<7):
    print("Bien")

elif(nota_alumno<9):
    print("Notable")
else:
    print("Excelente")