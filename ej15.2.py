def EscribimeloBien(palabras):
    palabrasSeparadas = palabras.split()
    oracion = ""
    for cadaPalabra in palabrasSeparadas:
        oracion = oracion + cadaPalabra.capitalize() + " "
        # le tengo que meter un espacio porque o sino esta todo juntito
    return print(oracion)


if 0 == 0:
    palabras = input("chiste gracioso en el que te pido que me des una oracion: ")
    EscribimeloBien(palabras)
