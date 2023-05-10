import sys
import msvcrt

def Frecuencia(listaNros):

    print("---------------------------------------------")
    print("--------- PRUEBA DE LA FRECUENCIA -----------")
    print("---------------------------------------------")

    # try:  
    # Datos
    z_a = float(input("Ingrese el estadistico Za: "))
    n = len(listaNros)
    x = float(input("Ingrese el numero de subintervalos: "))
    
    listaIntervalos = []
    listaFrecuenciaEsp = []
    listaFrecuenciaObs = []

    #2. Dividir al intervalo (0,1) en x sub-intervalos.

    ancho = 1/x
    intervalo = ancho
    while intervalo <= 1:
        listaIntervalos.append(intervalo)
        intervalo = round(intervalo + ancho, 6)

    #2.1 𝑭𝒆=𝒏/𝒙 Frecuencia esperada de variables u en cada subintervalo

    for nro in listaNros:
        for inter in listaIntervalos:
            if nro < inter

    #3. Determinar la frecuencia observada en cada sub-intervalo. Se denota como Foj, (con j=1,2,…,x)

    #4 Determinar el valor del estadístico Chi Cuadrado 𝝌2, utilizando la siguiente fórmula 
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