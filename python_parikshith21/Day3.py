# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:23:20 2019

@author: Parikshith.H
"""

#*********Variable-inputs**********#
a = input("Enter first input:")
b = input("Enter second input:")
c = a + b
print("Sum is",c)

#output:Enter first input:2
       #Enter second input:4
       #Sum is 24
       
p = input("Enter a value:") #every input from user is treated as string
print(type(p))
#output:Enter a value:2
        #<class 'str'>
        
p = int(input("Enter a value:"))
print(type(p))
#output:Enter a value:2
       #<class 'int'>