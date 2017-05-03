def euler53():
    return 0

def f(num):
    if num == 2:
        return 2
    return num*f(num-1)
        
