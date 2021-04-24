diaL = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def DiasQueFaltanParaIrATimesSquare(dia, mes, año, diaL):
    mesquefaltan = 12 - mes
    #aca me fijo cuantos meses faltan para terminar el año
    faltanadaparaqueterminelacuentaloprometo = 0
    if mesquefaltan != 0:
        for i in (range(mes, 12)):
            casicuentacompletadelosdiasquefaltan = DiasDelMes(año, i, diaL)
            faltanadaparaqueterminelacuentaloprometo = faltanadaparaqueterminelacuentaloprometo + casicuentacompletadelosdiasquefaltan
            #voy sumando los dias de los meses que faltan, y despues agrego el dia que me dijo
    lacuentacompleta = faltanadaparaqueterminelacuentaloprometo + LosDiasQueFaltanParaContarLaMoney(dia, mes, año, diaL)
    # en el caso que estemos en diciembre entonces solo es necesario calcular lo que falta para terminar el mes,
    # osea el 7.4
    return lacuentacompleta

def DiasDelMes(año, mes, eldiaquenoesdia):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        # Aca me fijo si el año es bisiesto por las dudas que pida febrero
        for i in range(1, 13):
            if i == mes:
                return eldiaquenoesdia[i - 1]
                # aca le resto uno a la i, porque o sino me va a tirar uno mas adelantado porque creo que las listas
                # empiezan con cero

    else:
        eldiaquenoesdia["2"] = [28]
    for i in range(1, 13):
        if i == mes:
            return eldiaquenoesdia[i - 1]


def LosDiasQueFaltanParaContarLaMoney(diaarestar, mes, año, diaL):
    return DiasDelMes(año, mes, diaL) - diaarestar


if 0 == 0:
    dia = int(input("che me pasas el dia en el que estamos:  "))
    mes = int(input("estoy re perdido man sorry, pero me decis el mes:  "))
    año = int(input("vengo del futuro, me decis el año en el que estamos: "))
    print(DiasQueFaltanParaIrATimesSquare(dia, mes, año, diaL))
