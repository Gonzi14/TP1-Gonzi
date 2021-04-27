radio = int(input("dame la radio: "))
from math import pi


def PerCir(radio):
    circunferencia = pi * radio * 2
    #  es la cuenta matematica para sacar la circunferencia, no se que queres que te diga
    return f"aca esta la circunferencia: {circunferencia}"


print(PerCir(radio))
