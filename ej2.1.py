def PerCal():
    altura = int(input("capo, damela altura de tu rectangulo todo hermoso: "))
    base = int(input("y ahora dame la base y ya estariamos: "))
    perimetro = base * 2 + altura * 2
    if base == altura:
        return f"como que me diste un cuadrado pero bue, aca tenes su perimetro {perimetro} "
    else:
        return f"el perimetro de tu rectangulo bellisimo es {perimetro}"


print(PerCal())
