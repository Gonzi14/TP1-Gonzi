vocalesNormales = "AEIOU"
vocalesMovidasUnLugar = "EIOUA"


def MovemeLasVocales(palabritas, vocales, vocalesMovidas):
    palabrasMovidas = ""
    cambio = str.maketrans(vocales, vocalesMovidas)
    for cadaLetra in palabritas:
        cadaLetra = cadaLetra.upper()
        palabrasMovidas = palabrasMovidas + cadaLetra.translate(cambio)
        palabrasMovidas = palabrasMovidas.capitalize()
    return print(palabrasMovidas)


if 0 == 0:
    palabras = input("escribime una oracion: ")
    MovemeLasVocales(palabras, vocalesNormales, vocalesMovidasUnLugar)
