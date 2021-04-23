#F = 9/5 C + 32
fafaren_algo = int(input("dame los farenheit: "))
celcius=0
def FaC(fafaren_algo):
    celcius = (fafaren_algo - 32 )* 5/9
    return f"aca esta la misma temperatura en celsius: {celcius}"
print(FaC(fafaren_algo))