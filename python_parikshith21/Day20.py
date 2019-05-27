# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:58:14 2019

@author: Parikshith.H
"""

#program to count the occurence of word 'day' in a string
str = "have a nice day enjoy the day manoj"
l = str.split()
print(l)
count = 0
for elem in l:
    if elem == 'day':
        count+=1
print(count)   
# =============================================================================
# #output:
# ['have', 'a', 'nice', 'day', 'enjoy', 'the', 'day', 'manoj']
# 2
# =============================================================================
 
#program to print all words and their length in a string
str1 = "This is python class"
count=0
l1=str1.split()
for elem in l1:
    print(elem,":",len(elem))  
# =============================================================================
# #output:
# This : 4
# is : 2
# python : 6
# class : 5
# =============================================================================

 
#program to print longest word in a string
str1 = "This is python class"
length=0
longest=None
l1=str1.split()
for word in l1:
    if longest == None or len(longest) < len(word):
        longest = word
print("The longest word is:",longest)
print("The length is:",len(longest)) 
# =============================================================================
# #output:
# The longest word is: python
# The length is: 6
# =============================================================================
 
 
#Program to create a list with user entered values
l = list()
n=int(input("Enter the number of elements:"))
for i in range(n):
    #l[i]=input()   #error
    elem=input()
    l.append(elem)
print(l)      
# =============================================================================
# #output: 
# Enter the number of elements:3
# 1
# 2
# 3
# ['1', '2', '3']
# =============================================================================
 

#Program to create a list with user entered values without for loop
l1=list()
while(True):
    elem=input()
    if elem=="exit":
        break
    else:
        l1.append(elem)
print(l1)   
# =============================================================================
# #output: 
# 1
# 2
# 3
# 4
# 5
# exit
# ['1', '2', '3', '4', '5']
# =============================================================================
 
    
#Program to find sum and average of elements in a list
l=list()
while(True):
    elem=(input("Enter values:"))
    if elem=="exit":
        break
    else:
        l.append(float(elem))
print(l)
print("The sum is:",sum(l))
print("The average is:",sum(l)/len(l))
# =============================================================================
# #output:
# Enter values:2
# Enter values:3
# Enter values:4
# Enter values:3
# Enter values:2
# Enter values:exit
# [2.0, 3.0, 4.0, 3.0, 2.0]
# The sum is: 14.0
# The average is: 2.8
# =============================================================================