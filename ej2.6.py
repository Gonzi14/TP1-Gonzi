radio = int(input("dame la radio: "))
from math import pi


def PerCir(radio):
    volumen = (4 / 3) * pi * (radio ** 3)
    #  es la cuenta matematica para sacar el area, no se que queres que te diga
    return f"aca esta el volumen: {volumen}"


print(PerCir(radio))
