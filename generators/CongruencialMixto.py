import sys

def CongruencialMixto():

    listaNrosAleatorios = []

    print("---------------------------------------------")
    print("--------- MÉTODO CONGRUENCIAL MIXTO ---------")
    print("---------------------------------------------")

    i=0

    try:
        semilla = int(input("Ingrese la semilla n0: "))
        a = int(input("Ingrese la constante multiplicativa a: "))
        c = int(input("Ingrese la constante aditiva c: "))
        m = int(input("Ingrese el modulo m: "))

        while(a<0):
            a = int(input("Error. Ingrese la constante multiplicativa a: "))
            
        while(c<0):
            c = int(input("Error. Ingrese la constante aditiva c: "))

        while(m<0):
            m = int(input("Error. Ingrese el modulo m: "))

        cantNro = int(input("Cantidad de números aleatorios a generar: "))
        
        print("-------")
        while(i<cantNro):
            ni = (a*semilla+c)%m
            nroAleatorio = float(ni/m)
            listaNrosAleatorios.append(nroAleatorio)
            print("u" + str(i+1) + " : " + str(nroAleatorio))
            print("-------")
            semilla = ni
            i = i+1
        return listaNrosAleatorios

    except(ValueError):
        print("Tienes un error de tipo: ",sys.exc_info()[0])
        print("Nota: Se debe ingresar un valor de tipo numerico")

