# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 23:50:56 2019

@author: Parikshith.H
"""

import numpy as np 
  
a = np.array([[1, 4, 2], 
                 [3, 4, 6], 
              [0, -1, 5]]) 
  
# sorted array 
print ("Array elements in sorted order:\n", 
                    np.sort(a, axis = None)) 
  
# sort array row-wise 
print ("Row-wise sorted array:\n", 
                np.sort(a, axis = 1)) 
  
# specify sort algorithm 
print ("Column wise sort by applying merge-sort:\n", 
            np.sort(a, axis = 0, kind = 'mergesort')) 
  
# =============================================================================
# #output:
# Array elements in sorted order:
#  [-1  0  1  2  3  4  4  5  6]
# Row-wise sorted array:
#  [[ 1  2  4]
#  [ 3  4  6]
#  [-1  0  5]]
# Column wise sort by applying merge-sort:
#  [[ 0 -1  2]
#  [ 1  4  5]
#  [ 3  4  6]]
# =============================================================================
