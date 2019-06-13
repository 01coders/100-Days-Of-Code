# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 20:21:05 2019

@author: Parikshith.H
"""

class student:
    id=100
    def __init__(self,n,ph):
        self.__name=n
        self.__phone=ph
        self.__usn='4VV16CS' + str(student.id)
        student.id=student.id+1
    def display(self):
        print(self.__name,self.__phone,self.__usn)
    
    @staticmethod   #no need self for static methods
    def totalstudents():
        return (student.id-100)
    #static methods must access only static/class variables
        
student1=student('a',9988776655)
student1.display()  
# =============================================================================
# #output: 
# a 9988776655 4VV16CS100
# =============================================================================

student2=student('b',9966554433)
student2.display()  
# =============================================================================
# #output
# b 9966554433 4VV16CS101
# =============================================================================

T=student.totalstudents()
print("total number of students is:",T ) 
# =============================================================================
# #output 
# total number of students is: 2
# =============================================================================
