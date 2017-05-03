digitpower = [0]
for i in range(1,10):
    digitpower.append(i**5)

def digitsum(n):
    s = 0
    for i in str(n):
        s+= digitpower[int(i)]
    return s


   

#upper est 9^5*6digits
sums = 0
for i in range(3,354294):
    if digitsum(i) == i:
        sums+=i
        print(i)
print(sums)
    
