n1=int(input("dame el N1: "))
n2=int(input("dame el N2: "))
n3=int(input("dame el N3: "))
n4=int(input("dame el N4: "))
def prrrrrrrrrrrroducto( n1, n2, n3, n4):
    mayorPrrrrrrrrrrrroducto=0
    for i in (n2,n3,n4):
        prrrrrrrrrrrroducto = n1 * i
        if (prrrrrrrrrrrroducto > mayorPrrrrrrrrrrrroducto):
            mayorPrrrrrrrrrrrroducto = prrrrrrrrrrrroducto
    for i in (n3,n4):
        prrrrrrrrrrrroducto = n2 * i
        if (prrrrrrrrrrrroducto > mayorPrrrrrrrrrrrroducto):
            mayorprrrrrrrrrrrroducto = prrrrrrrrrrrroducto
            '''aca lo q digo es que si el promedio que hiciste recien es mayor que lo que antes 
            considerabas mejor promedio entonces este es el nuevo mayor jaja salu2'''
    prrrrrrrrrrrroducto = n3 * n4
    if (prrrrrrrrrrrroducto > mayorPrrrrrrrrrrrroducto):
            mayorprrrrrrrrrrrroducto = prrrrrrrrrrrroducto
            return f"el mayor producto es: {mayorprrrrrrrrrrrroducto}"
print(prrrrrrrrrrrroducto( n1, n2, n3, n4))