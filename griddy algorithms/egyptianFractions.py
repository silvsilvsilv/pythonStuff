#Egyptian Fractions

from math import ceil

def egyptianFractions(n:int, d:int):

    list = []

    while n != 0:
        x = ceil(d/n)
        list.append(x)
        
        n = x * n - d
        d = d * x
        
    for i in range(len(list)):
        print(f"1/{list[i]} {'+' if i != len(list) - 1 else ''}", end=" ")
        

def main():
    
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

main()