#!/usr/bin/python

a = "Hello, World!"

print(a[1]) #character at position 1
print(a[2:5]) #position 2 to position 5

b="      Hello, World!"

print(a.strip()) # returns the value by striping whitespaces
print(len(b)) # returns the length of a string
print(b.lower()) # returns the string in lower case
print(b.upper()) # returns the string in upper case
print(b.replace("H", "J")) # replaces a characters with another character
print(b.split(",")) # returns ['Hello', ' World!']
