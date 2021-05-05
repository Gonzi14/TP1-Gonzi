def sacameLasVocales(palabras):
    palabrasCortadas = ""
    for cadaLetra in palabras:
        if not cadaLetra in "AEIOUaeiou":
            """ aca me fijo si son en mayusculas o minusculas x las dudas """
            palabrasCortadas = palabrasCortadas + cadaLetra
            # profe porfa no me desapruebes :(
    return print(palabrasCortadas)


if 0 == 0:
    palabras = input("escribime una oracion: ")
    sacameLasVocales(palabras)
