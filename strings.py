age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


txt = "My name is John, and I am {} years and {} months"
year = 12
month = 3
print(txt.format(year,month))


print(f"My name is John, and I am {year} years and {month} months")


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")
print(x)

x = txt.partition("bananas")
print(x)