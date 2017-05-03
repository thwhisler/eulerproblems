def _isPrime(x):
        #starts factors at 3, only odd numbers should be fed in
        factor = 3
        if x == 1:
            return False
    
        while (factor <= (x**.5)):
            if (x % factor == 0):
                return False
            factor +=1
        return True

class Prime:
    "Create lists of primes"

    def __init__(self,upper=1000000,lower=2):
        #ensure valid limits
        if lower > upper:
            temp = lower
            lower = upper
            upper = temp
        if lower % 2 == 0:
            lower += 1
        self.plist = []

        if lower >= 2:
            self.plist.append(2)
         
        if upper >= 2:
            for i in range(lower,upper+1,2):
                if _isPrime(i):
                    self.plist.append(i)
    def toList(self):
        return self.plist
    def printlist(self):
            print(self.plist)
                    
                    
