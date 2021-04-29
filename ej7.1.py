def anobisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
        """Verifica si el numero es exactamente divisible entre 400 para confirmar que sea un ano bisiesto. Si un ano 
        es divisible entre 100, pero no entre 400, entonces "no" es un ano bisiesto. Si un ano es divisible entre 100 
        y 400, entonces "si" es un ano bisiesto. """
        return (
            "si paaaaaaa es ano bisiesto, hay q celebrar en el caso que vos quieras que sea bisiesto, si no querias que"
            " sea bisisesto entonces mal ahi bro")
    # profe porfa no me desapruebes :(
    else:
        return (
            "nooooooo paaaaa, no es ano bisiesto mal ahi a menos que hayas querido que no sea ano bisiesto ahi bieeeeeeeen"
            " ahi paaaaaa hay q celebrar")


print(anobisiesto(int(input("dame el ano: "))))
