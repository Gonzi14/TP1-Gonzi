import time
from time import sleep
if 0 == 0:
    intentos = 0
    tiempito = 1
    while intentos != 100:
        intentodecontra = (input("ingrese la contra: "))
        if intentodecontra == "Gonzalo142214":
            print("Bienvenido")
            break
        else:
            intentos = intentos + 1
            tiempito = tiempito * tiempito + 1
            time.sleep(tiempito)
            print("Contra incorrecta, intente de nuevo")
    if intentos == 100:
        print("que malo que sos hackeando hermano")