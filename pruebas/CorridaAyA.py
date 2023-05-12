from pruebas.mensaje import mostrar_mensaje
from pruebas.mensaje import mostrar_lista
from itertools import groupby

# Son las 3am esto es un quilombo no pregunten como funciona
def obtener_frec_obs(listaConsec):

    listaConsec = [list(g) for k, g in groupby(listaConsec, lambda x:x>0)]

    # print(str(listaConsec))

    listaConsec.sort(key=len)
    listaConsec.reverse()

    # print(str(listaConsec))

    listaFrecObs = []

    max_long = len(listaConsec[0])

    for i in range(max_long):
        longitud = 0
        for sublist in listaConsec:
            if len(sublist) == (i + 1):
                longitud += 1
        listaFrecObs.append(longitud)

    return listaFrecObs

def CorridaAyA(listaNros):

    print("---------------------------------------------")
    print("------------ PRUEBA DE CORRIDA --------------")
    print("-------- ARRIBA Y ABAJO DE LA MEDIA ---------")
    print("---------------------------------------------")

    mostrar_lista(listaNros)
    # try:

    # 1. Generar una muestra de n números pseudo-aleatorios ui
    est_x = float(input("Ingrese el Estadístico Xa: "))
    n = len(listaNros)

    print("---------------------------------------------")

    # 2. A continuación la secuencia binaria S
    # 3. Determinar las longitudes de corrida (Frecuencia observada de longitud i)

    listaConsecutivos = []
    for num in listaNros:
        if num <= 0.5:
            listaConsecutivos.append(0)
        else:
            listaConsecutivos.append(1)

    listaFrecObs = obtener_frec_obs(listaConsecutivos)

    print("Frecuencias Observadas: ")
    for i, frec in enumerate(listaFrecObs):
        print("FO" + str(i + 1) + " = " + str(frec) + "\t", end="")
    
    print("")
    print("---------------------------------------------")

    # 4. Calcular la Frecuencia esperada para la i-ésima longitud 〖𝐹𝑒〗_𝑖=(𝑛−𝑖+3)/2^(𝑖+1) 

    listaFrecEsp = []

    for i in range(len(listaFrecObs)):
        listaFrecEsp.append(round((n - (i + 1) + 3)/pow(2, (i + 1) + 1), 3))

    print("Frecuencias Esperadas: ")
    for i, frec in enumerate(listaFrecEsp):
        print("FE" + str(i + 1) + " = " + str(frec) + "\t", end="")
    
    print("")
    print("---------------------------------------------")
    # 5. Calcular el Estadístico  𝝌2=∑_(𝒊=𝟏)^𝒙▒(〖𝑭𝒐〗_𝒊−〖𝑭𝒆〗_𝒊 )^𝟐/〖𝑭𝒆〗_𝒊 

    # Sumatoria
    chicuad = 0
    for i in range(len(listaFrecObs)):
        chicuad += pow(listaFrecObs[i] - listaFrecEsp[i], 2)/listaFrecEsp[i]

    chicuad = round(chicuad, 3)

    print("Estadístico X^2 (Chi Cuadrado) = " + str(chicuad))

    print("---------------------------------------------")

    print("¿" + str(chicuad) + " < " + str(est_x) + "?", end="")

    if(chicuad < est_x):
        mostrar_mensaje(True)
    else:
        mostrar_mensaje(False)