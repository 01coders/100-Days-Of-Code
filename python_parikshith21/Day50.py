# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:17:53 2019

@author: Parikshith.H
"""

import numpy as np 
  
# create an array of sine values 
a = np.array([0, np.pi/2, np.pi]) 
print ("Sine values of array elements:", np.sin(a)) 
# =============================================================================
# #output:
# Sine values of array elements: [0.0000000e+00 1.0000000e+00 1.2246468e-16]
# =============================================================================
  
# exponential values 
a = np.array([0, 1, 2, 3]) 
print ("Exponent of array elements:", np.exp(a)) 
# =============================================================================
# #output:
# Exponent of array elements: [ 1.          2.71828183  7.3890561  20.08553692]
# =============================================================================

# square root of array values 
print ("Square root of array elements:", np.sqrt(a)) 
# =============================================================================
# #output:
# Square root of array elements: [0.         1.         1.41421356 1.73205081]
# =============================================================================
