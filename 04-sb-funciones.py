#Declaración de la función imprimir()
def imprimir():
    #Cuerpo de la función
    print("Estamos aprendiendo PYTHON")
    print("Developer:")
    print("Cristopher Salas")

# Llamar a la función
for i in range(2):
    imprimir()

print("Ejecutando código fuera de función")

def t1():
    for j in range(5):
        print(j)

for i in range(5):
    t1()