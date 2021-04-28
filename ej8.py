diccionario = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
               (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def Roma(numero, diccionarioromano):
    añoromano = ""

    while numero > 0:
        for lsNumeros, lsLetras in diccionario:
            while numero >= lsNumeros:
                añoromano = añoromano + lsLetras
                numero = numero - lsNumeros
        return añoromano


print(Roma(int(input("escribime el año que queres pasar: ")), diccionario))
