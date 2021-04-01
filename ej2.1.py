def PerCal():
    h=int(input("capo, damela altura de tu rectangulo todo hermoso: "))
    b=int(input("y ahora dame la base y ya estariamos: "))
    p = b*2 + h*2
    if b==h:
        return f"como que me diste un cuadrado pero bue, aca tenes su perimetro {p} "
    else:
        return("el perimetro de tu rectangulo bellisimo es", p )

print(PerCal())