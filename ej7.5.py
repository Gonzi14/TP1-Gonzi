dia = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mesennumeritos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def DiasQueFaltanParaIrATimesSquare(dia, mesL):
    dias = LosDiasQueFaltanParaContarLaMoney(dia, mesL)
    mes = int(input("Me decis el mes otra vez que me lo olvide: "))
    for i in range(mes, 12):
        dias += DiasDelMes[1]
        return dias


def DiasDelMes(año, eldiaquenoesdia):
    mes = int(input("ingresar el mes, en numeros por supuesto: "))

    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        # Aca me fijo si el año es bisiesto por las dudas que pida febrero
        for i in range(1, 13):
            if i == mes:
                return eldiaquenoesdia[i - 1]
                # aca le resto uno a la i, porque o sino me va a tirar uno mas adelantado porque creo que las listas
                # empiezan con cero

    else:
        eldiaquenoesdia = [31, 28, 31, 30, 31, 30, 31, 31, 31, 30, 30, 31]
    for i in range(1, 13):
        if i == mes:
            return eldiaquenoesdia[i - 1]


def LosDiasQueFaltanParaContarLaMoney(diaarestar, mes):
    return DiasDelMes(int(input("dame el año brother: ")), dia) - diaarestar


print(DiasQueFaltanParaIrATimesSquare(int(input("Si queres dame un dia: ")), mesennumeritos))
