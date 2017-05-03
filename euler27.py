from primelist import Prime

bound = 100
primeslist = Prime(bound)
primeslist = primeslist.toList()
#longest sequence, a , b 
longest = [0,0,0]

for a in range(-1*bound,bound+1):
    for b in range(-1*bound,bound+1):
        n = 0
        quad = 2
        while quad in primeslist:
            quad = n * n + a * n + b
            if n > longest[0]:
                longest[1] = a
                longest[2] = b
print(longest)
        

