# F = 9/5 C + 32
fafaren_algo = 0
celcius = 0
# profe porfa no me desapruebes :(

def repeticion():
    for numero in range(0, 13):
        fafaren_algo = numero * 10

        print(farenheitACelcius(fafaren_algo))


def farenheitACelcius(fafaren_algo):
    celcius = (fafaren_algo - 32) * 5 / 9
    return f"aca esta {fafaren_algo} en celsius: {str(celcius)[:5]}"
    """aca lo que estoy haciendo es ir mostrando de 0 a 130 farenheit a celcius en forma de lista"""

repeticion()
