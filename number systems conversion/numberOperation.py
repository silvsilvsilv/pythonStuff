


if __name__ == "__main__":
    
    # * binary
    
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


    