#Importes
import Ejercicio_2.modulo as modulo


persona1 = modulo.Persona("Paquito", 57, 500)
persona2 = modulo.Persona("Manolo", 18, 650)

print("Persona 1: " + str(persona1))

salarios = [persona1.getSalario(), persona2.getSalario()]

print("Salarios antes de modificarlos: " + str (salarios))

persona2.setSalario(150)

salarios[1] = persona2.getSalario()

print("Salarios despues de modificarlos: " + str (salarios))

modulo.Persona.editarFichero("texto.txt", persona1.toString())
print("Se ha escrito en el fichero texto.txt")
