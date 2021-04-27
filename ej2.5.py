radio = int(input("dame la radio: "))
from math import pi


def PerCir(radio):
    area = pi * (radio ** 2)
    #  es la cuenta matematica para sacar el area, no se que queres que te diga
    return f"aca esta el area: {area}"


print(PerCir(radio))
