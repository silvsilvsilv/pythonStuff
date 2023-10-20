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

def rsa():
    p = int(input("P is: "))
    
    if not(isPrime(p)):
        print(f"{p} is not a prime number!")
        rsa()
    
    q = int(input("Q is: "))

    if not(isPrime(q)):
        print(f"{q} is not a prime number!")
        rsa()
    
    n = p * q
    print(f"N is: {p} * {q} = {n}")

    phiN = (p - 1) * (q - 1)
    print(f"Phi(n) is: {p-1} * {q-1} = {phiN}")

    pub = int(input("Public key: "))

    i = 1

    d = int( ((phiN*i) + 1) / pub )
    while ( d % 1 ) != 0:
        i+=1
    
    print(f"Public key = ({pub}, {n})\nPrivate key = ({d}, {n})")

    plainText = int(input("What is plain text value: "))
    
    cipherText = ( (plainText**pub ) % n )
    print(f"Cipher Text: {cipherText}")

    pText = ( (cipherText**d ) % n )
    print(f"Plain Text: {pText}") 

rsa()