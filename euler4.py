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
        

def euler4(digits):
    #[largest product, x, y]
    largest = [0,0,0]
    maxrange = int(10 ** digits)
    
    for x in range(int((maxrange/10)), maxrange):
        #dont waste time going through y values if x must be greater to be largest pali
        if (largest[0] / x) < (maxrange - 1):
            for y in range(int((maxrange/10)), maxrange):
                multi = x*y
                
                #dont waste time calculating palidrome if it will be less
                if largest[0] < multi:
                    if isPali(multi):
                            largest[0] = multi
                            largest[1] = x
                            largest[2] = y
    print(largest)
    



#speculation: odd digit length palindrome has no factors between terms
#speculation: largest palindrome digit length = 2*digit length of composite parts
#caution: this is not true for 1 digit (9 biggest palindrome), but I believe true for larger digit sizes

##every palindrome above 11 with an even number of digits has 11 as a factor
#for d>2 even digit palindrome in form of its terms: while n <= d/2 :(10^(d-1)+10^0)Asub1+(10^(d-2)+10^1)Asub2+...(10^(d-n)+10^(n-1))Asubn
#summation of (10^(d-n)+10^(n-1)) from 1 to d/2:(-1+10^d)/9
#for d>2 where d is even always of form 1111111...
#11 always factor of even digit palindromes

def euler4b(digits):
    #[largest product, x, y]
    maxrange = int(10 ** digits)
    #assuming largest palindrome digit length = 2*digit length of composite parts
    largest = [int(10 ** (digits+1)),0,0]
    
    for x in range(int((maxrange/10)), maxrange):
        #dont waste time going through y values if x must be greater to be largest pali
        if (largest[0] / x) < (maxrange - 1):
            for y in range(int((maxrange/10)), maxrange):
                multi = x*y

                #dont waste time calculating palidrome if it will be less
                #if (multi % 11 == 0): seems to slow 
                if largest[0] < multi:
                    if isPali(multi):
                        largest[0] = multi
                        largest[1] = x
                        largest[2] = y
    print(largest)
