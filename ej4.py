'''F = 9/5 C + 32'''
f = int(input("dame los farenheit: "))
c=0
def FaC(f):
    c = (f - 32 )* 5/9
    return f"aca esta la misma temperatura en celsius: {c}"
print(FaC(f))