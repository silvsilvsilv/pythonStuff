from prettytable import PrettyTable

num = "0o1123" #convert to binary 

n = []
for i in num:
    n.append(i)

table = []
n.reverse()
n = n[:-2]

for i in range(0,len(n)):
    table.append(n[i])
table.reverse()
n.reverse()
                    
print(table) 
table2 = []

ite = len(table) - 1 
while ite >= 0:
    table2.append(f"2^{ite}")
    ite -= 1

table3 = []
for i in range(len(table)):
    x = str(bin(int(table[i])))
    if (int(table[i]) < 8) and (int(table[i]) > 1):
        x = x.replace("o","0")
        table2.append(x)
    elif table[i] == 1:
        x = x.replace("o","00")
        table2.append(x)
    else:
        table2.append(f"{x[2:]}")

for i in range(len(table)):
    x = int(table[i],8)
    o = bin(x)
    o = o[2:]
    table3.append(o)

_table = PrettyTable(table2)
print(table2)
_table.add_row(table)
_table.add_row(table3)
print(_table)