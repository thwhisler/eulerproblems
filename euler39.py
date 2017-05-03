def numofrighttri(perimeter):
    trilist = set()
    for x in range(1,perimeter-1):
        for y in range(1,perimeter-1):
            z = perimeter-x-y
            if z**2 == (x**2)+(y**2):
                trilist.add(x)
                trilist.add(y)
                trilist.add(z)
        
    return int(len(trilist)/3)
largest = 0
for p in range(3,1001):
    temp = numofrighttri(p)
    if temp > largest:
        largest = temp
        perm = p
print(largest,perm)
