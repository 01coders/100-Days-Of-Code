# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:06:57 2019

@author: Parikshith.H
"""

class vehicle:
    def create(self,wheels): 
        self.w = wheels 
        
    def display(self):
        print("num of wheels are:",self.w)

bike=vehicle()
bike.create(2)
bike.display()
# =============================================================================
# #output: 
# num of wheels are: 2
# =============================================================================

car=vehicle()
car.create(4)
car.display()
# =============================================================================
# #output: 
# num of wheels are: 4
# =============================================================================

class vehicle:
    def __init__(self): #it is a default method called when an object is creted
        self.w=None
        self.c=None
        self.f='petrol'
        
    
    def assign(self,wheels,capacity,fuel):
        self.w=wheels
        self.c=capacity
        self.f=fuel
    def display(self):
        print(self.w,self.c,self.f)
        
bike = vehicle()
bike.assign(2,10,'petrol')
bike.display()
# =============================================================================
# #output:
# 2 10 petrol
# =============================================================================

car = vehicle()
car.display()
# =============================================================================
# #output: 
# None None petrol
# =============================================================================
