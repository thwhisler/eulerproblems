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

def euler10(x):
    sum = 2
    test = 3
    while test < x:
        if (isPrime(test)):
            sum += test
        test += 2
    print(sum)
