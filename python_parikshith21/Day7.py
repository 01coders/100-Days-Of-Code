# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:27:54 2019

@author: Parikshith.H
"""

for x in "banana":
  print(x)
# =============================================================================
# #output:
# b
# a
# n
# a
# n
# a
# =============================================================================
 
for index in [10,20,30,40]:  
    print("python")       
    print(index)   
# =============================================================================
# #output:
# python
# 10
# python
# 20
# python
# 30
# python
# 40
# =============================================================================

 
l = [10,20,30,40]
for index in l:
    print("hi")
    print(index)
# =============================================================================
# #output:
# hi
# 10
# hi
# 20
# hi
# 30
# hi
# 40
# =============================================================================
  
    
l2 = [10,20,"welcome",40.5,"End"]
for index in l2:
   print("hello")
   print(index)
# =============================================================================
# #output:
# hello
# 10
# hello
# 20
# hello
# welcome
# hello
# 40.5
# hello
# End
# =============================================================================
  
  
#write a program to add all the elements in a list
l = [10,20,30,40]
sum = 0
for index in l:
    sum = sum + index
print(sum)
# =============================================================================
# #output:
# 100
# =============================================================================
 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# =============================================================================
# #output:
# apple
# =============================================================================