# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:05:43 2019

@author: Parikshith.H
"""

 
L = [10,20,30,40,50]
n = len(L)
print("number of elements =",n)
for i in range(n):
    print(L[i])
# =============================================================================
# #output:
# number of elements = 5
# 10
# 20
# 30
# 40
# 50    
# =============================================================================
    
for elem in L:
    print(elem)
# =============================================================================
# #output:
# 10
# 20
# 30
# 40
# 50
# =============================================================================

#program to add the contents of two lists and store in another list
A = [10,20,30]
B = [1,2,3]
for i in range(len(A)):
    print(A[i] + B[i])
# =============================================================================
# #output:
# 11
# 22
# 33    
# =============================================================================

list = [1, 3, 5, 7, 9] 
for i, val in enumerate(list): 
    print (i, ",",val) 
# =============================================================================
# #output:
# 0 , 1
# 1 , 3
# 2 , 5
# 3 , 7
# 4 , 9
# =============================================================================

