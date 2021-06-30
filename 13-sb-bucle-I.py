# Bucle FOR

# Inicio de programa

for i in ["Cris","Naty","Cami"]:                 # La varaible i asigna el valor de la lista y cuenta hasta el fin de la lista
    print("Hola")
    print(i)

for i in [0,1,2,3,4,5,6,7,8,9]:
    print("Hola",end=" ")                        # Como queremos que finalice la impresión

print("")
print("")

print("Evaluación de correo el correo")

email=False
email_vl=input("Ingresa correo electrónico: ")

for i in email_vl:                                      # Lee los caracteres String
    if i =='@':
        email=True

if email:                                               # Implicitamente evalua variables boolean
    print("El email es correcto")
else:
    print("El email es incorrecto")

