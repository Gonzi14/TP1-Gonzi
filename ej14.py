import random
from random import randrange
import time
from time import sleep


def generacionDeNumeros():
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n1 = randrange(10)
    n2 = randrange(10)
    n3 = randrange(10)
    n4 = randrange(10)
    numero = [n1, n2, n3, n4]
    """ creo cuatro numeros del 1 al 10 y los junto en una lista """
    return validacionBase(numero)


def validacionBase(base):
    """print(based)"""
    """ activalo si queres saber el resultado """
    valido = True
    numeroBase0 = None
    numeroBase1 = None
    numeroBase2 = None
    numeroBase3 = None
    for numerito in base:
        if numerito != numeroBase0:
            if numerito == base[0]:
                numeroBase0 = numerito
            if numerito != numeroBase1:
                if numerito == base[1]:
                    numeroBase1 = numerito
                if numerito != numeroBase2:
                    if numerito == base[2]:
                        numeroBase2 = numerito
                    if numerito != numeroBase3:
                        if numerito == base[3]:
                            numeroBase3 = numerito
                    else:
                        valido = False
                else:
                    valido = False
            else:
                valido = False
        else:
            valido = False
    if valido == False:
        """ aca me voy fijando si el numero que esta leyendo, osea numerito es igual a la base, en ese caso voy a hacer
         que sean lo mismo, asi para el proximo numero que pase se compare con el, y cuando pasa el numero 4,
         se habra comparado con los 3 numeros anteriores """
        generacionDeNumeros()
    if valido == True:
        empiezaElJuego(base)


def empiezaElJuego(elNumero):
    termino = False
    while termino == False:
        loQueCreeElUsuario1 = int(input("Cual cree que es el 1er numero?"))
        loQueCreeElUsuario2 = int(input("Cual cree que es el 2do numero?"))
        loQueCreeElUsuario3 = int(input("Cual cree que es el 3er numero?"))
        loQueCreeElUsuario4 = int(input("Cual cree que es el 4to numero?"))
        loQueCreeElUsuarioLista = ([loQueCreeElUsuario1, loQueCreeElUsuario2, loQueCreeElUsuario3, loQueCreeElUsuario4])
        """print(loQueCreeElUsuarioLista)"""
        """ aca creo una lista de acuerdo a los 4 numeros que puso el usuario, para asi poder compararlo con la lista
         que es el resultado correcto """
        if loQueCreeElUsuarioLista == elNumero:
            print("su respuesta es.")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print("CORRECTA!!!!!")
            time.sleep(0.5)
            print("Felicitaciones!!!")
            print("Has ganado el juego.")
            termino = True
        else:
            print("su respuesta es.")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print("incorrecta, siga intentando")
            coincidencias = 0
            aciertos = 0
            # profe porfa no me desapruebes :(
            for i in range(1, 5):
                if loQueCreeElUsuarioLista[i - 1:i] == elNumero[i - 1:i]:
                    aciertos += 1
            for i in range(1, 5):
                if loQueCreeElUsuarioLista[i - 1] == elNumero[0] or loQueCreeElUsuarioLista[i - 1] == elNumero[1] or \
                        loQueCreeElUsuarioLista[i - 1] == elNumero[2] or loQueCreeElUsuarioLista[i - 1] == elNumero[3]:
                    coincidencias += 1
            coincidencias = coincidencias - aciertos
            """ lo que tiene esto es que un acierto lo toma como una coincidencia, asi que saco los aciertos de las
             verdaderas coincidencias.Esto pasa porque se fija si uno de los numeros que puso el usuario es igual a
             CUALQUIERA de los 4 verdaderos, de esta manera si el juego tiene que un 4 esta en la posicion 3 y el
             usuario puso 4 3n la posicion 3, igual asi la maquina que cuenta coincidencias lo toma como una """
            print(f"tuviste {aciertos} aciertos y {coincidencias} coincidencias")


if 0 == 0:
    generacionDeNumeros()

# galo y manu me ayudaron con partes muy especificas de este ejercicio
