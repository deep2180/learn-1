def add(a, b):
    return a+b

def sub(a,b):
    return a - b

def mult(a,b):
    return a*b

def div(a,b):
    if b == 0:
        print (f"can't divide by {b}")
        return 0
    return a/b