import sys
import msvcrt

def PruebaKS(listaNros):

    print("---------------------------------------------")
    print("---------------- PRUEBA K-S -----------------")
    print("---------------------------------------------")

    # try:  
    d_a = float(input("Ingrese el estadistico d: "))
    n = len(listaNros)

    listaOrdenada = sorted(listaNros)
    listaFn = []

    i = 0
    while(i<n):
        listaFn.append(i/n)
        i=i+1
    
    j=0
    listaResta = []

    while(j<n):
        listaResta.append(listaNros[j] - listaOrdenada[j])
        j = j + 10
    
    maximo  = max(listaResta)

    if(maximo < d_a):
        print("No se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido")
    else:
        print("Se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido")

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()

