def atleuVodaD(listaParaDarVuelta):
    listaDadaVuelta = []
    for i in range(len(listaParaDarVuelta) - 1, -1, -1):
        # profe porfa no me desapruebes :(
        listaDadaVuelta.append(listaParaDarVuelta[i])
        """como que va metiendo las cositas de atras de todo a una lista nueva"""
    return print(listaDadaVuelta)


if 0 == 0:
    texto = input("mandame el texto: ")
    listaParaDarVuelta = texto.split()
    atleuVodaD(listaParaDarVuelta)
