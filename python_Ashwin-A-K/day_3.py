a = 10
b = 20
c = 30
if(a > b and a > c):  # example for if, elif and else
    print("a is greatest")
elif b > a and b > c:
    print("b is greatest")
else:
    print("c is greatest")

a = "hi hello"
b = "hi hello"
if(a == b):  # checks for equivalance of string
    print("true1")
else:
    print("false")

c = "hello"

if(c == "hi"):
    print("true1")
else:
    print("false")

a = 10
b = 20
print(id(a))  # returns the address of obj being referred
print(id(b))
# address is allocated dynamically and changes as shown above

c = 30
d = 30
# since value is common separate mem allocation is not done adreess is same for both obj
print(id(c))
print(id(d))

a = 10
b = 10
if a is b:
    print("both are same")
else:
    # a is b :id(a)==id(b) #a is not b:id(a)!==id(b)
    print("both are different")
