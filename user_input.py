x = input(f"Enter your stuff\n")

print(x)

x_type = type(x)

if x.isdecimal() :
    x_type = "Float"
elif x.isdigit() :
    x_type = "Integer"
elif x.isalnum() :
    x_type = "AlphaNum"
elif x.isnumeric():
    x_type = "Numeric"
        

print(x_type) 