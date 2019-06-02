#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 21:05:00 2019

@author: athreya
"""

c=7//7      #Truncate division
print(c)    #1

c=7/7       #case1: int/int=float
print(c)    #1.0

c=3/2       
print(c)    #1.5

c=3//2       #case2: int//int=int
print(c)    #1

c=7.7/7     #case3: float/int=float
print(c)    #1.1

c=7.7//7   #case4: float//int=float
print(c)    #1.0

c=(200-70)*10/5
print(c)            #260.0

c=5*1**2        #1power2=1 and 1*5=5
print(c)        #5

c=True          #boolean value
print(c)        #True

c=not True
print(c)        #False

c="True"        #string True
print(c) 

c=not "True"    #string 
print(c)        #False

c=not "False"   #ascii value converted it to false.
print(c)        #False