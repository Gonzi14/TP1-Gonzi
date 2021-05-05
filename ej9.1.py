if 0 == 0:
    contraVerdadera = "Gonzalo142214"
    intentos = 0
    while intentos != 100:
        intentodecontra = (input("ingrese la contra: "))
        if intentodecontra == contraVerdadera:
            print("Bienvenido")
            # profe porfa no me desapruebes :(
        else:
            print("Contra incorrecta, intente de nuevo")
            intentos = intentos + 1
    if intentos == 100:
        print("que malo que sos hackeando hermano")
