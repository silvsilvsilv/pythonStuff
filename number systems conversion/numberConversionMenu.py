from toBinary import toBinaryProcess as toBinaryProcess
from toDecimal import toDecimalProcess as toDecimalProcess
from toOctal import toOctalProcess as toOctalProcess
from toHex import toHexProcess as toHexProcess
from numberConversion import numberConversion as numberConversion

if __name__ == "__main__":
    print("[1] Decimal\n[2] Binary\n[3] Octal\n[4] Hexadecimal\n")
    convert = int(input("What type of number to convert? "))
    
    toConvert = str(input("What number to convert? "))

    x = str(toConvert)

    numberConversion(x,convert)
    
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