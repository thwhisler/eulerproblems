def euler14(size):
    #holds calculated collatz seq length, length for any number = storage[number-2]
    storage = []
    largest = [1,1]
    for i in range(0,size-2):
        storage.append(0)
    for i in range(2,size):
        count = 1
        test = i
        
        while test != 1:
            #if currentvalue < newvalue we are testing and not 1 count will be in storage
            if (test < i):
                count += storage[int(test-2)]-1
                test = 1
            else:
                count += 1
                test = col(test)
        #store new calculate value and check if largest
        if largest[0] < count:
            largest[0] = count
            largest[1] = i
        storage[i-2] = count
    print(largest)
        
    
def col(num):
    if (num % 2) == 0:
        return (num / 2)
    else:
        return (3*num +1)
