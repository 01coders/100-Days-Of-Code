#!/usr/bin/python

l = [10, 20, 30]
l[1] = 40
print(l)
# l[4]=50 # cannot add ele to list based on index instead use append function
l.append(40)
print(l)

a = [10, 20, 30]
b = [34, 40]
a.extend(b)  # 'a' list is extend by adding 'b' list
print(a)

a.sort()  # to sort thr list
print(a)

x = [10, 20, 30, 40]
val = x.pop()  # method pop(),it returns last ele in the list
print(val)
print(x)
