#Importes
import os
import math
from datetime import date
import sys
# Archivo que contiene todas las funciones


def suma():
    print("Introduce un numero entero: ", end="")
    a = int(input())
    print("Introduce otro entero: ", end="")
    b = int(input())
    # Si nada de esto falla, entonces podemos sumar
    resultado = a + b
    os.system("cls")
    print("La suma de " + str(a) + " + " + str (b) + " = " + str (resultado))
    return a + b


def resta():
    print("Introduce un numero entero: ", end="")
    a = int(input())
    print("Introduce otro entero: ", end="")
    b = int(input())
    # Si nada de esto falla, entonces podemos restar
    resultado = a - b
    os.system("cls")
    print("La resta de " + str(a) + " - " + str(b) + " = " + str(resultado))
    return a - b


def multiplicar():
    print("Introduce un numero entero: ", end="")
    a = int(input())
    print("Introduce otro entero: ", end="")
    b = int(input())
    # Si nada de esto falla, entonces podemos multiplicar
    resultado = a * b
    os.system("cls")
    print("La multiplicacion de " + str(a) + " x " + str(b) + " = " + str(resultado))
    return a * b


def dividir():
    print("Introduce un numero entero: ", end="")
    a = int(input())
    print("Introduce otro entero: ", end="")
    b = int(input())
    # Si nada de esto falla, entonces podemos dividir
    resultado = a / b
    os.system("cls")
    print("La division de " + str(a) + " / " + str(b) + " = " + str(resultado))
    return a / b


def exponencial():
    print("Introduce un numero entero: ", end="")
    a = int(input())
    print("Introduce otro entero: ", end="")
    b = int(input())
    # Si nada de esto falla, entonces podemos hacer el exponencial
    resultado = a**b
    os.system("cls")
    print("El exponente de " + str(a) + " ^ " + str(b) + " = " + str(resultado))
    return a**b

def logBase10():
    print("Introduce un numero entero: ", end="")
    a = int(input())
    # Si nada de esto falla, entonces podemos hacer el exponencial
    resultado = math.log10(a)
    os.system("cls")
    print("El logaritmo de base 10 de " + str(a) + " es: " + str(resultado))
    return math.log10(a)

def fechaHoy():
    hoy = date.today()
    print("La fecha de hoy es: " + str (hoy))
    
def directorioPath():
    dir = sys.exec_prefix
    print("La ruta del path de Python es: " + str(dir))
