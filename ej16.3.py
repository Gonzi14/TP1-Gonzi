vocalesNormales = "AEIOU"
vocalesMovidasUnLugar = "EIOUA"


def movemeLasVocales(palabritas, vocales, vocalesMovidas):
    palabrasMovidas = ""
    cambio = str.maketrans(vocales, vocalesMovidas)
    for cadaLetra in palabritas:
        cadaLetra = cadaLetra.upper()
        palabrasMovidas = palabrasMovidas + cadaLetra.translate(cambio)
        # profe porfa no me desapruebes :(
        """ estas son cositas q aprendi en un videito de youtube, xq estuve intentando de hacer un diccionario y todo
          eso pero me parecia muuuy largo lo que me quedaba y asi me parece que queda mejor :) """
        palabrasMovidas = palabrasMovidas.capitalize()
    return print(palabrasMovidas)


if 0 == 0:
    palabras = input("escribime una oracion: ")
    movemeLasVocales(palabras, vocalesNormales, vocalesMovidasUnLugar)
