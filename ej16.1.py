def SacameLasVocales(palabras):
    palabrasCortadas = ""
    for cadaLetra in palabras:
        if not cadaLetra in "AEIOU" and not cadaLetra in "aeiou":
            #aca me fijo si son en mayusculas o minusculas x las dudas
            palabrasCortadas = palabrasCortadas + cadaLetra
    return print(palabrasCortadas)


if 0 == 0:
    palabras = input("escribime una oracion: ")
    SacameLasVocales(palabras)
