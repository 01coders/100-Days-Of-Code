# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:06:01 2019

@author: Parikshith.H
"""

import numpy as np 
  
a = np.array([[1, 2], 
              [3, 4]]) 
  
b = np.array([[5, 6], 
              [7, 8]]) 

c = [5, 6] 
  
# stacking columns 
print("\nColumn stacking:\n", np.column_stack((a, c))) 
# =============================================================================
# #output:
# Column stacking:
#  [[1 2 5]
#  [3 4 6]]
# =============================================================================
  
# concatenation method  
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1)) 
# =============================================================================
# #output:
# Concatenating to 2nd axis:
#  [[1 2 5 6]
#  [3 4 7 8]]
# =============================================================================
