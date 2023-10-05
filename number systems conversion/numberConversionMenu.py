from toBinary import toBinaryProcess as toBinaryProcess
from toDecimal import toDecimalProcess as toDecimalProcess
from toOctal import toOctalProcess as toOctalProcess
from toHex import toHexProcess as toHexProcess


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
        case 2:
            toBinaryProcess(x)  
        case 3:
            toOctalProcess(x)
        case 4:
            toHexProcess(x)
        case _:
            print("Invalid")