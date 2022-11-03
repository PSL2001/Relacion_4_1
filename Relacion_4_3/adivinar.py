#Importes
import random
import os
import msvcrt

# E: Un maximo y un minimo (int)
# S: Un numero aleatorio entre el maximo y el minimo

def generarAleatorio(min, max):
    try:
        if (min > max):
            aux = min
            min = max
            max = aux
        return random.randint(min, max)
    except TypeError:
        print("Esta funcion solo admite numeros")
        return -1

# La funcion hace al usuario adivinar un numero generado aleatoriamente en un rango del 1 al 100
# Se le comunica al usuario si el numero que el ha introducido es menor o mayor que el numero a adivinar
# Al final se le comunica cuantos intentos ha necesitado
#E: Nada
#S: Nada
def adivinarNumero():
    adivinado = False
    aleatorio = generarAleatorio(1, 100)
    intentos = 0
    while(adivinado == False):
        os.system("cls")
        try:
            print("Introduce el numero a buscar: ", end="")
            numero = int(input())
            if(numero > aleatorio):
                print("El numero que buscas es menor\nPulsa cualquier tecla para continuar:", end="")
                intentos+= 1
                msvcrt.getch()
            if(numero < aleatorio):
                print("El numero que buscas es mayor\nPulsa cualquier tecla para continuar:", end="")
                intentos+=1
                msvcrt.getch()
            if(numero == aleatorio):
                print("Correcto! El numero que buscabas era el " + str(aleatorio) + " y solo has necesitado " + str(intentos) + " intentos", end="")
                adivinado = True
        except ValueError:
            os.system("cls")
            print("Introduce un numero!\nPulsa cualquier tecla para continuar:", end="")
            msvcrt.getch()

adivinarNumero()
