def atleuVodaD(listaParaDarVuelta):
    for i in range(len(listaParaDarVuelta) - 1, -1, -1):
        cantidad = len(listaParaDarVuelta)
        listaParaDarVuelta.append(listaParaDarVuelta[len(listaParaDarVuelta) - i - 1])
        listaParaDarVuelta.remove(listaParaDarVuelta[len(listaParaDarVuelta) - i - 1])
    return print(listaParaDarVuelta)


if 0 == 0:
    texto = input("mandame el texto: ")
    listaParaDarVuelta = texto.split()
    atleuVodaD(listaParaDarVuelta)