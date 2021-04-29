dia = int(input("ingresar el dia, en numeros por supuesto: "))
mes = int(input("ingresar el mes, en numeros por supuesto: "))
ano = int(input("ingresar el ano, en numeros por supuesto, osea no me pongas dosmil veintiuno, ni que estemos en "
                "colegio catolico que tengamos que escribir tan formal: "))
invalido = int(input("si pones mes, dia, ano escribe 1, si pone dia, mes, año pon 2:"))

# profe porfa no me desapruebes :(
def esValidaLaCosaONoSignoDePregunta(dia, mes, ano, invalido):
    if invalido > 2:
        print("ah vos te crees gracioso no?, ahora no vas a poder usar nuestro programa por comico")
        return None
    """ aca por gracioso no le pienso mandar nada """
    if invalido == 1:
        print("lo sentimos, pero nuestro programa no funciona en invalidos, vuelva pronto!")
        """sos un invalido si usas mes, dia, año y por eso no quiero que use el programa"""
    else:
        if 31 >= dia > 0:
            if 0 < mes <= 12:
                return print("emmm se, esto es una fecha, osea tenes el dia y despues el mes y esas cosas")
            else:
                return print("che, como que esto no es una fecha, estas enfermo de la cabeza vos?")
        else:
            return print("che, como que esto no es una fecha, estas enfermo de la cabeza vos?")


print(esValidaLaCosaONoSignoDePregunta(dia, mes, ano, invalido))
