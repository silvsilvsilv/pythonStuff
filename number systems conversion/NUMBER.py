import math
import decimal

decimal.getcontext().prec = 50


def decimal_binary(number):
    number = decimal.Decimal(number)
    integer = int(number)
    fraction = number - integer

    int_binary = bin(integer)[2:]

    frac_bin = ""
    for _ in range(8):
        fraction *= decimal.Decimal(2)
        frac_digit = int(fraction)
        frac_bin += str(bin(frac_digit))[2:]
        fraction -= decimal.Decimal(frac_digit)

    binary_num = int_binary + "." + frac_bin

    return binary_num


def decimal_octal(number):
    number = decimal.Decimal(number)
    integer = int(number)
    fraction = number - integer

    int_octal = oct(integer)[2:]

    frac_oc = ""

    for _ in range(4):  # Assuming a maximum of 5 fractional digits for octal
        fraction *= 8
        frac_digit = int(fraction)
        frac_oc += str(frac_digit)
        fraction -= frac_digit

    octal_num = int_octal + "." + frac_oc

    return octal_num


def decimal_hexa(number):
    number = decimal.Decimal(number)
    integer = int(number)
    fraction = number - integer

    int_hexa = hex(integer)[2:].upper()
    frac_hexa = ""

    for _ in range(4):  # Assuming a maximum of 13 fractional digits for hexadecimal
        fraction *= decimal.Decimal(16)
        frac_digit = int(fraction)
        frac_hexa += str(hex(frac_digit))[2:].upper()
        fraction -= decimal.Decimal(frac_digit)

    hex_num = int_hexa + "." + frac_hexa

    return hex_num


def binary_decimal(number):
    if "." in number:
        int_part, frac_part = number.split(".")
    else:
        int_part = number
        frac_part = "0"

    int_decimal = int(int_part, 2)

    frac_decimal = decimal.Decimal("0.0")
    for i, bit in enumerate(frac_part):
        frac_decimal += decimal.Decimal(int(bit)) * (decimal.Decimal(2) ** -(i + 1))

    decimal_num = int_decimal + frac_decimal

    return decimal_num


def binary_octal(number):
    decimal_num = binary_decimal(number)
    octal_num = decimal_octal(decimal_num)
    return octal_num


def binary_hex(number):
    decimal_num = binary_decimal(number)
    hex_num = decimal_hexa(decimal_num)
    return hex_num


def octal_decimal(number):
    if "." in number:
        int_part, frac_part = number.split(".")
    else:
        int_part = number
        frac_part = "0"

    int_decimal = int(int_part, 8)

    frac_decimal = 0.0
    for i, digit in enumerate(frac_part):
        frac_decimal += int(digit) * (8 ** -(i + 1))

    decimal_num = int_decimal + frac_decimal

    return decimal_num


def octal_binary(number):
    decimal_num = octal_decimal(number)
    binary_num = decimal_binary(decimal_num)
    return binary_num


def octal_hex(number):
    decimal_num = octal_decimal(number)
    hex_num = decimal_hexa(decimal_num)
    return hex_num


def hex_decimal(hex_num):
    if "." in hex_num:
        int_part, frac_part = hex_num.split(".")
    else:
        int_part = hex_num
        frac_part = "0"

    int_decimal = int(int_part, 16)

    frac_decimal = decimal.Decimal("0.0")
    for i, digit in enumerate(frac_part):
        frac_decimal += decimal.Decimal(int(digit, 16)) * (
            decimal.Decimal(16) ** -(i + 1)
        )

    decimal_num = int_decimal + frac_decimal

    return decimal_num


def hex_binary(hex_num):
    decimal_num = hex_decimal(hex_num)
    binary_num = decimal_binary(decimal_num)
    return binary_num


def hex_octal(hex_num):
    decimal_num = hex_decimal(hex_num)
    octal_num = decimal_octal(decimal_num)
    return octal_num


def AddBinary():
    Array = []

    while True:
        choice = input("Enter a binary number or press 'X' to solve: ")

        if ( (choice == "X") or (choice == 'x') ):
            break
        else:
            Array.append(binary_decimal(choice))

    sum = 0
    for x in Array:
        sum += x

    print("The sum of: ")
    for x in Array:
        print("%15s" % (decimal_binary(x)))

    print("------------------")
    print("%15s" % (decimal_binary(sum)))


def AddOctal():
    Array = []

    while True:
        choice = input("Enter an octal number or press 'X' to solve: ")

        if ( (choice == "X") or (choice == 'x') ):
            break
        else:
            Array.append(octal_decimal(choice))

    sum = 0
    for x in Array:
        sum += x

    print("The sum of: ")
    for x in Array:
        print(decimal_octal(x))

    print("------------")
    print(decimal_octal(sum))


