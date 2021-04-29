x1 = int(input("dame la 1ra coordenadas de x:"))
x2 = int(input("dame la 2da coordenadas de x:"))
y1 = int(input("dame la 1ra coordenadas de y:"))
# profe porfa no me desapruebes :(
y2 = int(input("dame la 2da coordenadas de y:"))


def areaRec(x1, x2, y1, y2):
    x3 = abs(x2 - x1)
    y3 = abs(y2 - y1)
    area = y3 * x3
    return f"aca tenes el rectangulo maquina: {area}"
    """ aca a traves de 4 puntos le digo el rectangulo """

print(areaRec(x1, x2, y1, y2))
