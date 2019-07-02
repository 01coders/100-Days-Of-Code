# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:51:07 2019

@author: Parikshith.H
"""

import numpy as np 
  

# Example to show sorting of structured array 
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)] 
  
# Values to be put in array 
values = [('Virat', 2009, 8.5), ('Ajay', 2008, 8.7),  
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)] 
             
# Creating array 
arr = np.array(values, dtype = dtypes) 
print ("\nArray sorted by names:\n", 
            np.sort(arr, order = 'name')) 
              
print ("Array sorted by grauation year and then cgpa:\n", 
                np.sort(arr, order = ['grad_year', 'cgpa'])) 

# =============================================================================
# #output:
# Array sorted by names:
#  [(b'Aakash', 2009, 9. ) (b'Ajay', 2008, 8.7) (b'Pankaj', 2008, 7.9)
#  (b'Virat', 2009, 8.5)]
# Array sorted by grauation year and then cgpa:
#  [(b'Pankaj', 2008, 7.9) (b'Ajay', 2008, 8.7) (b'Virat', 2009, 8.5)
#  (b'Aakash', 2009, 9. )]
# =============================================================================
