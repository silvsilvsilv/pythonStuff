from prettytable import PrettyTable
from numberConversion import strToList as strToList, charToNumber as charToNumber
# * split into separate files for own sanity

def toBinary(num:str):

    match num[1]:
        case 'o':
            n = int(num,8)
            return(bin(n))
        case 'x':
            n = int(num,16)
            return(bin(n))
        case 'b':
            return(num)
        case _:
            n = int(num)
            return(bin(n))

def toBinaryProcess(num:str):
    
    n = strToList(num)
    p = "Binary"
    
    match n[1]:
        case 'x':
            p = "Hex"
        case 'o':
            p = "Octal"
        case 'b':
            p = "Binary"
        case _:
            p = "Decimal"
    
    print(f"Showing process for {p} to Binary conversion")
    print(f"Converting {num}")
    
    if p != "Binary":

        match p:
            case "Decimal":
                table = PrettyTable(["Division by 2","Quotient","Remainder", "Bit #"])
                x = int(num)
                l = []
                bit = 0
                while x > 0:
                    table.add_row([f"({x}/2)",f"{x//2}",f"{x%2}",f"{bit}"])
                    l.append(x%2)
                    x = x // 2
                    bit += 1
                print(table)
            case "Octal":
                __ = [] #tf is variable names amirite
                for i in n:
                    __.append(charToNumber(i))
                table = []
                for i in range(2,len(n),1):
                    table.append(n[i])
                
                table2 = []

                ite = len(table) - 1 
                while ite >= 0:
                    table2.append(f"2^{ite}")
                    ite -= 1

                table2 = []
                for i in range(2,len(n),1):
                    x = str(bin(int(__[i])))
                    if (int(__[i]) < 9) and (int(__[i]) > 1):
                        x = x.replace("b","0")
                        table2.append(f"{x[1:]}")
                    elif (int(__[i]) == 1):
                        x = x.replace("b","00")
                        table2.append(f"{x[1:]}")
                    else:
                        table2.append(f"{x[2:]}")
                
                table = PrettyTable(table)
                table.add_row(table2)
                print(table)
            
            case "Hex":
                __ = [] #tf is variable names amirite
                for i in n:
                    __.append(charToNumber(i))
                table = []
                for i in range(2,len(n),1):
                    table.append(n[i])
                
                table2 = []

                ite = len(table) - 1 
                while ite >= 0:
                    table2.append(f"2^{ite}")
                    ite -= 1

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
        
        print(f'\n{num} converted is {toBinary(num)}', end="\n")   
    else:
        print(f"{num} is already a Binary Number!", end="\n")


if __name__ == "__main__":

    print(f"Decimal to Binary\n")
    toBinaryProcess("123") # 1 111 011
    

    print(f"Octal to Binary\n")
    toBinaryProcess("0o123")# 1 010 011
    

    print(f"Hex to Binary\n")
    toBinaryProcess("0x123")# 0001 0010 0011