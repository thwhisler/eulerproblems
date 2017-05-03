def isPrime(x):
    if (x < 2):
        return False
    if (x == 2):
        return True
    factor = 2
    while (factor <= (x**.5)):
        if (x % factor == 0):
            return False
        factor +=1
    return True
def euler7(x):
    counter = 1
    prime = 3
    while (counter < x):
        if (isPrime(prime)):
            counter += 1
        prime += 2
    print(prime-2)

        
