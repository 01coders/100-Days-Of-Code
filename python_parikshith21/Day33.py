# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:56:32 2019

@author: Parikshith.H
"""

 
class A:
    def __init__(self,val1,val2):
        self.__a=val1
        self.__b=val2
    def display(self):
        print(self.__a,self.__b)
        
class B(A):
    def __init__(self,v1,v2,v3):
        super().__init__(v1,v2)
        self.__c=v3
    def display(self):
        super().display()
        print(self.__c)
        #print(self.__a)  #error
        
obj=B(10,20,30)
obj.display()  
# =============================================================================
# #output:
# 10 20
# 30
# =============================================================================
 

class A:
    def __init__(self,val1,val2):
        self.__a=val1
        self.b=val2
    def display(self):
        print(self.__a,self.b)
        
class B(A):
    def __init__(self,v1,v2,v3):
        super().__init__(v1,v2)
        self.__c=v3
    def display(self):
        super().display()
        print(self.__c)  
        print(self.b)   
        
obj=B(10,20,30)  
obj.display()   
# =============================================================================
# #output:
# 10 20 
# 30 
# 30
# =============================================================================
 