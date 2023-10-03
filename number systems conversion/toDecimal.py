from numberConversion import strToList as strToList

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
    
    print(f'\n{num} converted is {toDecimal(num)}', end="\n")


if __name__ == "__main__":
    print(f"Binary to Decimal\n")
    toDecimalProcess("0b10010110") # 150
    
    print(f"Octal to Decimal\n")
    toDecimalProcess("0o123")# 83
    
    print(f"Hex to Decimal\n")
    toDecimalProcess("0x123")# 291