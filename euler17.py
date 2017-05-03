def numword(num):
    f12 = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen', 'fourteen']
    #counts of basic structure beganings i.e. fif
    tensprefix = ['twen','thir','for','fif','six','seven','eigh','nine']
    constructers = ['teen','ty','hundred','thousand']
    word = ''
    if num == 0:
        return "Zero"
    if num < 0:
        word = 'negative'
        num *= -1
    if num <= 14:
        return word + f12[num-1]
    if num < 20:
        return word + tensprefix[num-12] + constructers[0]
    if num < 100:
        firstd = int(num/10)
        otherd = num % 10
        if otherd == 0:
            return word + tensprefix[firstd-2] + constructers[1]
        else:
            return word +tensprefix[firstd-2] + constructers[1] + numword(otherd)
    if num < 1000:
        firstd = int(num/100)
        otherd = num % 100
        if otherd == 0:
            return word + f12[firstd-1] + constructers[2]
        else:
            return word + f12[firstd-1] + constructers[2] + 'and' + numword(otherd)
        
        
sum = 0
for i in range(1,1000):
    sum += len(numword(i))

    #print(numword(i),len(numword(i)))
print(sum+11)
