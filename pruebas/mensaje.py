import time
import sys
import os
import msvcrt

def mostrar_mensaje(resultado):
    mensaje_true = "No se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido."
    mensaje_false = "Se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido."

    if resultado:
        mensaje = mensaje_true
    else: mensaje = mensaje_false
    print('\a')

    for i in range(3):
        os.system('color FF')
        sys.stdout.write("\033[1;32m")
        sys.stdout.write(mensaje)
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\b" * len(mensaje))
        sys.stdout.write("\033[1;31m")
        sys.stdout.write(mensaje)
        sys.stdout.flush()
        time.sleep(0.4)
        if i != 2:
            sys.stdout.write("\b" * len(mensaje))
    sys.stdout.write("\033[0;37m")
    
    print("\nPresione cualquier tecla para continuar...")
    msvcrt.getch()

def mostrar_lista(lista = [], mensaje = "Números cargados: "):
    sys.stdout.write("\033[1;37m")
    print(mensaje)
    sys.stdout.write("\033[0;37m")
    print("[",end="")
    cont = 0
    for i, elem in enumerate(lista):
        if cont == 7:
            print("")
            cont = 0
        sys.stdout.write("\033[0;3" + str(i % 7 + 1) + "m")  # Color
        print(str(elem), end="")
        if i != len(lista) - 1:
            print(",",end=" ")
        cont += 1
    sys.stdout.write("\033[0;37m")
    print("]")