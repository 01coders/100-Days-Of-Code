# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:37:39 2019

@author: Parikshith.H
"""

str="hello"
if str=="hi":
    print("true")
else:
    print("false")
# =============================================================================
# #output:
# false
# =============================================================================


if str < "hi":
    print("true")
else:
    print("false")
# =============================================================================
# #output:
# true
# =============================================================================

if 'e' in "hello":          #to check a character present in string or not
    print("true")
else:
    print("false")
# =============================================================================
# #output:
# true
# =============================================================================
    
s = "welcome"
for ch in s:
    print(ch)
# =============================================================================
# #output:
# w
# e
# l
# c
# o
# m
# e
# =============================================================================

for val in "hello":
    print(val)
# =============================================================================
# #output:
# h
# e
# l
# l
# o
# =============================================================================
    

fruit1 = input('Please enter the name of first fruit:\n')
fruit2 = input('Please enter the name of second fruit:\n')

if fruit1 < fruit2:
    print(fruit1 + " comes before " + fruit2 + " in the dictionary.")
elif fruit1 > fruit2:
    print(fruit1 + " comes after " + fruit2 + " in the dictionary.")
else:
    print(fruit1 + " and " + fruit2 + " are same.")
# =============================================================================
# #output:
# Please enter the name of first fruit:
# apple
# 
# Please enter the name of second fruit:
# cherry
# apple comes before cherry in the dictionary.
# =============================================================================
