# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:08:32 2019

@author: Parikshith.H
"""

class Date:
    def __init__(self,day,month,year):
        self.__day=day
        self.__month=month
        self.__year=year

    def get_day(self):
        return self.__day
    def get_month(self):
        return self.__month
    def get_year(self):
        return self.__year
    def set_day(self,value):
        self.__day=value
    def set_month(self,value):
        self.__month=value
    def set_year(self,value):
        self.__year=value

class customer:
    def __init__(self,name,num,dob):
        self.__name=name
        self.__num=num
        self.__dob=dob
        
    def get_name(self):
        return self.__name
    def get_num(self):
        return self.__num
    def get_dob(self):
        return self.__dob
    def set_name(self,value):
        self.__name=value
    def set_num(self,value):
        self.__num=value
    def set_dob(self,value):
        self.__dob=value
    
d=Date(13,11,1998)
c1=customer("Manoj",7204444566,d)
print(c1.get_name(),c1.get_num(),c1.get_dob().get_day()) #Manoj 7203344566 13
temp=c1.get_dob()
print(temp.get_day())  #13
temp.set_year(1999)
print(temp.get_day(),temp.get_month(),temp.get_year())  #13 11 1999
c1.get_dob().set_year(2000)
# =============================================================================
# #output:
# Manoj 7204444566 13
# 13
# 13 11 1999
# =============================================================================
