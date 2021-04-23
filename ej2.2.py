altura=0
base=0
def AreaRec():
    altura=(int("dame la altura de tu rectangulo horrible "))
    base=(int("daaaaale dame tu base asi ya terminamos "))
    area=base*altura
    if base==altura:
        return f"como te gustan los cuadrados eh, jugas al minecraft? {area}"
    else:
        return("Aca tenes tu area:", area)

print(AreaRec())