
def Añobisiesto( año ):
    if (año % 4 == 0 and año % 100 != 0 or año % 400 == 0):
        return("si paaaaaaa es año bisiesto, hay q celebrar en el caso que vos quieras que sea bisiesto, si no querias que sea bisisesto entonces mal ahi bro")
    else:
        return("nooooooo paaaaa, no es año bisiesto mal ahi a menos que hayas querido que no sea año bisiesto ahi bieeeeeeeen ahi paaaaaa hay q celebrar")
print(añobisiesto(int(input("dame el año: "))))