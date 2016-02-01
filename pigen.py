from decimal import *

def piGen(digit):
    pi = Decimal('0')
    for n in range(0, digit):
        
        part1 = Decimal((-1)**n) / (2**(10*n))
        part2 = Decimal(-(2**5)/(4*n + 1))
        part3 = Decimal(1/(4*n +3))
        part4 = Decimal(2**8 /(10*n + 1))
        part5 = Decimal(2**6/(10*n + 3))
        part6 = Decimal(2**2/(10*n + 5))
        part7 = Decimal(2**2/(10*n + 7))
        part8 = Decimal(1/(10*n + 9))
        pi += part1 * (part2 - part3 + part4 - part5 - part6 - part7 + part8)
        
    piRounded = Decimal(1/2**6) * pi
    return piRounded     
