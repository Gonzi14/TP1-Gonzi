def SeparadorDePalabras(palabras):
    palabraLista = palabras.split(" ")
    #lo voy cortando para poder ver cada palabra x separado
    lasPrimerasLetras = ""
    for i in palabraLista:
        lasPrimerasLetras = lasPrimerasLetras + i[0]
    return print(lasPrimerasLetras.upper())
    # asi queda mejor la cosa
if 0 == 0:
    palabras = input("mandame una oracion completa y te paso la abreviacion: ")
    SeparadorDePalabras(palabras)