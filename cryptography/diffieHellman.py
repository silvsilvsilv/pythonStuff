def isPrime(num:int):
    if num > 1:
    # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False

def diffieHelmanEncrypt():
    p = int(input("Input prime number: "))
    if not(isPrime(p)):
        print(f"{p} is not a prime number!")
        diffieHelmanEncrypt()

    gen = int(input("Input generator: "))

    pr1 = int(input("What is private key 1: "))
    pr2 = int(input("What is private key 2: "))

    
    pb1 = ( gen**pr1 ) % p
    print(f"Public Key 1: {pb1}")

    pb2 = ( gen**pr2 ) % p
    print(f"Public Key 2: {pb2}")

    ss1 = ( pb2**pr1 ) % p
    print(f"Shared secret 1: {ss1}")

    ss2 = ( pb1**pr2 ) % p
    print(f"Shared secret 2: {ss2}")
    

diffieHelmanEncrypt()