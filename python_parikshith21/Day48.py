# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:00:16 2019

@author: Parikshith.H
"""

import numpy as np 
  
arr = np.array([[1, 5, 6], 
                [4, 7, 2], 
                [3, 1, 9]]) 
  

# sum of array elements 
print ("Sum of all array elements:", 
                            arr.sum()) 
  
# cumulative sum along each row 
print ("Cumulative sum along each row:\n", 
                        arr.cumsum(axis = 1)) 
# =============================================================================
# #output:
# Sum of all array elements: 38
# Cumulative sum along each row:
#  [[ 1  6 12]
#  [ 4 11 13]
#  [ 3  4 13]]
# =============================================================================
