# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:20:13 2019

@author: Parikshith.H
"""

import numpy as np 
  
# Creating array object 
arr = np.array( [[ 1, 2, 3], 
                 [ 4, 2, 5]] ) 
  
# Printing type of arr object 
print("Array is of type: ", type(arr)) 
# =============================================================================
# #output:
# Array is of type:  <class 'numpy.ndarray'>
# =============================================================================
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", arr.ndim) 
# =============================================================================
# #output:
# No. of dimensions:  2
# =============================================================================
  
# Printing shape of array 
print("Shape of array: ", arr.shape) 
# =============================================================================
# #output:
# Shape of array:  (2, 3)
# =============================================================================
  
# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 
# =============================================================================
# #output:
# Size of array:  6
# =============================================================================
  
# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 
# =============================================================================
# #output:
# Array stores elements of type:  int32
# =============================================================================

