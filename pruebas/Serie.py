import sys
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



def Serie(listaNros):

    print("---------------------------------------------")
    print("-------- PRUEBA DE SERIE--------")
    print("---------------------------------------------")


    x = int(input("Ingrese el numero de x al cuadrado: "))
    arrayTuplas = []
    n = len(listaNros)
    if((n % 2) != 0):
        print("Error. Cantidad de numeros generados impares")
        msvcrt.getch()
        return 0

        
    i=0
    while(i<n):
        arrayTuplas.append((listaNros[i],listaNros[i+1]))
        i = i+2

    matriz_subintervalos = crear_matriz(x)
    frecuencia_cuadrantes = contar_pares_ordenados(arrayTuplas, matriz_subintervalos)

    # Imprimir la frecuencia de los cuadrantes
    for i, fila in enumerate(frecuencia_cuadrantes):
        for j, frecuencia in enumerate(fila):
           print(f"Cuadrante ({i+1}, {j+1}): {frecuencia}")


    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()

