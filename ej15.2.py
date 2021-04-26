def EscribimeloBien(palabras):
    palabrasSeparadas = palabras.split()
    lasletritas = ""
    for i in palabrasSeparadas:
        lasletritas = lasletritas + i[0]

    return print(lasletritas.upper())


if 0 == 0:
    palabras = input("chiste gracioso en el que te pido que me des una oracion: ")
    EscribimeloBien(palabras)
