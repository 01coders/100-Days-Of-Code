#!/usr/bin/python

a = [10, 20, 30]
b = [1, 2, 3]
d = a+b
print(d)  # a+b are concatenate to form a list...concatenation opertor(+)..type d also a list

e = a*3
print(e)  # [10,20,30]*3 :it repeats 3 times

# list slize is similar to string slize...only slize can be remove
l = [10, 20, 30, 40]
print(l)
print(l[1:3])
print(l[:2])

newl = l[0:4]
print(newl)
print(l)

print(l[::-1])
