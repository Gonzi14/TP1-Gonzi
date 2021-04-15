'''F = 9/5 C + 32'''
f = 1
c=0
def Rep():
    for numero in range(0 , 13):
        f = numero * 10
        
        print(FaC(f))
         
def FaC(f):
    c = (f - 32 )* 5/9
    return f"aca esta {f} en celsius: {c}"


Rep()