from pruebas.mensaje import MostrarMensaje

def Promedios(listaNros):

    print("---------------------------------------------")
    print("--------- PRUEBA DE LOS PROMEDIOS -----------")
    print("---------------------------------------------")

    i = 0
    m = 0
    n = len(listaNros)

    # try:  
    est_za = float(input("Ingrese el estadístico Za: "))

    while(i<n):
        m = m + float(listaNros[i])
        i = i+1

    prom = m/n

    print("Promedio X = " + str(prom))
    
    #3 Determinar el valor del estadístico Zo, utilizando la siguiente fórmula 
    est_z0 = ((prom-0.5)*pow(n,0.5))/0.2886

    print("Estadístico Zo = " + str(est_z0))

    #4. Si |𝒁𝟎|< Zα

    print("¿" + str(round(est_z0, 2)) + " < " + str(est_za) + "?")
    
    if est_z0 < est_za:
        MostrarMensaje(True)
    else:
        MostrarMensaje(False)

    # except(ValueError):
    #     print("Tienes un error de tipo: ",sys.exc_info()[0])
    #     print("Nota: Se debe ingresar un valor de tipo numerico")