def AddHexa():
    Array = []

    while True:
        choice = input("Enter a hexadecimal number or press 'X' to solve: ")

        if ( (choice == "X") or (choice == 'x') ):
            break
        else:
            Array.append(hex_decimal(choice))

    sum = 0
    for x in Array:
        sum += x

    print("The sum of: ")
    for x in Array:
        print(decimal_hexa(x))

    print("------------")
    print(decimal_hexa(sum))


def SubBin():
    minuend = input("Enter binary minuend: ")
    subtrahend = input("Enter binary subtrahend: ")

    if binary_decimal(minuend) < binary_decimal(subtrahend):
        print("Subtrahend cannot be greater than Minuend!! ")

    else:
        print("The difference of: ")
        print(minuend)
        print(subtrahend)
        print("----------")
        print(decimal_binary(binary_decimal(minuend) - binary_decimal(subtrahend)))


def SubOctal():
    minuend = input("Enter octal minuend: ")
    subtrahend = input("Enter octal subtrahend: ")

    if octal_decimal(minuend) < octal_decimal(subtrahend):
        print("Subtrahend cannot be greater than Minuend!! ")

    else:
        print("The difference of: ")
        print(minuend)
        print(subtrahend)
        print("----------")
        print(decimal_octal(octal_decimal(minuend) - octal_decimal(subtrahend)))


def SubHexa():
    minuend = input("Enter hexadecimal minuend: ")
    subtrahend = input("Enter hexadecimal subtrahend: ")

    if hex_decimal(minuend) < hex_decimal(subtrahend):
        print("Subtrahend cannot be greater than Minuend!! ")

    else:
        print("The difference of: ")
        print(minuend)
        print(subtrahend)
        print("----------")
        print(decimal_hexa(hex_decimal(minuend) - hex_decimal(subtrahend)))


def MultBin():
    Array = []

    while True:
        choice = input("Enter a binary number or press 'X' to solve: ")

        if ( (choice == "X") or (choice == 'x') ):
            break
        else:
            Array.append(binary_decimal(choice))

    product = 1
    for x in Array:
        product *= x

    print("The product of: ")
    for x in Array:
        print(decimal_binary(x))

    print("------------")
    print(decimal_binary(product))


def MultOctal():
    Array = []

    while True:
        choice = input("Enter an octal number or press 'X' to solve: ")

        if ( (choice == "X") or (choice == 'x') ):
            break
        else:
            Array.append(octal_decimal(choice))

    product = 1
    for x in Array:
        product *= x

    print("The product of: ")
    for x in Array:
        print(decimal_octal(x))

    print("------------")
    print(decimal_octal(product))


def MultHexa():
    Array = []

    while True:
        choice = input("Enter a hexadecimal number or press 'X' to solve: ")

        if ( (choice == "X") or (choice == 'x') ):
            break
        else:
            Array.append(hex_decimal(choice)) 

    product = 1
    for x in Array:
        product *= x
        print(product)

    print("The product of: ")
    for x in Array:
        print(decimal_hexa(x))

    print("------------")
    print(decimal_hexa(product))


def DivBin():
    dividend = input("Enter dividend: ")
    divisor = input("Enter divisor: ")

    if binary_decimal(dividend) < binary_decimal(divisor):
        print("divisor cannot be greater than dividend!! ")

    else:
        print("The quotient of: ")
        print(f" {dividend} / {divisor}")
        # print(divisor)
        print("----------")

        answer = math.floor(binary_decimal(dividend) / binary_decimal(divisor))
        remainder = binary_decimal(dividend) - answer * binary_decimal(divisor)

        print(f"{decimal_binary(answer)} r {decimal_binary(remainder)}")
        # print(remainder)


def DivOctal():
    dividend = input("Enter dividend: ")
    divisor = input("Enter divisor: ")

    if octal_decimal(dividend) < octal_decimal(divisor):
        print("divisor cannot be greater than dividend!! ")

    else:
        print("The difference of: ")
        print(dividend)
        print(divisor)
        print("----------")

        answer = math.floor(octal_decimal(dividend) / octal_decimal(divisor))
        remainder = octal_decimal(dividend) - answer * octal_decimal(divisor)

        print(f"{decimal_octal(answer)} r {decimal_octal(remainder)}")


def DivHexa():
    dividend = input("Enter dividend: ")
    divisor = input("Enter divisor: ")

    if hex_decimal(dividend) < hex_decimal(divisor):
        print("divisor cannot be greater than dividend!! ")

    else:
        print("The difference of: ")
        print(dividend)
        print(divisor)
        print("----------")

        answer = math.floor(hex_decimal(dividend) / hex_decimal(divisor))
        remainder = hex_decimal(dividend) - answer * hex_decimal(divisor)

        print(f"{decimal_hexa(answer)} r {decimal_hexa(remainder)}")

