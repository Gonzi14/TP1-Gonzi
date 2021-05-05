diasquepasaron = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]


def cheQueRapidoPasaElTiempo(mes, dia, diasquepasaron, ano):
    totalidaddediasquepasaronhastahoy = 0
    if diasDelMes(ano, mes) == False:
        if mes > 1:
            diasquepasaron[mes - 1] = diasquepasaron[mes - 1] - 1
            """aca lo que le digo es que si NO es bisiesto que le reste un dia al mes especifico en el que esta al menos 
            que sea enero """
    # profe porfa no me desapruebes :(
    for i in range(0, 13):
        if i == mes:
            totalidaddediasquepasaronhastahoy = diasquepasaron[i - 1] + dia
            """lo que estoy haciendo es sumar los dias que ya pasaron, sabiendo el mes, con el dia que me dijo el 
            chico """
    return totalidaddediasquepasaronhastahoy


def diasDelMes(ano, mes):
    esBisiesto = False
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        """ Aca me fijo si el año es bisiesto por las dudas que pida febrero """
        for i in range(1, 13):
            if i == mes:
                esBisiesto = True
                return esBisiesto
    return esBisiesto


if 0 == 0:
    dia = int(input("che me pasas el dia en el que estamos:  "))
    mes = int(input("estoy re perdido man sorry, pero me decis el mes:  "))
    ano = int(input("eu me pasas la 3, la que te pregunta el ano:  "))
    print(cheQueRapidoPasaElTiempo(mes, dia, diasquepasaron, ano))
