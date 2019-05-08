#!/usr/bin/python

try:  # try except for error handling
    a = int(input("enter a A value"))
    b = int(input("enter a B value"))
    print(a/b)
except:
    print("Enter valid input")

print(max("abc def")) #compares ascii values and returns highest value
print(min("abc def")) #prints ascii value of 'space'
print(min("abcdef"))
print(len("abc def"))

a=10
print(type(a))

b=int(-2.5) #to convert to int
b=float(1) #to convert to float
b=str(1) #to convert to string

# b=b+1
# print(s) #can only concatenate str (not "int") to str

fun2() #there is no segement of code... define anywhere and call anywhere
def fun():
    print ("this is a user  defined function")
def fun2():
    print ("this is a also user  defined function")
    print ("end of function")
print("this is first line")
fun()
