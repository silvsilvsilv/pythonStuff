from numberConversion import charToNumber as charToNumber

#TODO: add user input
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
    
    e = "0x123af"
    f = "0xf"

    #addition
    print(hex(int(e,16) + int(f,16)))

    #subtraction
    print(hex(int(e,16) - int(f,16)))

    #multiplication
    print(hex(int(e,16) * int(f,16)))

    #division
    # * now added remainder

    print(f"{hex(int(e,16) // int(f,16))} {'r: '+ (hex(int(e,16) % int(f,16))[2:]) if int(e,16) % int(f,16) != 0 else ' ' }")


    