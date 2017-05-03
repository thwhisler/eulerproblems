def euler9():
    for a in range(1,500):
        for b in range(1,500):
            temp = (a*a + b*b)
            if is_square(temp):
                c = int(temp**.5)
                if  (a+b+c) == 1000:
                    return (a,b,c,a*b*c)
            
def is_square(integer):
    root = integer**.5
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False
