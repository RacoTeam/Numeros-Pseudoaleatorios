from pruebas.mensaje import mostrar_mensaje
from pruebas.mensaje import mostrar_lista

def Frecuencia(listaNros):

    print("---------------------------------------------")
    print("--------- PRUEBA DE LA FRECUENCIA -----------")
    print("---------------------------------------------")

    mostrar_lista(listaNros)
    # try:  
    # Datos
    x_2a = float(input("Ingrese el Estadístico X_2a: "))
    n = len(listaNros)
    x = int(input("Ingrese el número de subintervalos x: "))
    
    listaIntervalos = []
    listaFrecuenciaObs = []

    print("---------------------------------------------")

    #2. Dividir al intervalo (0,1) en x sub-intervalos.
    
    listaIntervalos.append(0)

    ancho = 1/x
    intervalo = ancho
    while intervalo <= 1:
        listaIntervalos.append(intervalo)
        intervalo = round(intervalo + ancho, 4)

    for i in range(x):
        listaFrecuenciaObs.append(0)

    mostrar_lista(listaIntervalos, "Intervalos: ")
    print("---------------------------------------------")

    #2.1 𝑭𝒆=𝒏/𝒙 Frecuencia esperada de variables u en cada subintervalo

    frecuenciaEsperada = n/x

    print("Frecuencia Esperada: " + str(frecuenciaEsperada))
    print("---------------------------------------------")

    #3. Determinar la frecuencia observada en cada sub-intervalo. Se denota como Foj, (con j=1,2,…,x)

    for nro in listaNros:
        for i, inter in enumerate(listaIntervalos):
            if inter >= 1:
                break
            if inter < nro <= listaIntervalos[i+1]:
                listaFrecuenciaObs[i] += 1
                
    mostrar_lista(listaFrecuenciaObs, "Frecuencia Observada: ")
    print("---------------------------------------------")

    #4 Determinar el valor del estadístico Chi Cuadrado 𝝌2, utilizando la siguiente fórmula 
    
    j = 0
    sumatoria = 0
    while j < x:
        sumatoria += pow((listaFrecuenciaObs[j] - frecuenciaEsperada),2)
        j = j + 1
        
    x_2 = (x/n) * sumatoria
    
    print("X^2 (Chi Cuadrado) = " + str(x/n) + " * " + str(sumatoria))
    
    print("X^2 (Chi Cuadrado) = " + str(x_2))
    print("---------------------------------------------")

    #4. Si |X2|< X2α

    print("¿" + str(round(x_2, 2)) + " < " + str(x_2a) + "?", end="")

    if x_2 < x_2a:
        mostrar_mensaje(True)
    else:
        mostrar_mensaje(False)

    # except(ValueError):
    #     print("Tienes un error de tipo: ",sys.exc_info()[0])
    #     print("Nota: Se debe ingresar un valor de tipo numerico")