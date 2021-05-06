vocales = {
    "a": "e",
    "e": "i",
    "i": "o",
    "o": "u",
    "u": "a",
    "A": "E",
    "E": "I",
    "I": "O",
    "O": "U",
    "U": "A",
}


def movemeLasVocales(palabritas, vocales):
    palabrasMovidas = ""
    for cadaLetra in palabritas:
        if cadaLetra in "AEIOUaeiou":
            cadaLetra = vocales[str(cadaLetra)]
        palabrasMovidas = palabrasMovidas + cadaLetra
    return print(palabrasMovidas)



if 0 == 0:
    palabras = input("escribime una oracion: ")
    movemeLasVocales(palabras, vocales)
