h=0
b=0
def areaRec():
    h=(int("dame la altura de tu rectangulo horrible "))
    b=(int("daaaaale dame tu base asi ya terminamos "))
    A=b*h
    if b==h:
        return f"como te gustan los cuadrados eh, jugas al minecraft? {A}"
    else:
        return("Aca tenes tu area:", A)

print(areaRec())