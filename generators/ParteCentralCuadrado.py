import sys

def Cuadrado():
    listaNrosAleatorios = []

    print("---------------------------------------------")
    print("-- MÉTODO DE LA PARTE CENTRAL DEL CUADRADO --")
    print("---------------------------------------------")
    
    try:
        M = int(input("Ingrese la semilla M: "))
        n = int(input("Ingrese el numero de digitos deseados N: "))
        tot = int(input("Ingrese el total de números a generar TOT: "))
        
        j = 0 
        banderaprint = True
        
        print("-------")
        while (j<tot):
            x = pow(M,2)
            str_numero = str(x)
            longitud = len(str_numero)
            mitad = longitud // 2
            inicio = mitad - (n // 2)
            fin = inicio + n
            partes_centrales = str_numero[inicio:fin]
            concatenar = "0."+str(partes_centrales)
            nroAleatorio = float(concatenar)
            listaNrosAleatorios.append(nroAleatorio)
            print("u" + str(j+1) + " : " + concatenar)
            print("-------")
            M = int(partes_centrales)
            j=j+1

        return listaNrosAleatorios
    
    except(ValueError):
        print("Tienes un error de tipo: ",sys.exc_info()[0])
        print("Nota: Se debe ingresar un valor de tipo numerico")
