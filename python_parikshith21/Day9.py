# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:19:13 2019

@author: Parikshith.H
"""

 
str = "Python"
print(str)
print(str[0])
ch = str[1]
print(ch)
# =============================================================================
# #output:
# Python
# P
# y
# =============================================================================


str = "Python"
print(str[1:4])
# =============================================================================
# #output:
# yth
# =============================================================================


str2 = str[1:5]
print(str2)
# =============================================================================
# #output:
# ytho
# =============================================================================


str = "Python"
print(str)
str = "python.py"  #entire string is changed
print(str)      
print(str[1:4])
print(str)   #original string remains same
# =============================================================================
# #output:
# Python
# python.py
# yth
# python.py
# =============================================================================

s = "good morning"
print(s[1:])
print(s[:8])
print(s[:10])
print(s[0:8])
print(s[0:8:2]) #here increment by 2
print(s[9:1:-1]) #starting index is 9,ending index is 2,-1 is reverse order
print(s[9:1:-3])
print(s[: : -1])
# =============================================================================
# #output:
# ood morning
# good mor
# good morni
# good mor
# go o
# inrom do
# iod
# gninrom doog
# =============================================================================
