# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:17:23 2019

@author: Parikshith.H
"""

import re

print(".........................................")
line = "XYZ: 808.4.5.00"
if re.search("808",line):  #search for a pattern in a string
    print("True")  #output: True
if re.search('[0-9]+',line):
    print("True2") #output: True2
# =============================================================================
# #output:
# .........................................
# True
# True2
# =============================================================================

 
line='xyz@gmail.com,abc@gmail.com,this@gmail.com'
l=re.findall('[a-z]+@gmail.com',line)
print(l)
# =============================================================================
# #output:
# ['xyz@gmail.com', 'abc@gmail.com', 'this@gmail.com']
# =============================================================================
 
str=re.search('[a-z]+@gmail.com',line) #search and return first one
print(str)
# =============================================================================
# #output:
# <re.Match object; span=(0, 13), match='xyz@gmail.com'>
# =============================================================================

 
str1=re.search('[a-z]+@gmail.com',line).group()
print(str1)
# =============================================================================
# #output:
# xyz@gmail.com
# =============================================================================
