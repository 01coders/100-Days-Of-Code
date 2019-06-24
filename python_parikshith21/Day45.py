# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:32:56 2019

@author: Parikshith.H
"""

import numpy as np 
  
a = np.array([1, 2, 5, 3]) 
  
  
# square each element 
print ("Squaring each element:", a**2) 
  
# modify existing array 
a *= 2
print ("Doubled each element of original array:", a) 
  
# transpose of array 
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
  
print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T) 

# =============================================================================
# #output:
# Squaring each element: [ 1  4 25  9]
# Doubled each element of original array: [ 2  4 10  6]
# 
# Original array:
#  [[1 2 3]
#  [3 4 5]
#  [9 6 0]]
# Transpose of array:
#  [[1 3 9]
#  [2 4 6]
#  [3 5 0]]
# =============================================================================
