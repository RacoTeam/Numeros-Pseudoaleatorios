import sys
import math

def Lehmer():

    listaNrosAleatorios = []
    
    print("---------------------------------------------")
    print("-------------- METODO DE LEHMER -------------")
    print("---------------------------------------------")

    i=0

    try:
        semilla = int(input("Ingrese la semilla n0: "))
        t = int(input("Ingrese el numero t: "))
        
        k = int(math.log10(t))+1
        n = int(math.log10(semilla))+1

        cantNro = int(input("Cantidad de numeros aleatorios a generar: "))
        while(k>n):
            print("Error. Volver a ingresar los numeros")
            semilla = int(input("Ingrese la semilla n0: "))
            t = int(input("Ingrese el numero t: "))
            k = int(math.log10(t))+1
            n = int(math.log10(semilla))+1

        while(i<cantNro):
            total = str(semilla*t)
            kDig = total[0:k]
            ultimos = total[k:len(total)]
            ni = int(ultimos) - int(kDig)
            concatenar = "0."+str(ni)
            nroAleatorio = float(concatenar)
            listaNrosAleatorios.append(nroAleatorio)
            print("-------")
            print("n",i+1, ": ",ni)
            print("u",i+1, ": ",concatenar)
            print("-------")
            semilla = ni
            i = i+1

        return listaNrosAleatorios
            
    except(ValueError):
        print("Tienes un error de tipo: ",sys.exc_info()[0])
        print("Nota: Se debe ingresar un valor de tipo numerico")

Lehmer()