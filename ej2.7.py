c1=int(input("dame el primer cateto: "))
c2=int(input("dame el segundo cateto: "))
from math import sqrt
def PerCir(c1,c2):
    H=sqrt((c1**2)+(c2**2))
    '''es la cuenta matematica para sacar la hipotenusa, no se que queres que te diga'''
    return f"aca esta la hipotenusa: {H}"
print(PerCir(c1,c2))