def elegirPalabrasEspecifica(palabras, laLetrita):
    palabrasSeparadas = palabras.split()
    oracion = ""
    for cadaPalabra in palabrasSeparadas:
        if cadaPalabra[0].capitalize() == laLetrita.upper():
            """ aca me voy fijando si cada palabra empieza con la letra especifica, fijandome en la letra numero 0,
             osea primera, de cada palabra """
            # profe porfa no me desapruebes :(
            oracion = oracion + cadaPalabra.capitalize() + " "
        """ le tengo que meter un espacio porque o sino esta todo juntito """
    return print(oracion)


if 0 == 0:
    palabras = input("escribime una oracion: ")
    letraEspecial = input("escribime la letra especial: ")
    elegirPalabrasEspecifica(palabras, letraEspecial)
