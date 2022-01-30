
foo = 12*12

def ham(n="pig"):
    print(f"Here comes the {n}")

def mam(s, msg="Awesome"):
    print(f"foo will do {s*foo} which is {msg}")
    ham()

mam(11)
mam(1,"good!")

ham()


# A lil If else block

if foo == 0:
    print('0')
elif foo == 10:
    print('10')
else:
    print("n")

print(type(foo))

##print("111 tell me about it")
##print("Strcat with  " + str(10*12) + ' single quote')
#print(f"this is the geek way {12} of doing {111} things")

