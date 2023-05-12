import sys
import msvcrt

def Frecuencia(listaNros):

    print("---------------------------------------------")
    print("--------- PRUEBA DE LA FRECUENCIA -----------")
    print("---------------------------------------------")

    # try:  
    # Datos
    x_a = float(input("Ingrese el estadistico Xa: "))
    n = len(listaNros)
    x = float(input("Ingrese el numero de subintervalos: "))
    
    listaIntervalos = []
    
    listaFrecuenciaObs = []

    #2. Dividir al intervalo (0,1) en x sub-intervalos.
    
    listaIntervalos.append(0)

    ancho = 1/x
    intervalo = ancho
    while intervalo <= 1:
        listaIntervalos.append(intervalo)
        intervalo = round(intervalo + ancho, 4)

    for i in range(x):
        listaFrecuenciaObs.append(0)

    #2.1 𝑭𝒆=𝒏/𝒙 Frecuencia esperada de variables u en cada subintervalo

    frecuenciaEsperada = n/x

    #3. Determinar la frecuencia observada en cada sub-intervalo. Se denota como Foj, (con j=1,2,…,x)

    for nro in listaNros:
        for i, inter in enumerate(listaIntervalos):
            if inter >= 1:
                break
            if inter < nro <= listaIntervalos[i+1]:
                listaFrecuenciaObs[i] += 1
                

    print(listaNros)
    print(listaIntervalos)
    print(listaFrecuenciaObs)

    #4 Determinar el valor del estadístico Chi Cuadrado 𝝌2, utilizando la siguiente fórmula 
    j=0
    while(j<n):
        sum = pow((listaFrecuenciaObs[j] - frecuenciaEsperada),2)
        j=j+1
    
    #4. Si |X2|< X2α
    
    x2 = frecuenciaEsperada*sum
    if(x2 < x_a):
        print("No se rechaza la hipotesis de que los numeros provienen de un universo uniformemente distribuido")
    else:
        print("Se rechaza la hipotesis de que los numeros provienen de un universo uniformemente distribuido")



    
    # if z_0 < z_a:
    #     print("No se rechaza la hipótesis de que los números")
    #     print("provienen de un universo uniformemente distribuido")
    # else:
    #     print("Se rechaza la hipótesis de que los números")
    #     print("provienen de un universo uniformemente distribuido")

    # except(ValueError):
    #     print("Tienes un error de tipo: ",sys.exc_info()[0])
    #     print("Nota: Se debe ingresar un valor de tipo numerico")

    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()