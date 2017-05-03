f = open('euler67tri.txt', 'r')
#triangle reading and converting to list of rows of ints
triangle = f.read().split('\n')
for i in range(len(triangle)):
    triangle[i] = triangle[i].split(" ")
for i in range(len(triangle)):
    for x in range(len(triangle[i])):
        triangle[i][x] = int(triangle[i][x])
f.close()

#start from 2nd row to bottom go up adding greater of 2 values below it
for i in range(len(triangle)-2,-1,-1):
    for x in range(len(triangle[i])):
        test1 = triangle[i+1][x]
        test2 = triangle[i+1][x+1]
        if test1 > test2:
            largest = test1
        else:
            largest = test2
        triangle[i][x] += largest
        
print(triangle[0])
