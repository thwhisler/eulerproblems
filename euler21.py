def factorsum(num):
    if num % 2 == 0:
        odd = 1
        sum = 3
    else:
        odd = 2
        sum = 1
    counter = 3
    while counter <= (num / 2):
        if num % counter == 0:
            sum += counter
        counter += odd
    return sum

pairs = []
for i in range(1,10001):
    test = factorsum(i)
    if test > i:
        if factorsum(test) == i:
            pairs.append(i)
            pairs.append(test)
print(sum(pairs))
print(pairs)
