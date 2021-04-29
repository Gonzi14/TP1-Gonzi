import time
from time import sleep
# profe porfa no me desapruebes :(
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
            """ aca estoy haciendo que el tiempo se agrande basicamente, infinitamente asi que aunque tiene 100 
                        intentos, tiene que esperar todo ese tiempo"""
            time.sleep(tiempito)
            print("Contra incorrecta, intente de nuevo")
    if intentos == 100:
        print("que malo que sos hackeando hermano")