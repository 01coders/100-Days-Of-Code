a = 10  # initializing a variable and printing it
print(a)
type(a)
print("the value is a = ", a)  # no format specifier

s = 'Hi'
print(s, "World")
print(s+"World")  # no space is given
# print("the value is"+a)  #only concatenate str (not "int") to str

print("enter a value")
b = input()  # accepting input
print(b)

b = input("enter a value")  # simpliying above steps
print(b)

# d=a/b
#print("result is",d)
# TypeError: unsupported operand type(s) for /: 'str' and 'str' # because variable are treated as string

a = int(input("enter first input"))
b = int(input("enter second input"))  # now, both a and b are of type int
type(a)
type(b)
c = a/b
print("div is", c)
