import os
from generators.generadores import *
from pruebas.pruebas import *

# def ingresarNumerosAleatorios():
#     listaNrosAleatorios = []
#     i = 0
#     cant = int(input("Cantidad de numeros a ingresar: "))
#     while(i<cant):
#         num = float(input("Numero",i+1,":"))
#         listaNrosAleatorios.append(num)
#         i = i+1
#     return listaNrosAleatorios

def limpiar_consola():
    if os.name == 'posix':  # Linux y macOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

def ingreso_manual():
    numeros = []
    while True:
        try:
            numero = float(input("Ingrese un número (ingrese una tecla no numérica para finalizar): "))
            numeros.append(numero)
            limpiar_consola()
            print("Números ingresados:", numeros)
        except ValueError:
            break
    return numeros
    
def menu_generadores():
    print("GENERADORES:")
    print("1. Método de la Parte Central del Cuadrado")
    print("2. Método de Lehmer")
    print("3. Método Congruencial Mixto")
    print("4. Método Congruencial Multiplicativo")
    print("5. Método Congruencial Aditivo")
    print("0. Volver")
    print("")
    
    seleccion = input("Opción: ")
    try:
        seleccion = int(seleccion)
        limpiar_consola()

        if seleccion == 1:
            listaGenerada = Cuadrado()
            print(listaGenerada)
        elif seleccion == 2:
            listaGenerada = Lehmer()
            print(listaGenerada)
        elif seleccion == 3:
            listaGenerada = CongruencialMixto()
            print(listaGenerada)
        elif seleccion == 4:
            listaGenerada = CongruencialMultiplicativo()
            print(listaGenerada)
        elif seleccion == 5:
            listaGenerada = CongruencialAditivo()
            print(listaGenerada)
        elif seleccion == 0:
            return []
        else:
            print("Error. Seleccione una opción válida.")
        
    except:
        if seleccion:
            print("Error. Seleccione una opción válida.")
    
    return listaGenerada

def menu_pruebas(listaPrueba):
    if len(listaPrueba) == 0:
        print("Para realizar las pruebas estadísticas se necesitan de números pseudo-aleatorios previamente generados.")
        print("Seleccione la forma de obtención de los números pseudo-aleatorios")
        print("Opción 1: Ingresarlos manualmente")
        print("Opción 2: Generarlos a través de un generador")
        try:
            opcion = int(input("Opción: "))
            limpiar_consola()
            if opcion == 1:
                listaNrosAleatorios = ingreso_manual()
            elif opcion == 2:
                listaNrosAleatorios = menu_generadores()
            else:
                print("Opción invalida")
        except:
            if opcion:
                print("Error. Seleccione una opción válida.")
    else:
        print("PRUEBAS ESTADÍSTICAS:")
        print("1. Prueba de los promedios")
        print("2. Prueba de la frecuencia")
        print("3. Prueba de la serie")
        print("4. Prueba de Kolmogorov-Smirnov (K-S)")
        print("5. Prueba de corrida arriba y abajo de la media")
        print("0. Volver")
        print("")
        
        seleccion = input("Opción: ")
        try:
            seleccion = int(seleccion)
            limpiar_consola()

            if seleccion == 1:
                Promedios(listaPrueba)
            elif seleccion == 2:
                Frecuencia(listaPrueba)
            elif seleccion == 3:
                Serie(listaPrueba)
            elif seleccion == 4:
                PruebaKS(listaPrueba)
            elif seleccion == 5:
                CorridaAyA(listaPrueba)
            elif seleccion == 0:
                return
            else:
                print("Error. Seleccione una opción válida.")
        except:
            if seleccion:
                print("Error. Seleccione una opción válida.")

#Funciona como un main. Indica que empieza a ejecutar aqui
if __name__ == '__main__':

    limpiar_consola()

    bandera = True
    listaNrosAleatorios = []

    print("--------------------------------------------------")
    print("---- GENERADORES DE NÚMEROS PSEUDO-ALEATORIOS ----")
    print("------------- Y PRUEBAS ESTADÍSTICAS -------------")
    print("--------------------------------------------------\n")
    
    while bandera == True:
        if len(listaNrosAleatorios) > 0:
            print("Números cargados: ")
            print(listaNrosAleatorios)
        else:
            print("No se encuentran números cargados")

        print("--------------------------------------------------")
        print("Seleccione una opción")
        print("1. Generadores\t\t2. Pruebas")
        print("0. Salir")
        print("")

        seleccion = input("Opción: ")
        
        try:
            seleccion = int(seleccion)
            limpiar_consola()

            if seleccion == 1:
                listaNrosAleatorios = menu_generadores()
            elif seleccion == 2:
                menu_pruebas(listaNrosAleatorios)
            elif seleccion == 0:
                bandera = False
            else:
                print("Error. Seleccione una opción válida.")
        except:
            if seleccion:
                print("Error. Seleccione una opción válida.")

        limpiar_consola()