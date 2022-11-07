import os

def esVocal(car):
    vocales = "aeiouAEIOU"
    b = vocales.find(car)
    if (b > 0):
        return True
    else:
        return False
    

#Cuenta las vocales en una frase
def contarVocales():
    os.system("csl")
    texto = input("Introduce una frase: ")
    contador = 0

    for palabra in texto:
        if(esVocal(palabra)):
            contador += 1 
    
    print("Hay un total de: " + str (contador) + " vocales")

contarVocales()