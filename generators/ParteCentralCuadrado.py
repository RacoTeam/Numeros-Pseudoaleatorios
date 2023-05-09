import sys

def Cuadrado():
    print("---------------------------------------------")
    print("-- METODO DE LA PARTE CENTRAL DEL CUADRADO --")
    print("---------------------------------------------")

    try:
        M = int(input("Ingrese la semilla M: "))
        n = int(input("Ingrese el numero de digitos deseados N: "))
        tot = int(input("Ingrese el total de numeros a generar TOT: "))

        j = 0
        while (j<tot):
            x = pow(M,2)
            cadenaX = str(x)
            digitosCadena = len(cadenaX)

            pOi = digitosCadena - n

            if pOi%2 == 0:
                if digitosCadena == 1:
                    print(cadenaX)
                    M = int(cadenaX)
                if digitosCadena == 3:
                    print(cadenaX[1])
                    M = int(cadenaX[1])
                if digitosCadena == 5:
                    print(cadenaX[1:4])
                    M = int(cadenaX[1:4])
                if digitosCadena == 7:
                    print(cadenaX[2:5])
                    M = int(cadenaX[2:5])
                
                concatenar = "0,"+str(M)
                print("-------")
                print("u",j+1, ": ",concatenar)
                print("-------")
                j = j+1

            else:
                xMult = x*10
                cadenaX = str(xMult)
                digitosCadena = len(cadenaX)
                if digitosCadena == 1:
                    print(cadenaX)
                    M = int(cadenaX)
                if digitosCadena == 3:
                    print(cadenaX[1])
                    M = int(cadenaX[1])
                if digitosCadena == 5:
                    print(cadenaX[1:4])
                    M = int(cadenaX[1:4])
                if digitosCadena == 7:
                    print(cadenaX[2:5])
                    M = int(cadenaX[2:5])

                concatenar = "0,"+str(M)
                print("-------")
                print("u",j+1, ": ",concatenar)
                print("-------")
                j=j+1    


    except(ValueError):
        print("Tienes un error de tipo: ",sys.exc_info()[0])
        print("Nota: Se debe ingresar un valor de tipo numerico")

        #Para verificar si es par o impar 