# F = 9/5 C + 32
fafaren_algo = 1
celcius = 0
# profe porfa no me desapruebes :(

def rep():
    for numero in range(0, 13):
        fafaren_algo = numero * 10

        print(faC(fafaren_algo))


def faC(fafaren_algo):
    celcius = (fafaren_algo - 32) * 5 / 9
    return f"aca esta {fafaren_algo} en celsius: {celcius}"


rep()
