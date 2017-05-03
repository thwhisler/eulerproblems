def euler19():
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    #jan 1 1901 = tuesday, sundays 0 sat 6
    start = 2 
    total = 0
    for y in range (1901,2001):
        for i in range(0,len(months)):
            if start == 0:
               total += 1
            if (i == 1) and (y % 4 == 0):
                start = (start + months[i] + 1) % 7
            else:
                start = (start + months[i]) % 7

    print(total)
