#!/usr/bin/python

y = [10, 20, 30, 40]
y.pop(2)  # it remove & return the value of index 1
print(y)
y = [10, 20, 30, 40]
del y[0]  # it delets the ele of '0' index in list y
print(y)
# The method pop() removes & returns the value but del does not return the value

y = [10, 20, 30, 40]
del y[1:3]
print(y)

z = sum(y)
print(z)
avg = z/(len(y))
print(avg)
