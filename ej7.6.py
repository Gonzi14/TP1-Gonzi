diasquepasaron = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
mesennumeritos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def CheQueRapidoPasaElTiempo(mes, dia, diasquepasaron):
    totalidaddediasquepasaronhastahoy = 0
    for i in range(1, 12):
        if i == mes:
            totalidaddediasquepasaronhastahoy = diasquepasaron[i - 1] + dia
    return totalidaddediasquepasaronhastahoy


if 0 == 0:
    dia = int(input("che me pasas el dia en el que estamos:  "))
    mes = int(input("estoy re perdido man sorry, pero me decis el mes:  "))
    print(CheQueRapidoPasaElTiempo(mes, dia, diasquepasaron))
