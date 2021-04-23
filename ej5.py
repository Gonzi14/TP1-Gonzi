#F = 9/5 C + 32
fafaren_algo = 1
celcius=0
def Rep():
    for numero in range(0 , 13):
        fafaren_algo = numero * 10
        
        print(FaC(fafaren_algo))
         
def FaC(fafaren_algo):
    celcius = (fafaren_algo - 32 )* 5/9
    return f"aca esta {fafaren_algo} en celsius: {celcius}"


Rep()