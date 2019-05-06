#!/usr/bin/python

str = 'hello hi'
# it converts str into list. Each character is consider as ele. o/p is['h', 'e', 'l', 'l', 'o', ' ', 'h', 'i']
l = list(str)
print(l)

str = 'hello hi'
l = str.split()  # it splits string into the 2 ele. o/p is ['hello', 'hi']
print(l)

str = 'hello$hi'
l = str.split()  # it takes whole str..o/p is ['hello$hi']
print(l)

str = 'hello$hi'
delimiter = '$'
l = str.split(delimiter)  # delimiter removes the character ie..$
print(l)

# To print occurence of word 'hello' in a given string
str = 'hello'
l = list(str)
print(l)
