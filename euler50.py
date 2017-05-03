f = open('primelist.txt', 'r')
primes = [int(x) for x in f.read().split(', ')]
f.close()
sumlimit = 1000000
primestop = 100
largest = 0
lseq = 0

def helper(n):
    sump = 0
    seq = 0
    for i in primes[n:]:
        sump += i
        seq += 1
        if sump > sumlimit:
            break
        #print(sump,seq)
        global lseq
        if (seq > lseq) and (sump in primes):
            global largest
            largest = sump
            lseq = seq




for n in range(0,primestop):
    helper(n)
print(largest, lseq)
        
