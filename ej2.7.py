cateto1 = int(input("dame el primer cateto: "))
cateto2 = int(input("dame el segundo cateto: "))


def loDeLosTriangulitos(cateto1, cateto2):
    hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2))**0.5
    """  es la cuenta matematica para sacar la hipotenusa, no se que queres que te diga """
    return f"aca esta la hipotenusa: {hipotenusa}"
# profe porfa no me desapruebes :(


print(loDeLosTriangulitos(cateto1, cateto2))
