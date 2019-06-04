#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:30:02 2019

@author: athreya
"""


D = {'tv':5000, 'freezer':2000, 'washingmachine':3000}
for key in D:
    if(D[key]>2500):
        print(key,":",D[key])

#tv : 5000      
#washingmachine : 3000
        
d={'a':1,'b':2,'c':3}
l=list(d.values())
print(l)
l[0]=40
print(l)   

#[1, 2, 3]
#[40, 2, 3]

D = {'tv':5000, 'freezer':2000, 'washingmachine':3000}
l=list(d.keys())
print(l)
l2=list(d.values())
print(l2)

#['a', 'b', 'c']
#[1, 2, 3]


d = {'tv':5000, 'freezer':2000, 'washingmachine':3000}
l=list(d.keys())
l.sort()
for key in l:
    print(key,":",d[key]) 

#freezer : 2000
#tv : 5000
#washingmachine : 3000


#write a program to print occurance count of all the characters of a string.

str="Good Morning"
d=dict()
count=0
for char in str:
    if char in d:
        d[char]=d[char]+1
    else:
        d[char]=1
print(d)

#{'G': 1, 'o': 3, 'd': 1, ' ': 1, 'M': 1, 'r': 1, 'n': 2, 'i': 1, 'g': 1}