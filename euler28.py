sums = 1
multi = 2
num = 1
#1001 * 1001 
while num < 1002001:
    sums += num * 4 + multi*10
    num += multi*4
    multi += 2
print(sums)
    
