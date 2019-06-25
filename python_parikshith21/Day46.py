# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 14:33:03 2019

@author: Parikshith.H
"""

import numpy as np 
  
arr = np.array([[1, 5, 6], 
                [4, 7, 2], 
                [3, 1, 9]]) 
  
# maximum element of array 
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:", 
                    arr.max(axis = 1)) 
  
# minimum element of array 
print ("Column-wise minimum elements:", 
                        arr.min(axis = 0)) 
  
# =============================================================================
# #ouptut:
# Largest element is: 9
# Row-wise maximum elements: [6 7 9]
# Column-wise minimum elements: [1 1 2]
# =============================================================================
