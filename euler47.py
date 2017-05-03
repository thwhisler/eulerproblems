f = open('primelist.txt', 'r')
primes = [int(x) for x in f.read().split(', ')]
f.close()

def primefactors(num):
    i = 0
    primefactors = []
    root = int(num/2)
    for i in primes:
        if i <= root:
            if num % i == 0:
                primefactors.append(i)
        else:
            break
    return primefactors

def numprimefactors(num):
    return len(primefactors(num))


consecutive = 0
numlist = []
for n in range(1000000):
    if consecutive == 4:
        break
    if numprimefactors(n) == 4:
        #print(n,primefactors(n))
        consecutive += 1
        numlist.append(n)
    else:
        consecutive = 0
        numlist = []
print(numlist)

    
