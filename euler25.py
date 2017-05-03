import math

f1 = 1
f2 = 1
digits = 1
term = 2
while digits < 1000:
    temp = f1 + f2
    f1 = f2
    f2 = temp
    term += 1
    digits = int(math.log10(f2))+1
print(term)
