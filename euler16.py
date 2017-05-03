def euler16():
    largenum = str(2**1000)
    sum = 0 
    for i in range(0,len(largenum)):
        sum += int(largenum[i])
    print(sum)
    
