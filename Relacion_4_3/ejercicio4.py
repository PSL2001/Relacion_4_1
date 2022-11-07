import os
os.system("cls")
#Lista con palabras
palabras1 = ["Manolo", "Pepe", "Juanito", "Jose", "Zanahoria"]
palabras2 = ["Tomate", "Melon", "Sandia", "Basura", "Python"]

palabrasJuntas = palabras1 + palabras2

print("Palabras1 antes de ordenar: " + str(palabras1) + "\n")
print("Palabras2 antes de ordenar: " + str(palabras2) + "\n")

print("Palabras Unidas antes de ordenar: " + str(palabrasJuntas) + "\n")

palabrasOrdenadas = sorted(palabrasJuntas)

print("Palabras Unidas despues de ordenar: {} \n".format(palabrasOrdenadas))
