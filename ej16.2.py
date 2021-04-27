def MandameLasVocales(palabras):
    palabrasCortadas = ""
    for cadaLetra in palabras:
        if cadaLetra in "AEIOU" or cadaLetra.capitalize() in "AEIOU":
            #aca me fijo q sea si o si en mayusculas para estar seguro
            palabrasCortadas = palabrasCortadas + cadaLetra
    return print(palabrasCortadas)


if 0 == 0:
    palabras = input("escribime una oracion: ")
    MandameLasVocales(palabras)
