# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:28:03 2019

@author: Parikshith.H
"""


d={'a':1,'b':2,'c':3}
print(d) 
print(d.values()) 
print(d.keys()) 
print(d.items()) 
for val in d.values():
    print(val) 
for key,val in d.items():
     print(key,val) 
# =============================================================================
# #output:
# 1
# 2
# 3
# a 1
# b 2
# c 3
# =============================================================================

for t in d.items(): 
    print(t)
# =============================================================================
# #output
# ('a', 1)
# ('b', 2)
# ('c', 3)
# =============================================================================


#program to print the contents of the dict sorted by the key value
l=list()
D={'b':1,'a':2,'c':3}
L = list(D.keys())
L.sort()
print(L)
for key in L:
    print(key,":",D[key])
print(D)
print(L)
# =============================================================================
# #output:
# ['a', 'b', 'c']
# a : 2
# b : 1
# c : 3
# {'b': 1, 'a': 2, 'c': 3}
# ['a', 'b', 'c']
# =============================================================================
