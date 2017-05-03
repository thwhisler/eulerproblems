def isperm(num1,num2):
    num1 = str(num1)
    num2 = str(num2)
    for i in range(len(num1)):
        pos = num2.find(num1[i])
        if pos == -1:
            return False
        else:
            num2 = num2[:pos] + num2[(pos+1):]
    return True

f = open('primelist.txt', 'r')
primes = [int(x) for x in f.read().split(', ')]


maxnum = 10000
for i in primes:
    for n in range(1,int((maxnum-i)/2)):
        after1 = i + n
        after2 = i + 2* n
        if (after1 in primes) and (after2 in primes) and isperm(i,after1) and isperm(i,after2):
            print(i,after1,after2, n)
            
