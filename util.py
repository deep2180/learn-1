def add(a, b):
    return a+b

def sub(a,b):
    return a - b

def mult(a,b):
    return a*b

def div(a,b):
    if b == 0:
        print (f"{b} cant be zero(0)")
        return 0
    return a/b