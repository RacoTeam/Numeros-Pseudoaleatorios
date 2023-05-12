import os
import sys
from generators.generadores import *
from pruebas.pruebas import *


def limpiar_consola():
    if os.name == 'posix':  # Linux y macOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

def mostrar_lista(lista):
    sys.stdout.write("\033[1;37m")
    print("Numeros cargados: ")
    sys.stdout.write("\033[0;37m")
    print("[",end="")
    cont = 0
    for i, elem in enumerate(lista):
        if cont == 7:
            print("")
            cont = 0
        sys.stdout.write("\033[0;3" + str(i % 7 + 1) + "m")  # Color
        print(str(elem), end="")
        if i != len(lista) - 1:
            print(",",end=" ")
        cont += 1
    sys.stdout.write("\033[0;37m")
    print("]")

def ingreso_manual(listaNros):
    sys.stdout.write("\033[1;34m")
    print("--------------------------------------------------")
    print("----------------- INGRESO MANUAL -----------------")
    print("--------------------------------------------------")
    sys.stdout.write("\033[0;37m")
    mostrar_lista(listaNros)
    print("--------------------------------------------------\n")

    print("1. Añadir a lista")
    print("2. Cargar nueva lista")
    print("0. Volver")
    print("")

    seleccion = input("Opción: ")
    limpiar_consola()
    
    numeros = []
    i = 1

    if seleccion == "1":
        numeros = listaNros.copy()
        while True:
            try:
                print("Ingrese un número")
                print("Para finalizar ingrese una tecla no númerica")
                numero = float(input("n" + str(i) + ": "))
                i += 1
                numeros.append(numero)
                limpiar_consola()
                print("Números ingresados:", numeros)
            except ValueError:
                return numeros
    elif seleccion == "2":
        while True:
            try:
                print("Ingrese un número")
                print("Para finalizar ingrese una tecla no númerica")
                numero = float(input("n" + str(i) + ": "))
                i += 1
                numeros.append(numero)
                limpiar_consola()
                print("Números ingresados:", numeros)
            except ValueError:
                return numeros
    elif seleccion == "0":
        return listaNros
    else:
        print("Error. Seleccione una opción válida.")
    
def menu_generadores(listaNros):
    os.system('color FF')
    sys.stdout.write("\033[1;35m")
    print("--------------------------------------------------")
    print("---------- GENERADORES PSEUDOALEATORIOS ----------")
    print("--------------------------------------------------")
    sys.stdout.write("\033[0;37m")
    mostrar_lista(listaNros)
    print("--------------------------------------------------\n")
    print("1. Método de la Parte Central del Cuadrado")
    print("2. Método de Lehmer")
    print("3. Método Congruencial Mixto")
    print("4. Método Congruencial Multiplicativo")
    print("5. Método Congruencial Aditivo")
    print("0. Volver")
    print("")
    
    seleccion = input("Opción: ")
    try:
        limpiar_consola()

        if seleccion == "1":
            listaGenerada = Cuadrado()
            print(listaGenerada)
        elif seleccion == "2":
            listaGenerada = Lehmer()
            print(listaGenerada)
        elif seleccion == "3":
            listaGenerada = CongruencialMixto()
            print(listaGenerada)
        elif seleccion == "4":
            listaGenerada = CongruencialMultiplicativo()
            print(listaGenerada)
        elif seleccion == "5":
            listaGenerada = CongruencialAditivo()
            print(listaGenerada)
        elif seleccion == "0":
            return listaNros
        else:
            print("Error. Seleccione una opción válida.")
        
    except:
        if seleccion:
            print("Error. Seleccione una opción válida.")
    
    return listaGenerada

def menu_pruebas(listaPrueba):
    sys.stdout.write("\033[1;36m")
    print("--------------------------------------------------")
    print("-------------- PRUEBAS ESTADÍSTICAS --------------")
    print("--------------------------------------------------")
    sys.stdout.write("\033[0;37m")
    mostrar_lista(listaPrueba)
    print("--------------------------------------------------\n")
    print("1. Prueba de los promedios")
    print("2. Prueba de la frecuencia")
    print("3. Prueba de la serie")
    print("4. Prueba de Kolmogorov-Smirnov (K-S)")
    print("5. Prueba de corrida arriba y abajo de la media")
    print("0. Volver")
    print("")
    
    seleccion = input("Opción: ")
    # try:
    limpiar_consola()

    if seleccion == "1":
        Promedios(listaPrueba)
    elif seleccion == "2":
        Frecuencia(listaPrueba)
    elif seleccion == "3":
        Serie(listaPrueba)
    elif seleccion == "4":
        PruebaKS(listaPrueba)
    elif seleccion == "5":
        CorridaAyA(listaPrueba)
    elif seleccion == "0":
        return
    else:
        print("Error. Seleccione una opción válida.")
    # except:
    #     if seleccion:
    #         print("Error.")

#Funciona como un main. Indica que empieza a ejecutar aqui
if __name__ == '__main__':

    limpiar_consola()

    bandera = True
    listaNrosAleatorios = [0.01, 0.079, 0.168, 0.858, 0.901, 0.74, 0.713, 0.478, 0.277, 0.019, 0.548, 0.426]

    while bandera == True:
        os.system('color FF')
        sys.stdout.write("\033[1;32m")
        print("--------------------------------------------------")
        print("---- GENERADORES DE NÚMEROS PSEUDO-ALEATORIOS ----")
        print("------------- Y PRUEBAS ESTADÍSTICAS -------------")
        print("--------------------------------------------------")
        sys.stdout.write("\033[0;37m")

        if len(listaNrosAleatorios) > 0:
            mostrar_lista(listaNrosAleatorios)
        else:
            print("No se encuentran números cargados")

        print("--------------------------------------------------")
        sys.stdout.write("\033[1;37m")
        print("Seleccione una opción:")
        sys.stdout.write("\033[0;37m")
        sys.stdout.write("\033[4;35m")
        print("1. Generadores\t\t",end="")
        sys.stdout.write("\033[4;36m")
        print("2. Pruebas")
        sys.stdout.write("\033[4;34m")
        print("3. Ingresar datos manualmente")
        sys.stdout.write("\033[4;31m")
        print("0. Salir")
        sys.stdout.write("\033[0;37m")
        print("")

        seleccion = input("Opción: ")
        
        # try:
        limpiar_consola()

        if seleccion == "1":
            listaNrosAleatorios = menu_generadores(listaNrosAleatorios)
        elif seleccion == "2":
            if len(listaNrosAleatorios) == 0:
                print("Para realizar las pruebas estadísticas se necesitan de números pseudo-aleatorios previamente generados.")
                print("Seleccione la forma de obtención de los números pseudo-aleatorios")
                print("Opción 1: Ingresarlos manualmente")
                print("Opción 2: Generarlos a través de un generador")
                # try:
                opcion = int(input("Opción: "))
                limpiar_consola()
                if opcion == 1:
                    listaNrosAleatorios = ingreso_manual(listaNrosAleatorios)
                elif opcion == 2:
                    listaNrosAleatorios = menu_generadores(listaNrosAleatorios)
                else:
                    print("Opción invalida")
                # except:
                #     if opcion:
                #         print("Error. Seleccione una opción válida.")
            else:
                menu_pruebas(listaNrosAleatorios)
        elif seleccion == "3":
            listaNrosAleatorios = ingreso_manual(listaNrosAleatorios)
        elif seleccion == "0":
            bandera = False
        else:
            print("Error. Seleccione una opción válida.")
        # except:
        #     if seleccion:
        #         print("Error. Seleccione una opción válida.")

        limpiar_consola()