def esPalindromogonomolotono(palabrita):
    validacion = True
    if palabrita == palabrita[::-1]:
        """ otra vez estuve intentando crear 3 variables para cada palabra y de esa manera poder ir fijandome la
         primera letra con la ultima, la segunda con la anteultima y despues vi en youtube que existia esta funcion
         y me acorto como 20 lineas """
        # profe porfa no me desapruebes :(
        validacion = True
    else:
        validacion = False
    return print(validacion)


if 0 == 0:
    palabra = input("escribime una palabra: ")
    esPalindromogonomolotono(palabra)
