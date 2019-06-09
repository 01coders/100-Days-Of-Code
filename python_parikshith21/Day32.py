# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:06:53 2019

@author: Parikshith.H
"""

 
class customer:
    def __init__(self):
        self.__id=None
        self.__name=None
        self.__num=None
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_num(self):
        return self.__num

    def set_id(self,id):
        self.__id=id
    def set_name(self,name):
        self.__name=name
    def set_num(self,num):
        self.__num=num
        
c1=customer()
c1.set_id(24)
c1.set_name('xyz')
c1.set_num(9978798978)
print('The customer details are')
print('Name:',c1.get_name())
print('Id:',c1.get_id())
print('Num:',c1.get_num())

# =============================================================================
# #output:
# The customer details are
# Name: xyz
# Id: 24
# Num: 9978798978
# =============================================================================
 