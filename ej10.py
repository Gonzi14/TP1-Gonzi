import random
from random import randrange
x = (random.randrange(50))
""" ponele que "crea" un numero alelatorio"""
print("el numero es entre 0 y 50")
numero = int(input("cual crees que es el numero?"))
while numero != x:
    if numero > x:
        print("el numero es mas chico")
        numero = int(input("cual crees que es el numero?"))
        # profe porfa no me desapruebes :(
    if numero < x:
        print("el numero es mayor")
        numero = int(input("cual crees que es el numero?"))
    elif numero == x:
        print("corrrrrrrrrecto")
        break