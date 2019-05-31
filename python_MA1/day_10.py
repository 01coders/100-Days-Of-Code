#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:35:40 2019

@author: athreya
"""

# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

answer = "Left"
if answer == "Left":
    print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    
 
#Sample Program
def using_control_once():
    if (3>=3):
        return "Success #1"

def using_control_again():
    if (2>1):
        return "Success #2"

print (using_control_once())
print (using_control_again())

#Sample Program
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))          #1
print (greater_less_equal_5(5))          #0
print (greater_less_equal_5(6))          #-1


#Sample Program
def grade_converter(grade):
    if (grade>=90):
        return "A"
    elif (grade>=80):
        return "B"
    elif (grade>=70):
        return "C"
    elif (grade>=65):
        return "D"
    else:
        return "F"
      
# This prints "A"      
print (grade_converter(92))

# This prints "C"
print (grade_converter(70))

# This prints "F"
print (grade_converter(61))