from numberConversion import charToNumber as charToNumber


if __name__ == "__main__":
    
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
    # ! This does not account for after the decimal value (i.e. 1101 / 100 is actually 11.01 but only outputs 11)
    print(bin(int(a,2) // int(b,2)))

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
    # ! Does not account for the numbers after the decimal point
    print(oct(int(c,8) // int(d,8)))

    # * Hex
    print("\nHex")
    
    e = "0x123af"
    f = "0xf"

    #addition
    print(hex(int(e,16) + int(f,16)))

    #subtraction
    print(hex(int(e,16) - int(f,16)))

    #multiplication
    print(hex(int(e,16) * int(f,16)))

    #division
    print(hex(int(e,16) // int(f,16)))


    