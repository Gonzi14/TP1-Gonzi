def AreaRec():
    altura = 0
    base = 0
    altura = int(input("dame la altura de tu rectangulo horrible: "))
    base = int(input("daaaaale dame tu base asi ya terminamos: "))
    area = base * altura
    if base == altura:
        return f"como te gustan los cuadrados eh, jugas al minecraft? {area}"
    else:
        return f"Aca tenes tu area: {area}"


print(AreaRec())
