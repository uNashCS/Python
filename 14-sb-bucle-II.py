for i in range(6):
    print(f"El valor de la variable {i}")           # La f indica tipo funcion f - Como concatenación

for j in range(5,10):                               # El tipo range cuenta desde el 5 hasta el 9
    print(f"El valor es: {j}")

for k in range(5,50,3):                             # Cuenta desde el 5 al 50, y salta de 3 en 3, (ejemplo)
    print(k)

email = input("Inresa correo: ")
valido=False

for i in range(len(email)):
    print(email[i])
    if email[i]=='@':
        valido=True

if valido:
    print("Correo Válido")
else:
    print("COrreo Inválido")