# -*- coding: utf-8 -*-
"""
Created on Sun May 19 18:35:34 2019

@author: Parikshith.H
"""

#program to count number of o's in a string
str = "good morning"
count=0
for ch in str:   
    if (ch == 'o'):
        count+=1
print(count)
# =============================================================================
# #output:
# 3
# =============================================================================

#write a program to print a) to print first four characters of string
#                         b) to print morning
#                         c) to print substring present between @ and #
str="Good@morning#have a nice day"
print(str[:4])
print(str[5:12])
# =============================================================================
# #output:
# Good
# morning
# =============================================================================

index1=str.find('@')
index2=str.find('#')
print(str[index1+1:index2])
# =============================================================================
# #output:
# morning
# =============================================================================

str="Go#od@morning#have a nice day"
index1=str.find('@')
index2=str.find('#')
print(str[index1+1:index2]) #no out put as # is before @ 
# =============================================================================
# #output:
# no out put as # is before @ 
# =============================================================================

str="Go#od@morning#have a nice day"
index1=str.find('@')
index2=str.find('#',index1)
print(str[index1+1:index2]) 
# =============================================================================
# #output:
# morning
# =============================================================================