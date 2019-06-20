# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:00:22 2019

@author: Parikshith.H
"""

import numpy as np 
  
# Creating array from list with type float 
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float') 
print ("Array created using passed list:\n", a) 
# =============================================================================
# #output:
# Array created using passed list:
#  [[1. 2. 4.]
#  [5. 8. 7.]]
# =============================================================================
  
# Creating array from tuple 
b = np.array((1 , 3, 2)) 
print ("\nArray created using passed tuple:\n", b) 
# =============================================================================
# #output:
# Array created using passed tuple:
# [1 3 2]
# =============================================================================

# Creating a 3X4 array with all zeros 
c = np.zeros((3, 4)) 
print ("\nAn array initialized with all zeros:\n", c) 
# =============================================================================
# #output:
# An array initialized with all zeros:
#  [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
# =============================================================================
  
# Create a constant value array of complex type 
d = np.full((3, 3), 6, dtype = 'complex') 
print ("\nAn array initialized with all 6s." 
            "Array type is complex:\n", d) 
# =============================================================================
# #output:
# An array initialized with all 6s.Array type is complex:
#  [[6.+0.j 6.+0.j 6.+0.j]
#  [6.+0.j 6.+0.j 6.+0.j]
#  [6.+0.j 6.+0.j 6.+0.j]]
# =============================================================================
  

  
 