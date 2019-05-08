# operators part 2

#logical operators
a = 25
print(a > 3 and a < 10)  # returns False because 25 is greater than 3 AND 10
print(a > 3 or a < 4)    # returns True because 25 is greater than 3 
print(not(a > 3 or a < 10))   # returns False because not reverses the result

#Identity Operators
x = ["Hello", "world"]
y = ["damn", "tired"]
z = x
print(x is z)   # returns True because z is the same object as x
print(x is y)   # returns False because x is not the same object as y

#Membership operators
print("Hello" in x) #returns true as hello is present in x

#Bitwise operation
d=14
e=17
print(d&e) #returns zero as output by performing bitwise AND operation
print(d|e) #returns 31 as output by performing bitwise OR operation
print(d^e) #returns 31 as output by performing bitwise XOR operation
print(~(d|e)) #returns -32 as output by performing bitwise XOR operation
print(d<<2)   #returns 56 as output by performing bitwise left shift operation
print(d>>2)   #returns 3 as output by performing bitwise right shift operation
