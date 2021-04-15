
def añobisiesto( a ):
    if (a % 2 == 0 and a % 400 == 0 and a % 100 != 0):
        return("si paaaaaaa es año bisiesto, hay q celebrar en el caso que vos quieras que sea bisiesto, si no querias que sea bisisesto entonces mal ahi bro")
    else:
        return("nooooooo paaaaa, no es año bisiesto mal ahi a menos que hayas querido que no sea año bisiesto ahi bieeeeeeeen ahi paaaaaa hay q celebrar")
print(añobisiesto(int(input("dame el año: "))))


    