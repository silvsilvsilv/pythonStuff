def rsa():
    #TODO: add authenticator for prime number chuhcu
    p = int(input("P is: "))
    q = int(input("Q is: "))

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