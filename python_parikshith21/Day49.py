# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 7:33:03 2019

@author: Parikshith.H
"""

import numpy as np 
  
a = np.array([[1, 2], 
            [3, 4]]) 
b = np.array([[4, 3], 
            [2, 1]]) 
  
# add arrays 
print ("Array sum:\n", a + b) 
# =============================================================================
# #output:
# Array sum:
#  [[5 5]
#  [5 5]]
# =============================================================================

  
# multiply arrays (elementwise multiplication) 
print ("Array multiplication:\n", a*b) 
# =============================================================================
# #output:
# Array multiplication:
#  [[4 6]
#  [6 4]]
# =============================================================================

  
# matrix multiplication 
print ("Matrix multiplication:\n", a.dot(b)) 
# =============================================================================
# #output:
# Matrix multiplication:
#  [[ 8  5]
#  [20 13]]
# =============================================================================
