from toBinary import toBinaryProcess as toBinaryProcess
from toDecimal import toDecimalProcess as toDecimalProcess
from toOctal import toOctalProcess as toOctalProcess
from toHex import toHexProcess as toHexProcess
from numberConversion import numberConversion as numberConversion

import NUMBER 

if __name__ == "__main__":
    print("[1] Decimal\n[2] Binary\n[3] Octal\n[4] Hexadecimal\n")
    convert = int(input("What type of number to convert? "))
    
    toConvert = str(input("What number to convert? "))

    x = str(toConvert)

    match convert:
        case 1:
            #x = x
            x = "Decimal"
        case 2:
            # x = "0b" + x
            x = "Binary"
        case 3:
            # x = "0o" + x
            x = "Octal"
        case 4:
            # x = "0x" + x
            x = "Hex"
        case _:
            print("Invalid!")
    
    print("\n[1] Decimal\n[2] Binary\n[3] Octal\n[4] Hexadecimal")
    convertTo = int(input("Convert to what? "))
    print("==============",end='\n')

    y = ""
    match convertTo:
        case 1:
            # toDecimalProcess(x)
            y = "Decimal"
        case 2:
            # toBinaryProcess(x)
            y = "Binary"  
        case 3:
            # toOctalProcess(x)
            y = "Octal"
        case 4:
            # toHexProcess(x)
            y = "Hex"
        case _:
            print("Invalid")

    convertionOperation = x + y

    
    match convertionOperation:
        case "DecimalBinary": print(f"\n{toConvert} in binary is {NUMBER.decimal_binary(toConvert)}")
        case "DecimalOctal": print(f"\n{toConvert} in octal is {NUMBER.decimal_octal(toConvert)}")
        case "DecimalHex": print(f"\n{toConvert} in hex is {NUMBER.decimal_hexa(toConvert)}")
        case "BinaryDecimal": print(f"\n{toConvert} in decimal is {NUMBER.binary_decimal(toConvert)}")
        case "BinaryOctal": print(f"\n{toConvert} in octal is {NUMBER.binary_octal(toConvert)}")
        case "BinaryHex": print(f"\n{toConvert} in hexadecimal is {NUMBER.binary_hex(toConvert)}")
        case "OctalDecimal":print(f"\n{toConvert} in decimal is {NUMBER.octal_decimal(toConvert)}")
        case "OctalBinary": print(f"\n{toConvert} in binary is {NUMBER.octal_binary(toConvert)}")
        case "OctalHex": print(f"\n{toConvert} to hex is {NUMBER.octal_hex(toConvert)}")
        case "HexDecimal": print(f"\n{toConvert} to decimal is {NUMBER.hex_decimal(toConvert)}")
        case "HexBinary": print(f"\n{toConvert} to binary is {NUMBER.hex_binary(toConvert)}")
        case "HexOctal": print(f"\n{toConvert} to octal is {NUMBER.hex_octal(toConvert)}")
