import sys
import msvcrt

def CorridaAyA(listaNros):

    print("---------------------------------------------")
    print("-------- PRUEBA DE CORRIDA ARRIBA Y ABAJO --------")
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
        print("No se rechaza la hipotesis de que los numeros provienen de un universo uniformemente distribuido")
    else:
        print("Se rechaza la hipotesis de que los numeros provienen de un universo uniformemente distribuido")

    
    
    #3 Determinar el valor del estadístico Zo, utilizando la siguiente fórmula 
    

    #4. Si |𝒁𝟎|< Zα
    

    # except(ValueError):
    #     print("Tienes un error de tipo: ",sys.exc_info()[0])
    #     print("Nota: Se debe ingresar un valor de tipo numerico")





    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()