if __name__ == "__main__":
    while True:
        print("\n\n\nChoose an option:")
        print("<1> Conversion")
        print("<2> Operation")
        choice = input("\nEnter your choice: ")

        match choice:
            case "1":
                while True:
                    print("\n\nChoose an option:")
                    print("<1> Decimal to Binary")
                    print("<2> Decimal to Octal")
                    print("<3> Decimal to Hexadecimal")
                    print("<4> Binary to Decimal")
                    print("<5> Binary to Octal")
                    print("<6> Binary to Hexadecimal")
                    print("<7> Octal to Decimal")
                    print("<8> Octal to Binary")
                    print("<9> Octal to Hexadecimal")
                    print("<10> Hexadecimal to Decimal")
                    print("<11> Hexadecimal to Binary")
                    print("<12> Hexadecimal to Octal")
                    print("<0> Back")

                    choice2 = input("\nEnter your choice: ")

                    match choice2:
                        case "1":
                            decimal_num = input("\n\nEnter a decimal number: ")
                            answer = decimal_binary(decimal_num)
                            print(f"\n{decimal_num} in binary is {answer}")

                        case "2":
                            decimal_num = input("\n\nEnter a decimal number: ")
                            answer = decimal_octal(decimal_num)
                            print(f"\n{decimal_num} in octal is {answer}")

                        case "3":
                            decimal_num = input("\n\nEnter a decimal number: ")
                            answer = decimal_hexa(decimal_num)
                            print(f"\n{decimal_num} in hexadecimal is {answer}")

                        case "4":
                            binary_num = input("\n\nEnter a binary number: ")
                            answer = binary_decimal(binary_num)
                            print(f"\n{binary_num} in decimal is {answer}")

                        case "5":
                            binary_num = input("\n\nEnter a binary number: ")
                            answer = binary_octal(binary_num)
                            print(f"\n{binary_num} in octal is {answer}")

                        case "6":
                            binary_num = input("\n\nEnter a binary number: ")
                            answer = binary_hex(binary_num)
                            print(f"\n{binary_num} in hexadecimal is {answer}")

                        case "7":
                            octal_num = input("\n\nEnter an octal number: ")
                            answer = octal_decimal(octal_num)
                            print(f"\n{octal_num} in decimal is {answer}")

                        case "8":
                            octal_num = input("\n\nEnter an octal number: ")
                            answer = octal_binary(octal_num)
                            print(f"\n{octal_num} in binary is {answer}")

                        case "9":
                            octal_num = input("\n\nEnter an octal number: ")
                            answer = octal_hex(octal_num)
                            print(f"\n{octal_num} in hexadecimal is {answer}")

                        case "10":
                            hexa_num = input("\n\nEnter a hexadecimal number: ")
                            answer = hex_decimal(hexa_num)
                            print(f"\n{hexa_num} in decimal is {answer}")

                        case "11":
                            hexa_num = input("\n\nEnter a hexadecimal number: ")
                            answer = hex_binary(hexa_num)
                            print(f"\n{hexa_num} in binary is {answer}")

                        case "12":
                            hexa_num = input("\n\nEnter a hexadecimal number: ")
                            answer = hex_octal(hexa_num)
                            print(f"\n{hexa_num} in octal is {answer}")

                        case "0":
                            break

            case "2":
                while True:
                    print("\n\nChoose an option:")
                    print("<1> Addition of Binary")
                    print("<2> Addition of Octal")
                    print("<3> Addition of Hexadecimal")
                    print("<4> Subtraction of Binary")
                    print("<5> Subtraction of Octal")
                    print("<6> Subtraction of Hexadecimal")
                    print("<7> Multiplication of Binary")
                    print("<8> Multiplication of Octal")
                    print("<9> Multiplication of Hexadecimal")
                    print("<10> Division of Binary")
                    print("<11> Division of Octal")
                    print("<12> Division of Hexadecimal")
                    print("<0> Back")

                    choice3 = input("Enter your choice: ")

                    match choice3:
                        case "1":
                            AddBinary()

                        case "2":
                            AddOctal()

                        case "3":
                            AddHexa()

                        case "4":
                            SubBin()

                        case "5":
                            SubOctal()

                        case "6":
                            SubHexa()

                        case "7":
                            MultBin()

                        case "8":
                            MultOctal()

                        case "9":
                            MultHexa()

                        case "10":
                            DivBin()

                        case "11":
                            DivOctal()

                        case "12":
                            DivHexa()
                        case "0":
                            break

            case "0":
                break
