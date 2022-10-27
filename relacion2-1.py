# importes
import os
import msvcrt

# Creamos el diccionario principal vacio
d = {}
#Booleano para salir o no
salir = False

# Funcion que muestra al usuario las opciones posibles
# E: Nada
# S: String con una opcion que puede valer para el menu o no
def menu():
    #Limpiamos pantalla de terminal
    os.system('cls')
    #Mostramos opciones
    print("Opciones \n **************************** \n 1 - Introducir un valor en el diccionario \n 2 - Eliminar un nombre del diccionario \n 3 - Mostrar todos los valores del diccionario \n 4 - Borrar el diccionario \n 9 - Salir")
    # Añadimos un end al final para que se quede en la misma linea
    print("Inserta un numero del menu: ", end="")
    opcion = input()
    return opcion

#Funcion que añade un valor al diccionario
# E: Nada
# S: Nada
def añadeValor():
    #Cogemos el array global
    global d
    os.system("cls")
    print("Vamos a introducir un valor nuevo. \nIntroduce un nombre en el diccionario: ", end="")
    nombre = input()
    # Obtenemos la ultima posicion del diccionario
    ultimaPos = len(d)
    # print(ultimaPos + 1)
    clave = "Valor" + str (ultimaPos + 1)
    #Creamos un string para la clave y añadimos el valor
    d[clave] = nombre
    #Volvemos a main
    main()

#Funcion para eliminar 1 solo valor del diccionario
# E: Nada
# S: Nada
def eliminarValor():
    #Cogemos el diccionario global
    global d
    os.system("cls")
    print("Vas a eliminar una clave del diccionario. \nIntroduce el numero de la clave a eliminar: ", end="")
    #Quitamos el elemento con la clave escrita en el diccionario usando un string (ya que todas las claves empiezan con "Clave")
    clave = d.pop("Valor" + input())
    #Guardando esto en una variable nos devuelve el nombre de esta
    print("Vas a eliminar la clave: " + clave + "\n")
    print("\nClave eliminada. El diccionario se quedará asi \n")
    for e in d.items():
        #Mostramos al usuario los items que quedan en el diccionario
        print(e)
    #Esperamos un input del usuario y volvemos a main
    print("\nPulsa cualquier tecla para continuar: ", end="")
    msvcrt.getch()
    main()

# Funcion para mostrar todos los datos del diccionario si los tienen
# E: Nada
# S: Nada
def mostrarDiccionario():
    #Cogemos el diccionario global
    global d
    #Guardamos la longitud
    longitud = len(d)
    if (longitud != 0):
        #Si la longitud es distinta de 0 entonces mostramos al usuario
        for e in d.items():
            print(e)
    else:
        #Y si no es el caso imprimimos en pantalla que esta vacio
        print("El diccionario esta vacio \n")
    #Esperamos un input de usuario y volvemos a main
    print("\nPulsa cualquier tecla para continuar: ", end="")
    msvcrt.getch()
    main()

# Funcion que borra el diccionario completamente
# E: Nada
# S: Nada
def borrarDiccionario():
    #Cogemos el diccionario global
    global d
    #Preguntamos si quiere borrar el diccionario entero
    print("¿De verdad que quieres borrar todo el contenido del diccionario? S-si N-no: ", end="")
    eleccion = input()
    #Mientras que se nos mande S o s 
    if (eleccion == "S" or eleccion == "s"):
        #Se borra el diccionario y lo notificamos al usuario
        d.clear()
        print("Se ha borrado el diccionario \n")
    #Esperamos un input del usuario y volvemos a main
    print("Pulsa cualquier tecla para continuar: ", end="")
    msvcrt.getch()
    main()

# Funcion para salir del programa con un mensaje de despedida
# E: Nada
# S: Nada
def salirPrograma():
    #Cojemos el booleano global
    global salir
    #Lo dejamos en true para salir del bucle
    salir = True
    #Y mostramos un mensaje de despedida
    print("Hasta otra\n Programa creado por: Pablo Sánchez López")

# Funcion main que trata que hacer con cada opcion
# E: Nada
# S: Nada
def main():
    #Cojemos el booleano global
    global salir
    #Mientras esta variable sea falsa
    while salir == False:
        #Guardamos la opcion del menu
        opcionMenu = int(menu())
        #Si ese valor coincide con 1 o 2 o 3 o 4 o 9, se llamará a su funcion correspondiente
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
                #Pero si no de da ningun caso se lo mostramos al usuario por pantalla
                print("No has seleccionado una opcion correcta, pulsa una tecla para continuar")
                msvcrt.getch()
            
main()