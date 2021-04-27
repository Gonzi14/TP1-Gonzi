def atleuVodaD(listaParaDarVuelta):
    listaDadaVuelta = []
    for i in range(len(listaParaDarVuelta) - 1, -1, -1):
        listaDadaVuelta.append(listaParaDarVuelta[i])
    return print(listaDadaVuelta)


if 0 == 0:
    texto = input("mandame el texto: ")
    listaParaDarVuelta = texto.split()
    atleuVodaD(listaParaDarVuelta)
