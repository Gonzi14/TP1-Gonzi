def hayQueSerAmarreta(textito, costeCorto, costeLargo, lonMax):
    textoCortado = textito.split(" ")
    costeTotal = 0
    mensajeFinal = ""
    longitudDelTexto = len(textoCortado)
    nuevoTextoCortado = list()
    for palabra in textoCortado:
        nuevoTextoCortado[palabra] = textoCortado[palabra]
        """ no se porque pero no me tira un error si en vez de poner lista pongo una variable que sea igual a una lista?
         asi q yqs lo puse asi, me aparecio en internet, tipo tiene sentido pero no lo hubiera pensado asi """
        if len(palabra) <= lonMax:
            costeTotal = costeTotal + costeCorto
            # profe porfa no me desapruebes :(
            mensajeFinal = mensajeFinal + palabra + " "
        else:
            if palabra != "STOP" or palabra != "STOPSTOP":
                costeTotal = costeTotal + costeLargo
                palabra = palabra[0:lonMax] + "@"
                """ aca le digo que si es una palabra largita que agarre solo lo que necesite osea [0:longitudMaxima]
                 y le meto un @ al final """
                mensajeFinal = mensajeFinal + palabra + " "
    for palabra in textoCortado:
        for letras in palabra:
            print(letras)
            if letras == ".":
                palabra = palabra.replace('.', " ")
                palabra = nuevoTextoCortado.insert(palabra + 1, " STOP")

            if palabra == textoCortado[longitudDelTexto - 1]:
                palabra = palabra.replace('.', ' ')
                palabra = nuevoTextoCortado.insert(longitudDelTexto, " STOPSTOP")
    # con voz de conductor de colectivo super grave
    print(f"mira capo, te queda asi: {mensajeFinal}.Te va a salir {costeTotal} mangos")


if 0 == 0:
    texto = input("escribime el texto: ")
    costeDeCorto = int(input("escribime el coste de corto: "))
    costeDeLargo = int(input("escribime el coste de largo: "))
    longitudMaxima = int(input("escribime una longitud maxima: "))
    hayQueSerAmarreta(texto, costeDeCorto, costeDeLargo, longitudMaxima)
