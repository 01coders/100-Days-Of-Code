#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 23:40:58 2019

@author: athreya
"""

print (type(42))
print (type(4.2))
print (type('spam'))

# =============================================================================
# OUTPUT
# <class 'int'>
# <class 'float'>
# <class 'str'>
# =============================================================================

#Iterations
counter=1
while counter<=3:
    print(counter)
    counter+=1
print("end")

# =============================================================================
# #OUTPUT
# 1
# 2
# 3
# end
# =============================================================================


#write a program to find sum of 1st n natural numbers
n=10
sum = 0
for i in range(1,n+1):
    sum=sum + i
    print(sum)

# =============================================================================
# #OUTPUT
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55
# =============================================================================

n=10
sum=0
i=1
while i<=n:
     sum = sum + i
     i = i+1;
print(sum)             #55


for index in [10,20,30,40]:
     print("hi")                 #4 times hi
     print(index)  

# =============================================================================
# #OUTPUT
# hi
# 10
# hi
# 20
# hi
# 30
# hi
# 40
# =============================================================================
