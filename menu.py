import sys
import math
from generators import (CongruencialAditivo, Lehmer, CongruencialMixto, CongruencialMultiplicativo, ParteCentralCuadrado)

print("--------------------------------------------------")
print("---- GENERADORES DE NUMEROS PSEUDO-ALEATORIOS ----")
print("------------- Y PRUEBAS ESTADISTICAS -------------")
print("--------------------------------------------------")

bandera = True

while bandera == True:
    print("GENERADORES:")
    print("1. Metodo de la Parte Central del Cuadrado")
    print("2. Metodo de Lehmer")
    print("3. Metodo Congruencial Mixto")
    print("4. Metodo Congruencial Multiplicativo")
    print("5. Metodo Congruencial Aditivo")
    seleccion = int(input("Opción:"))

    def switch(seleccion):
        if seleccion == 1:
            ParteCentralCuadrado.Cuadrado()
        elif seleccion == 2:
            Lehmer.Lehmer()
        elif seleccion == 3:
            CongruencialMixto.CongruencialMixto()
        elif seleccion == 4:
            CongruencialMultiplicativo.CongruencialMultiplicativo()
        elif seleccion == 5:
            CongruencialAditivo.CongruencialAditivo()

    print(switch(seleccion)) 

    bandera = False