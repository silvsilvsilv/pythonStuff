import NUMBER
#Number Operation
def addition(num1:str,num2:str, opType:str):
    try:
        match opType:
            case "Binary": print(bin(int(num1,2) + int(num2,2))[2:])
            case "Octal": print(oct(int(num1,8) + int(num2,8))[2:])
            case "Hex": print(hex(int(num1,16) + int(num2,16))[2:])
            case "Decimal": print(int(num1) + int(num2))
    except:
        print(f"Not a {opType} number!\n"); numberOperation()

def subtraction(num1:str, num2:str, opType:str):
    try:
        match opType:
            case "Binary": print(bin(int(num1,2) - int(num2,2))[2:])
            case "Octal": print(oct(int(num1,8) - int(num2,8))[2:])
            case "Hex": print(hex(int(num1,16) - int(num2,16))[2:])
            case "Decimal": print(int(num1) - int(num2))
    except:
        print(f"Not a {opType} number!\n"); numberOperation()

def multiplication(num1:str, num2:str, opType:str):
    try:
        match opType:
            case "Binary": print(bin(int(num1,2) * int(num2,2))[2:])
            case "Octal": print(oct(int(num1,8) * int(num2,8))[2:])
            case "Hex": print(hex(int(num1,16) * int(num2,16))[2:])
            case "Decimal": print(int(num1) * int(num2))
    except:
        print(f"Not a {opType} number!\n"); numberOperation()

def division(num1:str, num2:str, opType:str):
    try:
        match opType:
            case "Binary": print(f"{bin(int(num1,2) // int(num2,2))[2:]} {'r: ' + str(int(num1,2) % int(num2,2)) if int(num1,2) % int(num2,2) != 0 else ''}")
            case "Octal": print(f"{oct(int(num1,8) // int(num2,8))[2:]} {'r: ' + str(oct(int(num1,8) % int(num2,8)))[2:] if int(num1,8) % int(num2,8) != 0 else ''}")
            case "Hex": print(f"{hex(int(num1,16) // int(num2,16))[2:]} {'r: ' + str(hex(int(num1,16) % int(num2,16)))[2:] if int(num1,16) % int(num2,16) != 0 else ''}")
            case "Decimal": print(f"{int(num1) // int(num2)} {'r: ' + str(int(num1) % int(num2)) if int(num1) % int(num2) != 0 else ''}")
    except:
        print(f"Not a {opType} number!\n"); numberOperation()

def numberOperation():

    choice = 0
    opType = "Binary"

    num1 = num2 = op = ""
    print("===Number operation===\n\nPlease separate numbers with a space")
    print("[1] Binary Operation\n[2] Octal Operation\n[3] Hexadecimal Operation\n")
    choice = int(input("What choice? "))

    match choice:
        case 1: opType = "Binary"
        case 2: opType = "Octal"
        case 3: opType = "Hex"
        # case 4: opType = "Decimal"
        case _: print("Invalid!\n\n"); numberOperation()

    # num1 = str(input(f"Enter a {opType} number: "))
    # op = str(input("What operation? "))
    # num2 = str(input(f"Enter a {opType} number: "))
    print("Input operation: ")
    op = str(input(""))
    
    match opType:
        case "Binary": 
            if(op == '+'):
                NUMBER.AddBinary()
            elif(op=='-'):
                NUMBER.SubBin()
            elif(op=='*'):
                NUMBER.MultBin()
            elif(op=='/'):
                NUMBER.DivBin()
        case "Octal":
            if(op == '+'):
                NUMBER.AddOctal()
            elif(op=='-'):
                NUMBER.SubOctal()
            elif(op=='*'):
                NUMBER.MultOctal()
            elif(op=='/'):
                NUMBER.DivOctal()
        case "Hex":
            if(op == '+'):
                NUMBER.AddHexa()
            elif(op=='-'):
                NUMBER.SubHexa()
            elif(op=='*'):
                NUMBER.MultHexa()
            elif(op=='/'):
                NUMBER.DivHexa()



def a():
    
    # * binary
    print("Binary")
    # addition
    a = "1101"
    b = "100"
    print(bin(int(a,2) + int(b,2)))

    # subtration
    print(bin(int(a,2) - int(b,2)))

    # multiplication
    print(bin(int(a,2) * int(b,2)))

    # division
    # * now added remainder
    print(f"{bin(int(a,2) // int(b,2))} {'r: ' + (bin(int(a,2) % int(b,2))[2:]) if int(a,2) % int(b,2) != 0 else ' '}")

    # * octal
    c = "123"
    d = "12"
    print("\nOctal")
    #addition
    print(oct(int(c,8) + int(d,8)))

    #subtraction
    print(oct(int(c,8) - int(d,8)))

    #multiplication
    print(oct(int(c,8) * int(d,8)))

    #division
    # * now added remainder
    print(f"{oct(int(c,8) // int(d,8))} {'r: '+(oct(int(c,8) % int(d,8))[2:]) if int(c,8) % int(d,8) != 0 else ' '}")

    # * Hex
    print("\nHex")
    
    e = "123af"
    f = "f"

    #addition
    print(hex(int(e,16) + int(f,16)))

    #subtraction
    print(hex(int(e,16) - int(f,16)))

    #multiplication
    print(hex(int(e,16) * int(f,16)))

    #division
    # * now added remainder

    print(f"{hex(int(e,16) // int(f,16))} {'r: '+ (hex(int(e,16) % int(f,16))[2:]) if int(e,16) % int(f,16) != 0 else ' ' }")

try:
    while True:
        numberOperation()
except:
    print("\nQuitting program")