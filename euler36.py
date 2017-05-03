def isPali(x):
    length = len(str(x))
    back = length - 1
    front = 0
    while (front <= back):
        if (str(x)[front] != str(x)[back]):
            return False
        front += 1
        back -= 1
    return True

sums = 0
for i in range(1,1000001):
    if isPali(i) and isPali(bin(i)[2:]):
        print(i)
        sums += i
print(sums)
