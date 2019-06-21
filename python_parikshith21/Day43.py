# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:55:45 2019

@author: Parikshith.H
"""

import numpy as np 
  
  
# Create an array with random values 
e = np.random.random((2, 2)) 
print ("\nA random array:\n", e) 
# =============================================================================
# #output:
# A random array:
#  [[0.15823576 0.59599377]
#  [0.55632106 0.87976667]]
# =============================================================================
  
# Create a sequence of integers  
# from 0 to 30 with steps of 5 
f = np.arange(0, 30, 5) 
print ("\nA sequential array with steps of 5:\n", f) 
# =============================================================================
# #output:
# A sequential array with steps of 5:
#  [ 0  5 10 15 20 25]
# =============================================================================
  
# Create a sequence of 10 values in range 0 to 5 
g = np.linspace(0, 5, 10) 
print ("\nA sequential array with 10 values between 0 and 5:\n", g) 
# =============================================================================
# #output:
# A sequential array with 10 values between 0 and 5:
#  [0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
#  3.33333333 3.88888889 4.44444444 5.        ]
# =============================================================================
  
# Reshaping 3X4 array to 2X2X3 array 
arr = np.array([[1, 2, 3, 4], 
                [5, 2, 4, 2], 
                [1, 2, 0, 1]]) 
  
newarr = arr.reshape(2, 2, 3) 
  
print ("\nOriginal array:\n", arr) 
print ("Reshaped array:\n", newarr) 
# =============================================================================
# #output:
# Original array:
#  [[1 2 3 4]
#  [5 2 4 2]
#  [1 2 0 1]]
# Reshaped array:
#  [[[1 2 3]
#   [4 5 2]]
# 
#  [[4 2 1]
#   [2 0 1]]]
# =============================================================================
  
# Flatten array 
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
flarr = arr.flatten() 
  
print ("\nOriginal array:\n", arr) 
print ("Fattened array:\n", flarr) 
# =============================================================================
# #output:
# Original array:
#  [[1 2 3]
#  [4 5 6]]
# Fattened array:
#  [1 2 3 4 5 6]
# =============================================================================
