diasquepasaron = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]


def CheQueRapidoPasaElTiempo(mes, dia, diasquepasaron):
    totalidaddediasquepasaronhastahoy = 0
    for i in range(1, 12):
        if i == mes:
            totalidaddediasquepasaronhastahoy = diasquepasaron[i - 1] + dia
            #lo que estoy haciendo es sumar los dias que ya pasaron, sabiendo el mes, con el dia que me dijo el chico
    return totalidaddediasquepasaronhastahoy


if 0 == 0:
    dia = int(input("che me pasas el dia en el que estamos:  "))
    mes = int(input("estoy re perdido man sorry, pero me decis el mes:  "))
    print(CheQueRapidoPasaElTiempo(mes, dia, diasquepasaron))