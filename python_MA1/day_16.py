#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:16:11 2019

@author: athreya
"""

str="hello"
if str=="hi":
    print('true block')
else:
    print('false block')
    
#false block

if str<"hi":
    print("true 2")
else:
    print("false 2")
    
#true 2

if 'e' in "hello":
    print("true 3")
else:
    print("false 3")

#true 3
    
s = "welcome"
for ch in s:
    print(ch)
# welcome vertically
    
for val in "hello":
    print(val)
#hello vertically
    
#program on class
class vehicle:
    def create(self,wheels):
        self.w = wheels
        
    def display(self):
        print("No.of wheels are:", self.w)

bike=vehicle()
bike.create(2)
bike.display()

#No.of wheels are: 2
