from pruebas.mensaje import MostrarMensaje

def PruebaKS(listaNros):

    print("---------------------------------------------")
    print("---------------- PRUEBA K-S -----------------")
    print("---------------------------------------------")

    # try:  
    d_a = float(input("Ingrese el Estadístico d: "))
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

    print("¿" + str(round(maximo, 2)) + " < " + str(d_a) + "?")

    if maximo < d_a:
        MostrarMensaje(True)
    else:
        MostrarMensaje(False)

