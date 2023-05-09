import sys

def CongruencialAditivo():
    print("---------------------------------------------")
    print("-------- METODO CONGRUENCIAL ADITIVO --------")
    print("---------------------------------------------")

    i=0
    j = 0
    lista = []

    try:
        k = int(input("Ingrese el mayor subindice k: "))
        while(i<=k):
            if(k==0):
                print("Ingrese el n0")
                ni = int(input())
                lista.append(ni)
                i = i+1

            else:    
                print("Ingrese el n -",k)
                ni = int(input())
                lista.append(ni)
                i = i+1
        m = int(input("Ingrese el modulo m: "))  
        while(m<0):
            m = int(input("Error. Ingrese el modulo m: "))

        ultimo = int(len(lista))
        for i in range(ultimo):
            ni = (int(lista[ultimo-1]) + int(lista[i])) % m
            nroAleatorio = float(ni/m)
            tresDecimales = round(nroAleatorio, 3)
            print("u",i+1, ": ",tresDecimales)
            lista.append(ni)
            ultimo = int(len(lista))


    except(ValueError):
        print("Tienes un error de tipo: ",sys.exc_info()[0])
        print("Nota: Se debe ingresar un valor de tipo numerico")
