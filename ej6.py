numerito1 = int(input("dame el Numero 1: "))
numerito2 = int(input("dame el Numero 2: "))
numerito3 = int(input("dame el Numero 3: "))
numerito4 = int(input("dame el Numero 4: "))
 # profe porfa no me desapruebes :(

def producto(numerito1, numerito2, numerito3, numerito4):
    mayorProducto = -10000000
    for i in (numerito2, numerito3, numerito4):
        producto = numerito1 * i
        if (producto > mayorProducto):
            mayorProducto = producto

    for i in (numerito3, numerito4):
        producto = numerito2 * i
        if (producto > mayorProducto):
            mayorProducto = producto

            """ aca lo q digo es que si el promedio que hiciste recien es mayor que lo que antes  considerabas mejor 
            promedio entonces este es el nuevo mayor jaja salu2 """
    producto = numerito3 * numerito4
    if (producto > mayorProducto):
        mayorProducto = producto
    return f"el mayor producto es: {mayorProducto}"


print(producto(numerito1, numerito2, numerito3, numerito4))
