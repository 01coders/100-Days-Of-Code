# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:14:11 2019

@author: Parikshith.H
"""

 
class vehicle:
    num=10   #class variables/static variables-assigned a value inside class declaration
    #static variable does not belong to object it belongs to class
    #static variable is shared among objects
    #static variables exists throughout the program
    def __init__(self,w,t):
        self.__wheel=w
        self.__type=t
        self.__number=vehicle.num
        vehicle.num=vehicle.num+1
         
    def display(self):
        print(self.__wheel,self.__type,self.__number)
        
print(vehicle.num) 
car1=vehicle(4,'petrol')
car1.display()  
# =============================================================================
# #output:
# 10
# 4 petrol 10
# =============================================================================

print(vehicle.num) 
car2=vehicle(4,'diesel')
car2.display()  
# =============================================================================
# #output:
# 11
# 4 diesel 11
# =============================================================================
print(vehicle.num) 
# =============================================================================
# #output:
# 12
# =============================================================================
 


class student:
    id=1
    def __init__(self,n,ph):
        self.__name=n
        self.__phone=ph
        self.__usn='4VV16CS' + str(student.id)
        student.id=student.id+1
    def display(self):
        print(self.__name,self.__phone,self.__usn)
        
student1=student('a',9988776655)
student1.display()  
# =============================================================================
# #output: 
# a 9988776655 4VV16CS1
# =============================================================================

student2=student('b',9966554433)
student2.display()  
# =============================================================================
# #output:
# b 9966554433 4VV16CS2
# =============================================================================
