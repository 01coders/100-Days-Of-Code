#!/usr/bin/python

l1 = [10, 20, 30, 40]  # its start from zero (list is a collection of ele)
print(l1)
print(l1[3])

l1[3] = 50
print(l1)

l2 = [10, 2.5, 'hello']  # list can contain of homo or hetrogeneous ele
print(l2)
print(l2[2])
l2[1] = "welcome"  # list are mutable and strings are immutable
print(l2)

# 4 ele in list(int,str,list inside list..ie.[])
l3 = [10, 10, 'hello', ['A', 'B']]
print(l3[3])
print(l3[2])
print(l3[3][0])  # it can be print list inside list ie..A index[0],B index[1]

l4 = ([10, 20, 30], [2, 4, 5])  # here l4=([0],[1])
print(l4[1])
