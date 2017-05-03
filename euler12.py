#wrong for 1
def numfactors(x):
    #if x = 1:
        #return 1
    counter = 1
    total = 0
    #factors have corresponding halfs
    while (counter < (x**.5)):
        if (x % counter == 0):
            total += 2
        counter += 1
    #except squares 
    if (x % (x**.5)) == 0:
        total +=1
    return total

def euler12(div):
    test = 3
    trinum = 2
    factors = 0
    while  factors <= div:
        trinum += 1
        test = (trinum * (trinum + 1)) / 2
        factors = numfactors(test)
    
    print(test, factors, trinum)
