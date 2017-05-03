def euler5():
    num = 2520
    factors = [19,18,17,16,15,14,13,12,11]
    found = False
    while not found:
        pos = True
        for i in range(0,len(factors)):
            if (num % factors[i] != 0):
                pos = False
                break
        if pos:
            print(num)
            found = True
        num += 20
