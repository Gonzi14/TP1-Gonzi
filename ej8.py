diccionario = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
               (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def roma(numero, diccionarioromano):
    anoromano = ""

    while numero > 0:
        for lsNumeros, lsLetras in diccionario:
            while numero >= lsNumeros:
                # profe porfa no me desapruebes :(
                anoromano = anoromano + lsLetras
                numero = numero - lsNumeros
        return anoromano


print(roma(int(input("escribime el año que queres pasar: ")), diccionario))
