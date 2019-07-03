# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:05:45 2019

@author: Parikshith.H
"""


import numpy as np 
  
a = np.array([[1, 2], 
              [3, 4]]) 
  
b = np.array([[5, 6], 
              [7, 8]]) 
  
# vertical stacking 
print("Vertical stacking:\n", np.vstack((a, b))) 
# =============================================================================
# #output:
# Vertical stacking:
#  [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
# =============================================================================
  
# horizontal stacking 
print("\nHorizontal stacking:\n", np.hstack((a, b))) 
# =============================================================================
# #output:
# Horizontal stacking:
#  [[1 2 5 6]
#  [3 4 7 8]]
# =============================================================================
