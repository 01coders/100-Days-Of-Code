# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 22:05:54 2019

@author: Parikshith.H
"""

class vehicle:
    def __init__(self,wheels,capacity,fuel):  
        self.w=wheels
        self.c=capacity
        self.f=fuel

    def display(self):
        print(self.w,self.c,self.f)
    
car=vehicle(4,15,'petrol')
car.display()
car=vehicle(4,5,'diesel')
car.display()        
# =============================================================================
# #output: 
# 4 15 petrol
# 4 5 diesel
# =============================================================================

bike=vehicle(2,5,'petrol')
bike.display() 
# =============================================================================
# #output: 
# 2 5 petrol
# =============================================================================


 
class vehicle:
    def __init__(self,wheels=0,capacity=0,fuel='diesel'): 
        self.w=wheels
        self.c=capacity
        self.f=fuel
    def assign(self,wheels,capacity,fuel):
        self.w=wheels
        self.c=capacity
        self.f=fuel
    def display(self):
        print(self.w,self.c,self.f)
        
car=vehicle(4,5,'petrol')
car.display()
# =============================================================================
# #output: 
# 4 5 petrol
# =============================================================================

bike=vehicle()
bike.display()
# =============================================================================
# #output: 
# 0 0 diesel
# =============================================================================

auto=vehicle()
auto.display()
# =============================================================================
# #output: 
# 0 0 diesel
# =============================================================================
 