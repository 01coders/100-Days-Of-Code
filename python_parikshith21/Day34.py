# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:43:35 2019

@author: Parikshith.H
"""

class customer:
    __counter=1000
    def __init__(self,NAME,NUM):
        self.__id=customer.__counter+1
        self.__name=NAME
        self.__num=NUM
        customer.__counter=customer.__counter+1
        
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_num(self):
        return self.__num
    def set_id(self):
        return self.__id
    def set_name(self):
        return self.__name
    def set_num(self):
        return self.__num

class privilaged_customer(customer):
    def __init__(self,NAME,NUM,DISCOUNT):
        super().__init__(NAME,NUM)
        self.discount=DISCOUNT

c1=privilaged_customer('abc',15,10)
print(c1.discount)  
print(c1.get_id(),c1.get_name(),c1.get_num())  
# =============================================================================
# #output:
# 10
# 1001 abc 15
# =============================================================================
