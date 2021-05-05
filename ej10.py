import random
from random import randrange

elNumeroRandom = (random.randrange(50))
print(elNumeroRandom)
""" ponele que "crea" un numero alelatorio"""
print("el numero es entre 0 y 50")
numero = int(input("cual crees que es el numero?"))
while numero != elNumeroRandom:
    if numero > elNumeroRandom:
        print("el numero es mas chico")
        numero = int(input("cual crees que es el numero?"))
        # profe porfa no me desapruebes :(
    if numero < elNumeroRandom:
        print("el numero es mayor")
        numero = int(input("cual crees que es el numero?"))
print("corrrrrrrrrecto")
