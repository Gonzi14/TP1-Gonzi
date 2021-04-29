def atleuVodaD(listaParaDarVuelta):
    for i in range(len(listaParaDarVuelta) - 1, -1, -1):
        cantidad = len(listaParaDarVuelta)
        listaParaDarVuelta.append(listaParaDarVuelta[len(listaParaDarVuelta) - i - 1])
        # profe porfa no me desapruebes :(
        listaParaDarVuelta.remove(listaParaDarVuelta[len(listaParaDarVuelta) - i - 1])
        """lo que hace esto es que agarra la lista y mientras que saca una lo va metiendo al otro lado"""
    return print(listaParaDarVuelta)


if 0 == 0:
    texto = input("mandame el texto: ")
    listaParaDarVuelta = texto.split()
    atleuVodaD(listaParaDarVuelta)