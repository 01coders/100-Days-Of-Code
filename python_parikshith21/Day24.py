# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:33:16 2019

@author: Parikshith.H
"""

#tuples can be used on both RHS and LHS of an expression
l=['hi','hello']
(a,b)=l
print(a)    
print(b)   
print(type(a))  
# =============================================================================
# #output:
# hi
# hello
# <class 'str'>
# =============================================================================


x,y=l
print(x)  
print(y)  
print(type(y))  
# =============================================================================
# #output:
# hi
# hello
# <class 'str'>
# =============================================================================

(p,q)=10,20
print(p)  #10
# =============================================================================
# #output:
# 10
# =============================================================================

#Progarm to print the words in a sentence in decending order of their length
#convert the string into an list of array using split function
#find the length of each word and store
#sort the elements
#display

txt = "but soft what light in yonder window breaks"
temp_list = list() 
res_list=list() 
l=txt.split()
print(l)
for word in l:
    temp_list.append((len(word),word))
print(temp_list)
temp_list.sort()
print(temp_list)
for length,wd in temp_list:
    res_list.append(wd)
print(res_list)
# =============================================================================
# #output:
# ['but', 'soft', 'what', 'light', 'in', 'yonder', 'window', 'breaks']
# [(3, 'but'), (4, 'soft'), (4, 'what'), (5, 'light'), (2, 'in'), (6, 'yonder'),
#  (6, 'window'), (6, 'breaks')]
# [(2, 'in'), (3, 'but'), (4, 'soft'), (4, 'what'), (5, 'light'), (6, 'breaks'),
#  (6, 'window'), (6, 'yonder')]
#['in', 'but', 'soft', 'what', 'light', 'breaks', 'window', 'yonder']
# =============================================================================