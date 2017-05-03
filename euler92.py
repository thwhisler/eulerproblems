
def nextnum(num):
    x = 0
    for i in str(num):
        x += int(i)**2
    return x

#generates list of weither chain end is 1 or 89 in order respective to their numbers 
def listbuilder():
    #567 highest possible 2nd value < 10 mil
    list891 = []
    for i in range(1,567):
        #print('\n'+ str(i) * 10 + ' ' + '\n')
        seq = nextnum(i)
        notrep = True
        while notrep:
            #print(str(seq)+'->',end='')
            if seq == 89:
                list891.append(89)
                notrep = False
            if seq == 1:
                list891.append(1)
                notrep = False
            seq = nextnum(seq)
    return list891

n89 = 0
for i in range(1,10000000):
    data = listbuilder()
    if data[nextnum(i)-1] == 89:
        n89 +=1
print(n89)
