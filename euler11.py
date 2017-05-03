
#finds largest product of <productnum> adjacent <numsize> digit numbers in the grid of numbers
def euler11():
    numsize = 2
    productnum = 4

    data = gridformat(numsize)
    rowlen = len(data[0])
    columnlen = len(data)
    biggest = 0
    store =[]
    #horizontal products
    for column in range(0,columnlen):
        for row in range(0,rowlen - productnum+1):
            test = 1
            for i in range(0,productnum):
                test *= data[column][row+i]
            if test > biggest:
                biggest = test
                store = ['horizontal',column,row]
    #vertical products
    for column in range(0,columnlen-productnum+1):
        for row in range(0,rowlen):
            test = 1
            for i in range(0,productnum):
                test *= data[column+i][row]
            if test > biggest:
                biggest = test
                store = ['vetical',column,row]
    #diagonal down products
    for column in range(0,columnlen-productnum+1):
        for row in range(0,rowlen-productnum+1):
            test = 1
            for i in range(0,productnum):
                test *= data[column+i][row+i]
            if test > biggest:
                biggest = test
                store = ['diagonal down',column,row]
    #diagonal up products
    for column in range(productnum-1,columnlen):
        for row in range(0,rowlen-productnum+1):
            test = 1
            for i in range(0,productnum):
                test *= data[column-i][row+i]
            if test > biggest:
                biggest = test
                store = ['diagonal up',column,row]
                
    store.append(biggest)
    return store
    
#grid format: Rectangle amount of numbers, Numbers with leading zeros to digit length, 1 character seperating numbers
#returns list of lists with ints
def gridformat(numsize):
    dataraw = open('euler11data.txt')
    data = []
    line = dataraw.readline()
    rowlen = len(line)
    while line != '':
        row = []
        for i in range(0,rowlen-numsize,numsize+1):
            row.append(int(line[i:i+numsize]))
        data.append(row)
        line = dataraw.readline()
    dataraw.close()
    return data
