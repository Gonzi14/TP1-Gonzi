import time
from time import sleep
palabra = input("meteme una palabrita: ")
palabraENMAYUSCULAS = input("meteme la palabra que me diste recien PERO EN MAYUSCULAS: ")
palabra1 = palabra.upper()
if palabra1 == palabraENMAYUSCULAS:
    print("TRUE")
else:
    print("...")
    time.sleep(2)
    print("no es lo que te pedi")


