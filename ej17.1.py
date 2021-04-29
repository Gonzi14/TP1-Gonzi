def hayQueSerAmarreta(textito, costeCorto, costeLargo, lonMax):
    textoCortado = textito.split(" ")
    costeTotal = 0
    mensajeFinal = ""
    for i in range(len(textoCortado)):
        aux = textoCortado[i]
        """ no se porque pero no me tira un error si en vez de poner lista pongo una variable que sea igual a una lista?
         asi q yqs lo puse asi, me aparecio en internet, tipo tiene sentido pero no lo hubiera pensado asi """
        if len(aux) <= lonMax:
            costeTotal = costeTotal + costeCorto
            mensajeFinal = mensajeFinal + aux + " "
            # profe porfa no me desapruebes :(
        else:
            costeTotal = costeTotal + costeLargo
            aux = aux[0:lonMax] + "@"
            """ aca le digo que si es una palabra largita que agarre solo lo que necesite osea [0:longitudMaxima]
             y le meto un @ al final """
            mensajeFinal = mensajeFinal + aux + " "
    # con voz de conductor de colectivo super grave
    print(f"mira capo, te queda asi: {mensajeFinal}.Te va a salir {costeTotal} mangos")


if 0 == 0:
    texto = input("escribime el texto: ")
    costeDeCorto = int(input("escribime el coste de corto: "))
    costeDeLargo = int(input("escribime el coste de largo: "))
    longitudMaxima = int(input("escribime una longitud maxima: "))
    hayQueSerAmarreta(texto, costeDeCorto, costeDeLargo, longitudMaxima)
