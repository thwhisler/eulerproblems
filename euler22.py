def euler22():
    #read in file, turn into list
    dataraw = open('p022_names.txt')
    data = []
    read = True
    #to start on letter instead of quote
    dataraw.read(1)
    rtemp = dataraw.read(1)
    count = 1
    while read:
        while rtemp != '\"':
            rtemp = dataraw.read(1)
            count += 1
        dataraw.seek(dataraw.tell()-count)
        data.append(dataraw.read(count-1))
        count = 1
        #to start on letter skipping dividers
        rtemp = dataraw.read(4)
        if len(rtemp) < 2:
            read = False
    dataraw.close()
    #alphabetize
    data.sort()
    #sum
    sum = 0
    for i in range(0,len(data)):
        sum += alphavalue(data[i])*(i+1)
    return sum
def alphavalue(name):
    #creates list [A,...,Z]
    chars = list(map(chr, range(65, 91)))
    sum = 0
    for letter in range(0,len(name)):
        counter = 0
        search = True
        while search:
            if chars[counter] == name[letter]:
                sum += counter+1
                search = False
            else:
                counter = counter+1
    return sum
