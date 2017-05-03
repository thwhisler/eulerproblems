def euler3(x):
    ogvalue = x
    factors = []
    counter = 3

    while (x != 1):
        #2 only even prime, pull out first
        while (x % 2 == 0):
            factors.append(2)
            x = int(x / 2)
        #check every odd number 3 onwards 
        if (x % counter == 0):
            factors.append(counter)
            x = int(x / counter)
        else:
            counter += 2

    print("The prime factors of ", ogvalue, " are ", factors)
        
