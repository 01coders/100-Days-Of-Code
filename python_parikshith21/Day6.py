# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:20:24 2019

@author: Parikshith.H
"""

count=0
result=0
for count in range(1,10):
    result=result+count
    if result>6:
        break
print("result=",result)  
#output:10  (1,3,6,10 and 10>6 so break)

count=0
for count in range(0,10):
    if count<5:
        continue
    print(count) 
#output:5 6 7 8 9
    
for val in "string":
    if val == "i":
        break
    print(val)
print("The end")
# =============================================================================
# #output:
# s
# t
# r
# The end
# =============================================================================

for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")
# =============================================================================
# #output:
# s
# t
# r
# n
# g
# The end
# =============================================================================