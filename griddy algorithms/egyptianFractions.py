#Egyptian Fractions

from math import ceil, floor, fsum
from fractions import Fraction

def egyptianFractions(n:int, d:int):

    list = []
    # frac = Fraction(n,d) #5/6

    # ! Deprecated, will try new methods (i.e. doesn't fucking work)
    # y = 0
    # x = Fraction(1,ceil(d/n)) #1/2
    # frac -= x #5/6 - 1/2
    # print(x) # 1/2
    # list.append(x)
    # print(f"Frac is {frac}")

    # # while frac != 0:

    # #     # 5/6 - 1/2 - 1/3 = 0
        
    # #     y = Fraction(n,d) - frac 
    # #     frac -= y
    # #     list.append(f"{y}")
    
    #// stolen form geeksforgeeks
    while n != 0:
        x = ceil(d/n)
        list.append(x)

        n = x * n - d
        d = d * x
        
    for i in range(len(list)):
        print(f"1/{list[i]} {'+' if i != len(list) - 1 else ''}", end=" ")
        

if __name__ == "__main__":
    
    n = d = 0

    n = int(input("Numerator? "))

    d = int(input("Denominator? "))


    print(f"{n}/{d} = ",end='')

    if n > 0 and d > 0:
        egyptianFractions(n,d)
    elif n != 0 and d == 0:
        print("Undefined")
    else:
        print("0")

