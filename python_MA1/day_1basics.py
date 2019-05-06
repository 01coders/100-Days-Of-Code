#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:14:57 2019

@author: athreya
"""

#Python Programming

#Print function: Prints the given text within single/double quotes

print('Hi wecome to Python!')
#Hi wecome to Python!
print("Hello World")
#Hello World

#Strings: Text in Python is considered a specific type of data called a string. 

print("Hello World this is Manoj")
#Hello World this is Manoj
print('Here is the place where you can learn python')
#Here is the place where you can learn python
print("Hello" + "Python")
#HelloPython

#Multi-line Strings

pond='''The old pond,
A frog jumps in:
Plop!'''

#Variables: Deals with data that changes over time.

todays_date = "May 06, 2019"
print(todays_date)
todays_date = "May 07, 2019"
print(todays_date)

#Arithmetic Operations

add=3+2
sub=7-5
mul=5*5
div=7/3
mod=9%2
print(add,sub,mul,div,mod)          #5 2 25 2.3333333333333335 1

a=5/3
b=float(5)/float(3)
print(int(a))               #1
print(b)                #1.6666666666667                

#Numbers

#Create a new variable called total_cost which is the product of how many
#cucumbers you are going to buy and the cost per cucumber
cucumbers=7
price_per_cucumber=3.25
total_cost=cucumbers*price_per_cucumber
print(total_cost)
#22.75

a=55
b=6
c=float(a/b)
print(c)          #9.1666666666666666666666

#Booleans
#True or False value

skill_completed = "Python Syntax"
exercises_completed = 13
points_per_exercise = 5
point_total = 100
point_total += exercises_completed*points_per_exercise

print("I got "+str(point_total)+" points!")
#I got 165 points


