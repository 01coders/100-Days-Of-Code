# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:50:42 2019

@author: Parikshith.H
"""

fout = open('output.txt','w')
line1 = "This is the first line\n"
fout.write(line1)
line2 = "This is the second line"
fout.write(line2)
fout.close()


 
try:
    fout = open('output.txt','w')
    line1 = "This is the first line\n"
    fout.write(line1)
    line2 = "This is the second line"
    fout.write(line2)
    fout.close()
except:
    print("file cannot be opened")
    
# =============================================================================
# #output:
# In "output.txt" file
# =============================================================================
