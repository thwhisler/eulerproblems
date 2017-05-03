def isperm(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    for i in range(len(num1)):
        if num2.find(num1[i]) == -1:
            return False
    return True
#primelist gen
f = open('primelist.txt', 'r')
primes = [int(x) for x in f.read().split(', ')]
sortedp = []
i = 0

#rearrange to set of sets where the numbers are permutations
while i < len(primes)-2:
    test = primes[i]
    keyp = []
    x = i
    while x < len(primes):
        if isperm(test,primes[x]):
            keyp.append(primes[x])
        x += 1
    if len(keyp) >= 3:
        sortedp.append(keyp)
    i += 1
realsort = []
for i in sortedp:
    #print(realsort,i[-1])
    if i[-1] in realsort:
        continue
    realsort.append(i)
        
print(realsort)
f.close()
