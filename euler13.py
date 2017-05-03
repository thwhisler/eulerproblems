def euler13():
    dataraw = open('euler13data.txt')
    data = []
    sum = 0
    for line in dataraw:
        sum += int(line)
    print(str(sum)[0:10])
    dataraw.close()
