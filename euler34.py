facts = [1]
x = 1
for i in range(1,10):
    x = x*i
    facts.append(x)

def digitsum(n):
    s = 0
    for i in str(n):
        s+= facts[int(i)]
    return s


   

#upper est 9! = 362880*7digits
sums = 0
for i in range(3,362880*7):
    if digitsum(i) == i:
        sums+=i
        print(i)
print(sums)
    
