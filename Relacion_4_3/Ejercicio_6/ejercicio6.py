#Importes
import os
fichero = open("Ejercicio_6/texto1.txt", "r")
palabras = []
lineas = fichero.readlines()

fichero.close()

for linea in lineas:
    palabras.append(linea)

palabras.sort()

print("La lista de palabras ordenadas es: {}".format(palabras))

with open('resultado.txt', 'w') as fichNuevo:
    fichNuevo.write(str(palabras))
    fichNuevo.close()
os.system("cls")
print("Se ha escrito en el archivo resultado.txt")
