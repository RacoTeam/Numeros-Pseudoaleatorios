from pruebas.mensaje import mostrar_mensaje
from pruebas.mensaje import mostrar_lista

def PruebaKS(listaNros):

    print("---------------------------------------------")
    print("---------------- PRUEBA K-S -----------------")
    print("---------------------------------------------")
    
    mostrar_lista(listaNros)

    # try:
    d_a = float(input("Ingrese el Estadístico d_(a,n): "))
    n = len(listaNros)

    print("---------------------------------------------")

    listaOrdenada = sorted(listaNros)
    listaFn = []

    i = 1
    while i <= n:
        listaFn.append(round(i/n, 3))
        i = i + 1

    print("Distribución Acumulada = " + str(listaFn))
    
    print("---------------------------------------------")

    j = 0
    listaResta = []
    while j < n:
        listaResta.append(round(listaFn[j] - listaOrdenada[j], 3))
        j = j + 1

    print("Estadístico K-S = " + str(listaResta))

    maximo = max(listaResta)

    print("Máximo = " + str(maximo))

    print("---------------------------------------------")

    print("¿" + str(round(maximo, 3)) + " < " + str(d_a) + "?", end="")

    if maximo < d_a:
        mostrar_mensaje(True)
    else:
        mostrar_mensaje(False)

