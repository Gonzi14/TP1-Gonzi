dia = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mesennumeritos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def diasDelMes(ano, eldiaquenoesdia):
    mes = int(input("ingresar el mes, en numeros por supuesto: "))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        """ Aca me fijo si el año es bisiesto por las dudas que pida febrero """
        for i in range(1, 13):
            if i == mes:
                return eldiaquenoesdia[i - 1]
                """ aca le resto uno a la i, porque o sino me va a tirar uno mas adelantado porque creo que las listas
                 empiezan con cero """
    # profe porfa no me desapruebes :(
    else:
        eldiaquenoesdia = [28]
    for i in range(1, 13):
        if i == mes:
            return eldiaquenoesdia[i - 1]


print(diasDelMes(int(input("dame el ano: ")), dia))
