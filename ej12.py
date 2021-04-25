import time
from time import sleep
palabra = input("meteme una palabrita: ")
cuantashay = 0
for letrita in palabra.upper():
    if letrita in "AEIOU":
        cuantashay += 1
        print(f"cuento...{cuantashay}")
        time.sleep(1)

print(f"la palabra que me diste, osea {palabra.lower()}, tiene {cuantashay} vocales ")