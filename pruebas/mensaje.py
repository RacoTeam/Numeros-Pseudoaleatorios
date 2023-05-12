import time
import sys
import os
import msvcrt

def MostrarMensaje(resultado):
    mensaje_true = "No se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido."
    mensaje_false = "Se rechaza la hipótesis de que los números provienen de un universo uniformemente distribuido."

    if resultado:
        mensaje = mensaje_true
    else: mensaje = mensaje_false

    for i in range(3):
        os.system('color FF')
        sys.stdout.write("\033[1;32m")
        sys.stdout.write(mensaje)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\b" * len(mensaje))
        sys.stdout.write("\033[1;31m")
        sys.stdout.write(mensaje)
        sys.stdout.flush()
        time.sleep(0.5)
        if i != 2:
            sys.stdout.write("\b" * len(mensaje))
    sys.stdout.write("\033[0;37m")
    
    print("\nPresione cualquier tecla para continuar...")
    msvcrt.getch()