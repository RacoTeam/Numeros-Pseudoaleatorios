from pruebas.mensaje import MostrarMensaje
import msvcrt

def crear_matriz(x):
    matriz = []
    ancho_subintervalo = 1 / x
    largo_subintervalo = 1 / x
    
    for i in range(x):
        fila = []
        for j in range(x):
            subintervalo = {
                'inicio_ancho': i * ancho_subintervalo,
                'fin_ancho': (i + 1) * ancho_subintervalo,
                'inicio_largo': j * largo_subintervalo,
                'fin_largo': (j + 1) * largo_subintervalo,
            }
            fila.append(subintervalo)
        matriz.append(fila)
    
    return matriz

def contar_pares_ordenados(pares, matriz):
    contador = [[0] * len(matriz) for _ in range(len(matriz[0]))]
    
    for par in pares:
        numero_fila = par[0]
        numero_columna = par[1]
        
        for i, fila in enumerate(matriz):
            for j, subintervalo in enumerate(fila):
                if subintervalo['inicio_ancho'] <= numero_fila <= subintervalo['fin_ancho'] and \
                   subintervalo['inicio_largo'] <= numero_columna <= subintervalo['fin_largo']:
                    contador[i][j] += 1
    
    return contador

def dibujar_matriz(matriz):
    size = len(matriz)

    # Dibuja los bordes superiores de la matriz
    print("+" + "-" * (size * 2 - 1) + "+")

    for fila in matriz:
        # Dibuja los elementos de la fila
        print("|" + " ".join(str(elemento) for elemento in fila) + "|")

    # Dibuja el borde inferior de la matriz
    print("+" + "-" * (size * 2 - 1) + "+")

def Serie(listaNros):

    print("---------------------------------------------")
    print("------------- PRUEBA DE SERIE ---------------")
    print("---------------------------------------------")

    
    # 1. Generar n pares de números pseudo-aleatorios (ui, u i+1 )
    
    if (len(listaNros) % 2) != 0:
        print("Error. Cantidad de números generados impares.")
        print("Cargue una cantidad par e intente de nuevo.")
        msvcrt.getch()
        return 0
    n = len(listaNros)/2
    
    est_x2 = float(input("Ingrese el estadístico X2a: "))
    x = int(input("Ingrese cantidad de filas/columnas X: "))
    
    # 2. Dividir el cuadrado unitario en x2 celdas. 
    # 𝐅𝐞=𝐧/𝐱^𝟐   Frecuencia esperada en cada una de las celdas
    
    frecuenciaEsp = n/pow(x, 2)
    
    # 3. Determinar la frecuencia observada en cada una de las x2 celdas. 
    # Se denota como Fjk (con j,k=1,2,…,x)

    arrayTuplas = []
    i = 0
    while i < (n * 2):
        arrayTuplas.append((listaNros[i],listaNros[i+1]))
        i = i + 2

    matriz_subintervalos = crear_matriz(x)
    frecuenciaObs = contar_pares_ordenados(arrayTuplas, matriz_subintervalos)

    # Imprimir la frecuencia de los cuadrantes
    # for i, fila in enumerate(frecuenciaObs):
    #     for j, frecuencia in enumerate(fila):
    #        print(f"Cuadrante ({i+1}, {j+1}): {frecuencia}")

    dibujar_matriz(frecuenciaObs)

    # 4. Calcular el Estadístico Chi Cuadrado

    # Quito las sublistas
    frecuenciaObs_lineal = [item for sublist in frecuenciaObs for item in sublist]

    # Calculo sumatoria
    chicuad = sumatoria = 0
    for j, frec in enumerate(frecuenciaObs_lineal):
        sumatoria += pow((frec - frecuenciaEsp), 2)
    
    # Calculo chi cuadrado
    chicuad = (pow(x, 2)/n) * sumatoria

    # 5. Si 𝝌2 <𝝌"2α" no se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido
    
    print("Chi Cuadrado X^2 = " + str(round(chicuad, 2)))

    print("¿" + str(round(chicuad, 2)) + " < " + str(est_x2) + "?")

    if chicuad < est_x2:
        MostrarMensaje(True)
    else:
        MostrarMensaje(False)