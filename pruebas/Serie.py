import sys

def Serie():

    listaNrosAleatorios = []

    print("---------------------------------------------")
    print("---- METODO CONGRUENCIAL MULTIPLICATIVO -----")
    print("---------------------------------------------")

    i=0

    try:
        semilla = int(input("Ingrese la semilla n0: "))
        a = int(input("Ingrese la constante multiplicativa a: "))
        m = int(input("Ingrese el modulo m: "))

        while(a<0):
            a = int(input("Error. Ingrese la constante multiplicativa a: "))
            
        while(semilla<0):
            semilla = int(input("Error. Ingrese la semilla n0: "))

        while(m<0):
            m = int(input("Error. Ingrese el modulo m: "))

        cantNro = int(input("Cantidad de numeros aleatorios a generar: "))
        
        while(i<cantNro):
            ni = (a*semilla)%m
            nroAleatorio = float(ni/m)
            tresDecimales = round(nroAleatorio, 3)
            listaNrosAleatorios.append(tresDecimales)
            print("u",i+1, ": ",tresDecimales)
            semilla = ni
            i = i+1
        
        return listaNrosAleatorios

    except(ValueError):
        print("Tienes un error de tipo: ",sys.exc_info()[0])
        print("Nota: Se debe ingresar un valor de tipo numerico")
