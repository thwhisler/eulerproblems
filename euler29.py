powers = []
for a in range(2,1001):
    for b in range(2,1001):
        temp = a**b
        if temp not in powers:
            powers.append(temp)
print(len(powers))
