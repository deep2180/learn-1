x = "12.1a"


try:
    dig = int(x)
    print(dig*2)
#except:
except ValueError:
    print("Oh No!")    