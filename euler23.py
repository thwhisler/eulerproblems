abunds = []

#true if abundant number
def abundant(num):
    root = int(num / 2)+1
    sum = 1
    for i in range(2,root):
        if num % i == 0:
            sum+=i
        if sum > num:
            return True
    return False
#tests if num is abundant sum
def issum(num):
    for i in range(len(abunds)):
        if i > num - 12:
            return False
        #only do i index onwards or will be duplicate testing
        for j in abunds[i:]:
            if abunds[i] + j == num:
                #print(i,j)
                return True

#non higher than 20161, 12 min incremet, builds list for issum
for i in range(12,20150):
    if abundant(i):
        abunds.append(i)

#sum until first abund sum
nonabundsum = sum(range(1,24))
for i in range(1,20162):
    if not issum((i)):
        nonabundsum += i
    
print(nonabundsum)
