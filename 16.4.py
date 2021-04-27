def EsPalindromogonomolotono(palabrita):
    validacion = True
    if palabrita == palabrita[::-1]:
        validacion = True
    else:
        validacion = False
    return print(validacion)


if 0 == 0:
    palabra = input("escribime una palabra: ")
    EsPalindromogonomolotono(palabra)
