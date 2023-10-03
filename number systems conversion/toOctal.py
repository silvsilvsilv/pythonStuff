from prettytable import PrettyTable
from numberConversion import strToList as strToList, charToNumber as charToNumber

def toOctal(num:str):

    match num[1]:
        case 'x':
            n = int(num,16)
            return(oct(n))
        case 'b':
            n = int(num,2)
            return(oct(n))
        case 'o':
            return(num)
        case _:
            n = int(num)
            return(oct(n))

def toOctalProcess(num:str):
    n = strToList(num)
    p = "Octal"
    
    match n[1]:
        case 'x':
            p = "Hex"
        case 'o':
            p = "Octal"
        case 'b':
            p = "Binary"
        case _:
            p = "Decimal"
    
    print(f"Showing process for {p} to Octal conversion")
    print(f"Converting {num}")
    
    if p != "Octal":

        match p:
            case "Decimal":
                table1 = PrettyTable(["Division by 8","Quotient","Remainder", "Bit #"])
                x = int(num)
                l = []
                bit = 0
                while x > 0:
                    table1.add_row([f"({x}/8)",f"{x//8}",f"{x%8}",f"{bit}"])
                    l.append(x%8)
                    x = x // 8
                    bit += 1
                print(table1)

            case "Binary":
                table1 = []
                n.reverse()
                n = n[:-2]
                __table = []
                for i in range(0,len(n),3):
                    x = n[i:i+3]
                    x.reverse()
                    __table.append(x)
                    table1.append(''.join(x))
                table1.reverse()
                n.reverse()
                
                table2 = []
                
                ite = len(__table) - 1
                while ite >= 0:
                    table2.append(f"8^{ite}")
                    ite -= 1
                
                table3 = []

                for i in range(len(table1)):
                    x = int(table1[i],2)
                    o = oct(x)
                    o = o[2:]
                    table3.append(o)
                
                _table = PrettyTable(table2)
                _table.add_row(table1)
                _table.add_row(table3)
                print(_table)
            
            case "Hex":
                __ = [] #tf is variable names amirite
                for i in n:
                    __.append(charToNumber(i))
                table = []
                for i in range(2,len(n),1):
                    table.append(n[i])
                table2 = []
                for i in range(2,len(n),1):
                    x = str(bin(int(__[i])))
                    if (int(__[i]) < 9) and (int(__[i]) > 1):
                        x = x.replace("b","00")
                        table2.append(f"{x[1:]}")
                    elif (int(__[i]) == 1):
                        x = x.replace("b","000")
                        table2.append(f"{x[1:]}")
                    else:
                        table2.append(f"{x[2:]}")
                
                table = PrettyTable(table)
                table.add_row(table2)
                print(table)

        print(f'\n{num} converted is {toOctal(num)}', end="\n")   
    else:
        print(f"{num} is already a Octal Number!", end="\n")

if __name__ == "__main__":
    print(f"Binary to Octal\n")
    toOctalProcess("0b10010110") # 226
    
    print(f"Decimal to Octal\n")
    toOctalProcess("123")# 173
    
    print(f"Hex to Octal\n")
    toOctalProcess("0x123")# 443