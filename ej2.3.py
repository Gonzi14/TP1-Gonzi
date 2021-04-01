x1=int(input("dame la 1ra coordenadas de x:"))
x2=int(input("dame la 2da coordenadas de x:"))
y1=int(input("dame la 1ra coordenadas de y:"))
y2=int(input("dame la 2da coordenadas de y:"))
def AreaRec(x1,x2,y1,y2):
    x3=abs(x2-x1)
    y3=abs(y2-y1)
    A=y3*x3
    return f"aca tenes el rectangulo maquina: {A}"

print(AreaRec(x1,x2,y1,y2))