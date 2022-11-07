import os
os.system("cls")
#Lista con palabras
palabras1 = ["Manolo", "Pepe", "Juanito", "Jose", "Zanahoria"]
palabras2 = ["Tomate", "Melon", "Sandia", "Basura", "Python"]

numeros1 = [47, 56, 77, 23, 12]
numeros2 = [34, 42, 69, 80, 31]

palabrasJuntas = palabras1 + palabras2
numeroJuntos = numeros1 + numeros2

print("Palabras1 antes de ordenar: " + str(palabras1) + "\n")
print("Palabras2 antes de ordenar: " + str(palabras2) + "\n")

print("Numeros1 antes de ordenar: " + str(numeros1) + "\n")
print("Numeros2 antes de ordenar: " + str(numeros2) + "\n")

print("Palabras Unidas antes de ordenar: " + str(palabrasJuntas) + "\n")
print("Numeros Unidos antes de ordenar: " + str(numeroJuntos) + "\n")

palabrasOrdenadas = sorted(palabrasJuntas)
numerosOrdenados = sorted(numeroJuntos)

print("Palabras Unidas despues de ordenar: {} \n".format(palabrasOrdenadas))
print("Numeros Unidos despues de ordenar: {} \n".format(numerosOrdenados))
