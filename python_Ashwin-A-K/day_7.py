#!/usr/bin/python

l = [10, 20, 30, 40, 50]
n = len(l)
print("number of elements =",)
for i in range(n):
    print(l[i])

for elem in l:
    print(elem)

# write a prog to add the content of list stored in other list

A = [10, 20, 30]
B = [1, 2, 3]
for i in range(len(A)):
    print(A[i]+B[i])

a = [10, 20, 30]
b = [1, 2, 3]
c = a[0]+b[0]  # adds elements of index 0 of list a & b
print(c)
