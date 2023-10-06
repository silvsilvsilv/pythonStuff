from fractions import Fraction
from math import fsum, floor, ceil

x = Fraction(5,6)
#6/5 = 1.111 = 2
x -= Fraction(1,2)
# 5/6 - 1/2 = 1/3 
# a - b = c
# c -= a
# x -= Fraction(1,3)

list = [2,3]

i = 0
total = 0
while i < len(list):
    total += (1/list[i])
    i += 1

print(round(total,5) == round((5/6), 5))