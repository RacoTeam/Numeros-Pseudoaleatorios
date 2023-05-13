import sys
import math
import msvcrt

def Lehmer():

    listaNrosAleatorios = []
    
    print("---------------------------------------------")
    print("-------------- MÉTODO DE LEHMER -------------")
    print("---------------------------------------------")

    i=0

    try:
        semilla = int(input("Ingrese la semilla n0: "))
        t = int(input("Ingrese el numero t: "))
        
        k = int(math.log10(t))+1
        n = int(math.log10(semilla))+1

        cantNro = int(input("Cantidad de números aleatorios a generar: "))
        while(k>n):
            print("Error. Volver a ingresar los números")
            semilla = int(input("Ingrese la semilla n0: "))
            t = int(input("Ingrese el numero t: "))
            k = int(math.log10(t))+1
            n = int(math.log10(semilla))+1

        print("-------")
        while(i<cantNro):
            total = str(semilla*t)
            kDig = total[0:k]
            ultimos = total[k:len(total)]
            ni = int(ultimos) - int(kDig)
            if ni < 0: 
                print("No se puede generar el número u" + str(i+1))
                print("Se guardará hasta el número u" + str(i))
                print("\nPresione una tecla para continuar...")
                msvcrt.getch()
                return listaNrosAleatorios
            concatenar = "0."+str(ni)
            nroAleatorio = float(concatenar)
            listaNrosAleatorios.append(nroAleatorio)
            print("n" + str(i+1) + " : " + str(ni))
            print("u" + str(i+1) + " : " + concatenar)
            print("-------")
            semilla = ni
            i = i+1
        
        return listaNrosAleatorios
            
    except(ValueError):
        print("Tienes un error de tipo: ",sys.exc_info()[0])
        print("Nota: Se debe ingresar un valor de tipo numerico")
        return []
