# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:16:39 2019

@author: Parikshith.H
"""

#***********Variables***********#
c = 11%9
print(c)     #2
 
c = -11%9    #9*2=18 18-11=7 #remainder cannot be negative
print(c)    #7
 
c = 7//7
print(c)    #1
 
c = 7/7
print(c)    #1.0
 
c = 3/2   #3/2 answer is 1.5(floating) 
print(c)    #1.5

c = 3//2  #3//2 truncate division answer is 1 int//int=int
print(c)    #1

c = 7.7/7  #7.7/7 answer is 1.1(floating)
print(c)    #1.1
 
c = 7.7//7 #7.7//7 answer is 1.0 exception float//int=float.0
print(c)    #1.0

c=5*1**2  #precedence 1^2=1 then 5*1=5
print(c)   #5

c=True  #boolean value true
print(c)    #True

c=not True #it means not 1 => 0 so false
print(c)    #False

c="True"  #string
print(c)    #True

c=not "True"  #answer is false, it is not of ascii value => 0 so false (~1=0)
print(c)      #~ of any value other than 0 is 0 i.e ~1=0
#output:False

c=not False #it means not 0 => 1 so true
print(c)    #True

c=not "False"  #answer is false, it is not o ascii value => 0 so false (~1=0)
print(c)    #False