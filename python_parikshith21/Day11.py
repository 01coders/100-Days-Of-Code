# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:30:47 2019

@author: Parikshith.H
"""

str="hello"
p=str.upper()
print(p)
print(str)
# =============================================================================
# #output:
# HELLO
# hello
# =============================================================================


index=str.find('l')
print(index) #finds char in string and will return the index of first occurance
# =============================================================================
# #output:
# 2
# =============================================================================

index=str.find('lo')
print(index) #returns the starting index of substring
# =============================================================================
# #output:
# 3
# =============================================================================


str2="  good morning  "
p=str2.strip() #removes leading white spaces only
print(p)
# =============================================================================
# #output:
# good morning
# =============================================================================

str3="good morning"
index=str3.find('o')
print(index)
index=str3.find('o',4) #start search 'o' from index 4 onwards
print(index)
# =============================================================================
# #outptut:
# 1
# 6
# =============================================================================

str4="Good morning"
if str4.startswith("Good"):
    print("true")
else:
    print("false")
# =============================================================================
# #output:
# true
# =============================================================================