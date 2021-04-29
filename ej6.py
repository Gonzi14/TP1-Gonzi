numerito1 = int(input("dame el Numero 1: "))
numerito2 = int(input("dame el Numero 2: "))
numerito3 = int(input("dame el Numero 3: "))
numerito4 = int(input("dame el Numero 4: "))
 # profe porfa no me desapruebes :(

def prrrrrrrrrrrroducto(numerito1, numerito2, numerito3, numerito4):
    mayorPrrrrrrrrrrrroducto = 0
    for i in (numerito2, numerito3, numerito4):
        prrrrrrrrrrrroducto = numerito1 * i
        if (prrrrrrrrrrrroducto > mayorPrrrrrrrrrrrroducto):
            mayorPrrrrrrrrrrrroducto = prrrrrrrrrrrroducto
    for i in (numerito3, numerito4):
        prrrrrrrrrrrroducto = numerito2 * i
        if (prrrrrrrrrrrroducto > mayorPrrrrrrrrrrrroducto):
            mayorPrrrrrrrrrrrroducto = prrrrrrrrrrrroducto
            """ aca lo q digo es que si el promedio que hiciste recien es mayor que lo que antes  considerabas mejor 
            promedio entonces este es el nuevo mayor jaja salu2 """
    prrrrrrrrrrrroducto = numerito3 * numerito4
    if (prrrrrrrrrrrroducto > mayorPrrrrrrrrrrrroducto):
        mayorPrrrrrrrrrrrroducto = prrrrrrrrrrrroducto
        return f"el mayor producto es: {mayorPrrrrrrrrrrrroducto}"


print(prrrrrrrrrrrroducto(numerito1, numerito2, numerito3, numerito4))
