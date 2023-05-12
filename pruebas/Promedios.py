import sys
import msvcrt

def Promedios(listaNros):

    print("---------------------------------------------")
    print("--------- PRUEBA DE LOS PROMEDIOS -----------")
    print("---------------------------------------------")

    i = 0
    m = 0
    n = len(listaNros)

    # try:  
    z_a = float(input("Ingrese el estadistico Za: "))

    while(i<n):
        m = m + float(listaNros[i])
        i = i+1

    prom = m/n
    
    #3 Determinar el valor del estadístico Zo, utilizando la siguiente fórmula 
    z_0 = ((prom-0.5)*pow(n,0.5))/0.2886

    #4. Si |𝒁𝟎|< Zα
    if z_0 < z_a:
        print("No se rechaza la hipótesis de que los números")
        print("provienen de un universo uniformemente distribuido")
    else:
        print("Se rechaza la hipótesis de que los números")
        print("provienen de un universo uniformemente distribuido")

    # except(ValueError):
    #     print("Tienes un error de tipo: ",sys.exc_info()[0])
    #     print("Nota: Se debe ingresar un valor de tipo numerico")

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()