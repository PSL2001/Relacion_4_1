# importes
import os
import msvcrt

# Creamos el diccionario principal
d = {}
#Booleano para salir o no
salir = False


def menu():
    os.system('cls')
    print("Opciones \n **************************** \n 1 - Introducir un valor en el diccionario \n 2 - Eliminar un nombre del diccionario \n 3 - Mostrar todos los valores del diccionario \n 4 - Borrar el diccionario \n 9 - Salir")
    print("Inserta un numero del menu: ", end="")
    opcion = input()
    return opcion


def añadeValor():
    global d
    os.system("cls")
    print("Vamos a introducir un valor nuevo. \nIntroduce un nombre en el diccionario: ", end="")
    nombre = input()
    # Obtenemos la ultima posicion del diccionario
    ultimaPos = len(d)
    print(ultimaPos + 1)
    clave = "Valor" + str (ultimaPos + 1)
    d[clave] = nombre
    main()

def eliminarValor():
    global d
    os.system("cls")
    print("Vas a eliminar una clave del diccionario. \nIntroduce el numero de la clave a eliminar: ", end="")
    clave = d.pop("Valor" + input())
    print("Vas a eliminar la clave: " + clave + "\n")
    print("\nClave eliminada. El diccionario se quedará asi \n")
    for e in d.items():
        print(e)
    print("\nPulsa cualquier tecla para continuar: ", end="")
    msvcrt.getch()
    main()

def mostrarDiccionario():
    global d
    longitud = len(d)
    if (longitud != 0):
        for e in d.items():
            print(e)
    else:
        print("El diccionario esta vacio \n")
    print("\nPulsa cualquier tecla para continuar: ", end="")
    msvcrt.getch()
    main()
    
def borrarDiccionario():
    global d
    print("¿De verdad que quieres borrar todo el contenido del diccionario? S-si N-no: ", end="")
    eleccion = input()

    if (eleccion == "S" or eleccion == "s"):
        d.clear()
        print("Se ha borrado el diccionario \n")

    print("Pulsa cualquier tecla para continuar: ", end="")
    msvcrt.getch()
    main()

def salirPrograma():
    global salir
    salir = True
    print("Hasta otra\n Programa creado por: Pablo Sánchez López")

def main():
    global salir
    while salir == False:
        opcionMenu = int(menu())
        match opcionMenu:
            case 1:
                añadeValor()
            case 2:      
                eliminarValor()
            case 3:
                mostrarDiccionario()
            case 4:
                borrarDiccionario()
            case 9:
                salirPrograma()
            case other:
                print("No has seleccionado una opcion correcta, pulsa una tecla para continuar")
                msvcrt.getch()
            
main()