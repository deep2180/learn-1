a = input("Hey give me a number:")

print(a)

f = input(f"this is formatted input after you gave me {a}.. whats next ? ")
print(f)

def foo():
    a=10
    print(int(a)*int(f))


foo() 

print(a)


def straight_up(x):
    print(f"This was the input you typed {x}")

straight_up(int(input("Enter Now\n")))