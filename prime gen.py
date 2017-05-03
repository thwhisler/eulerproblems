def isPrime(x):
    factor = 2
    while (factor <= (x**.5)):
        if (x % factor == 0):
            return False
        factor +=1
    return True

#gen primes from lower to upper
#lower must be odd
upper = 1000000
#lower = 3
lower = 3
primes = []
if lower >= 2:
    primes.append(2)
for i in range(lower,upper,2):
    if isPrime(i):
        primes.append(i)

f = open('primelist.txt', 'w')
f.write(str(primes).strip('[]'))
f.close()

#f = open('primelist.txt', 'r')
#primes = [int(x) for x in f.read().split(', ')]
