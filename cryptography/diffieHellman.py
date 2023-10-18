def diffieHelmanEncrypt():
    #TODO: add prime number validator chuchu
    p = int(input("Input prime number: "))
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