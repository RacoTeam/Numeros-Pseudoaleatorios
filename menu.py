from generators import CongruencialAditivo
from generators import CongruencialMixto
from generators import CongruencialMultiplicativo
from generators import Lehmer
from generators import ParteCentralCuadrado

"""def ingresarNumerosAleatorios():
    listaNrosAleatorios = []
    i = 0
    cant = int(input("Cantidad de numeros a ingresar: "))
    while(i<cant):
        num = float(input("Numero",i+1,":"))
        listaNrosAleatorios.append(num)
        i = i+1
    return listaNrosAleatorios"""

print("--------------------------------------------------")
print("---- GENERADORES DE NUMEROS PSEUDO-ALEATORIOS ----")
print("------------- Y PRUEBAS ESTADISTICAS -------------")
print("--------------------------------------------------")

banderaGeneradores = True
listaNrosAleatorios = []

while banderaGeneradores == True:
    print("GENERADORES:")
    print("1. Metodo de la Parte Central del Cuadrado")
    print("2. Metodo de Lehmer")
    print("3. Metodo Congruencial Mixto")
    print("4. Metodo Congruencial Multiplicativo")
    print("5. Metodo Congruencial Aditivo")
    print("------------------------------------------------")
    print("PRUEBAS ESTADISTICAS:")
    print("6. Prueba de los promedios")
    print("7. Prueba de la frecuencia")
    print("8. Prueba de la serie")
    print("9. Prueba de Kolmogorov-Smirnov (K-S)")
    print("10. Prueba de corrida arriba y abajo de la media")
    print("")

    seleccion = int(input("Opción: "))

    def switch(seleccion):
        if seleccion == 1:
            listaNrosAleatorios = ParteCentralCuadrado.Cuadrado()
            print(listaNrosAleatorios)
        elif seleccion == 2:
            listaNrosAleatorios = Lehmer.Lehmer()
            print(listaNrosAleatorios)
        elif seleccion == 3:
            listaNrosAleatorios = CongruencialMixto.CongruencialMixto()
            print(listaNrosAleatorios)
        elif seleccion == 4:
            listaNrosAleatorios = CongruencialMultiplicativo.CongruencialMultiplicativo()
            print(listaNrosAleatorios)
        elif seleccion == 5:
            listaNrosAleatorios = CongruencialAditivo.CongruencialAditivo()
            print(listaNrosAleatorios)
        elif seleccion == 6:
            print("Para realizar las pruebas estadísticas se necesitan de números pseudo-aleatorios previamente generados.")
            print("Seleccione la forma de obtención de los números pseudo-aleatorios")
            print("Opcion 1: Ingresarlos manualmente")
            print("Opcion 2: Generarlos a traves de los generadores")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                print("Ingresar Manualmente nros aleatorios")
            elif opcion == 2:
                print("Menu Generadores")
            else:
                print("Opcion invalida")
        else:
            print("Error. Seleccione una opción válida.")

    switch(seleccion)
    banderaGeneradores = False