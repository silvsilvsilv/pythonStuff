from prettytable import PrettyTable
from numberConversion import strToList as strToList, charToNumber as charToNumber
from toBinary import toBinaryProcess as toBinaryProcess, toBinary as toBinary

def numberToChar(x:int):
    
    if isinstance(x,int):
        match x:
            case 10:
                return 'a'
            case 11:
                return 'b'
            case 12:
                return 'c'
            case 13:
                return 'd'
            case 14:
                return 'e'
            case 15:
                return 'f'

    return x

def toHex(num:str):
    
    match num[1]:
        case 'o':
            n = int(num,8)
            return(hex(n))
        case 'b':
            n = int(num,2)
            return(hex(n))
        case 'x':
            return(num)
        case _:
            n = int(num)
            return(hex(n))
        
def toHexProcess(num:str):
    n = strToList(num)
    p = "Hex"
    
    match n[1]:
        case 'x':
            p = "Hex"
        case 'o':
            p = "Octal"
        case 'b':
            p = "Binary"
        case _:
            p = "Decimal"
    
    print(f"Showing process for {p} to Hex conversion")
    print(f"Converting {num}")
    
    if p != "Hex":

        match p:
            case "Decimal":
                table = PrettyTable(["Division by 16","Quotient","Remainder", "Bit #"])
                x = int(num)
                l = []
                bit = 0
                while x > 0:
                    table.add_row([f"({x}/16)",f"{x//16}",f"{numberToChar(x%16)}",f"{bit}"])
                    l.append(x%16)
                    x = x // 16
                    bit += 1
                print(table)

            case "Binary":
                table = []
                n.reverse()
                n = n[:-2]
                __table = []
                for i in range(0,len(n),4):
                    x = n[i:i+4]
                    x.reverse()
                    
                    while len(x) < 4:
                        x.insert(0,"0")
                    
                    __table.append(x)
                    table.append(''.join(x))
                table.reverse()
                n.reverse()
                
                table2 = []
                
                ite = len(__table) - 1
                while ite >= 0:
                    table2.append(f"16^{ite}")
                    ite -= 1
                
                table3 = []

                for i in range(len(table)):
                    x = int(table[i],2)
                    o = hex(x)
                    o = o[2:]
                    
                    table3.append(o)
 
                _table = PrettyTable(table2)
                _table.add_row(table)
                _table.add_row(table3)
                print(_table)
            
            case "Octal":
                print(f"\nTo convert to Hexa we must first convert to Binary\n")
                toBinaryProcess(num)
                print(f"\nAnd then we convert to Hex\n")
                toHexProcess(toBinary(num))
                
        print(f'\n{num} converted is {toHex(num)}', end="\n")   
    else:
        print(f"{num} is already a Hex Number!", end="\n")

if __name__ == "__main__":
    print(f"Binary to Hex\n")
    toHexProcess("0b1010011") # Ox96
    
    print(f"Decimal to Hex\n")
    toHexProcess("123")# 7b
    
    print(f"Octal to Hex\n")
    toHexProcess("0o123")# 53