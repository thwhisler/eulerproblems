def euler20():
    largenum = 1
    sum = 0
    for i in range(2,101):
        largenum *= i
    largenum = str(largenum)
    for i in range(0,len(largenum)):
        sum += int(largenum[i])
    print(sum)
    
