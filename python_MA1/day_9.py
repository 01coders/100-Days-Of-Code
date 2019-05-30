#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:28:55 2019

@author: athreya
"""

from datetime import datetime

now=datetime.now()
print(now)
#2019-05-30 19:29:23.478768

now=datetime.now()
print(now.year)         #2019
print(now.month)        #5
print(now.day)          #30

print('%02d/%02d/%04d' % (now.month, now.day, now.year))
#05/30/2019

print('%s:%s:%s' % (now.hour, now.minute, now.second))
#19:37:11

#Program

def deathdoor():
    print("You've just entered the deathdoor!")
    print ("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print ("You have got a chance on Earth again!!!")
    elif answer == "right" or answer == "r":
        print ("You are in Heaven!!!")
    else:
        print ("You didn't pick left or right! Try again.")
        deathdoor()

deathdoor()

# =============================================================================
# You've just entered the deathdoor!
# Do you take the door on the left or the right?
# 
# Type left or right and hit 'Enter'.l
# You have got a chance on Earth again!!!
# 
# Type left or right and hit 'Enter'.r
# You are in Heaven!!!
# =============================================================================

