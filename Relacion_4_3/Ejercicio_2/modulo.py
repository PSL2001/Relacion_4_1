#Importes
import os



class Persona:
    
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getEdad(self):
        return self.edad
    
    def setEdad(self, edad):
        self.edad = edad
    
    def getSalario(self):
        return self.salario
    
    def setSalario(self, salario):
        self.salario = salario
    
    def __str__(self) -> str:
        return str (self.nombre) + ", " + str (self.edad) + ", " + str (self.salario)

    def toString(self):
        return str (self.nombre) + ", " + str (self.edad) + ", " + str (self.salario)
    
    def editarFichero(ruta, texto):
        os.system("cls")
        if (texto == ""):
            print("¿Que deseas añadir al texto?")
            texto = input()
        
        with open(ruta, "w") as fichero:
            fichero.write(texto)
            fichero.close()
    

    
