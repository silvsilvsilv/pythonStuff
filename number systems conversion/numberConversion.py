from prettytable import PrettyTable

def strToList(x:str):
    list = []
    
    for i in range(len(x)):
        list.append(x[i])
    
    return list

def toDecimal(num:str):

    if len(num) != 1:
        match num[1]:
            case 'o':
                return(int(num,8))
            case 'x':
                return(int(num,16))
            case 'b':
                return(int(num,2))
            case _:
                return(num)
    else:
        return(num)

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

def toDecimalProcess(num:str):

    n = strToList(num)
    p = "Decimal"

    if len(n) != 1:
        match n[1]:
            case 'x':
                p = "Hex"
            case 'b':
                p = "Binary"
            case 'o':
                p = "Octal"
    else:
        p = "Decimal"
    
    print(f"Showing process for {p} to Decimal conversion")
    print(f"Converting {num}")
    print(f"{num} = ",end='')

    r = 10
    n.reverse()
    match p:
        case "Hex":
            n = n[:len(n)-2]
            r = 16
        case "Binary":
            n = n[:len(n)-2]
            r = 2
        case "Octal":
            n = n[:len(n)-2]
            r = 8
    
    if p != "Decimal":
        for i in range(len(n)-1,-1,-1):
            print(f"({n[i]} * {r}^{i}) {'+' if i != 0 else ''}",end="")
    else:
        for i in range(len(n)- 1,-1,-1):
            print(f"({n[i]} * 10^{i}) {'+' if i != 0 else ''}", end=" ")
            # print(i)
    
    print(f'\n{num} converted is ', end="")

def charToNumber(x:str):

    if isinstance(x,str):
        match x:
            case "a":
                return 10
            case "b":
                return 11
            case "c":
                return 12
            case "d":
                return 13
            case "e":
                return 14
            case "f":
                return 15
    
    return x
          
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
                table = []
                n.reverse()
                n = n[:-2]
                __table = []
                for i in range(0,len(n),3):
                    x = n[i:i+3]
                    x.reverse()
                    __table.append(x)
                    table.append(''.join(x))
                table.reverse()
                n.reverse()
                    
                print(table) 
                table2 = []

                ite = len(__table) - 1 
                while ite >= 0:
                    table2.append(f"2^{ite}")
                    ite -= 1

                table3 = []

                for i in range(len(table)):
                    x = int(table[i],2)
                    o = oct(x)
                    o = o[2:]
                    table3.append(o)

                _table = PrettyTable(table2)
                print(table2)
                _table.add_row(table)
                _table.add_row(table3)
                print(_table)
            
            case "Hex":
                __ = [] #tf is variable names amirite
                for i in n:
                    __.append(charToNumber(i))
                table = []
                for i in range(2,len(n),1):
                    table.append(n[i])
                
                print(table) 
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
        
        print(f'\n{num} converted is ', end="")   
    else:
        print(f"{num} is already a Binary Number!", end="\n")

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

        print(f'\n{num} converted is ', end="")   
    else:
        print(f"{num} is already a Octal Number!", end="\n")

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
                    table.add_row([f"({x}/16)",f"{x//16}",f"{x % 16}",f"{bit}"])
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
                    o = oct(x)
                    o = o[2:]
                    table3.append(o)
                
                _table = PrettyTable(table2)
                _table.add_row(table)
                _table.add_row(table3)
                print(_table)
            
            case "Oct":
                print(f"Decimal equivalent is: {toDecimal(num)}")
                toOctalProcess(str(toDecimal(num)))

        
        print(f'\n{num} converted is ', end="")   
    else:
        print(f"{num} is already a Hex Number!", end="\n")

if __name__ == "__main__":
    print("[1] Decimal\n[2] Binary\n[3] Octal\n[4] Hexadecimal\n")
    convert = int(input("What type of number to convert? "))
    
    toConvert = str(input("What number to convert? "))

    x = str(toConvert)

    match convert:
        case 1:
            x = x
        case 2:
            x = "0b" + x
        case 3:
            x = "0o" + x
        case 4:
            x = "0x" + x
        case _:
            print("Invalid!")
    
    print("\n[1] Decimal\n[2] Binary\n[3] Octal\n[4] Hexadecimal")
    convertTo = int(input("Convert to what? "))
    print("==============",end='\n')

    match convertTo:
        case 1:
            toDecimalProcess(x)
            print(toDecimal(x))
        case 2:
            toBinaryProcess(x)
            print(toBinary(x))
        case 3:
            toOctalProcess(x)
            print(toOctal(x))
        case 4:
            toHexProcess(x)
            print(toHex(x))
        case _:
            print("Invalid")