#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:15:37 2019

@author: athreya
"""

#1
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print ("With tax: %f" % bill)
  return bill

#2
def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print ("With tip: %f" % bill)
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)            #108.00
meal_with_tip = tip(meal_with_tax)        #124.20

#Functions 3
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print ("%d squared is %d." % (n, squared))
  return squared
square(10)                 #100

#4
def power(base,exponent):
  result = base ** exponent
  print ("%d to the power of %d is %d." % (base, exponent, result))

power(5,3)  #5 to the power of 3 is 125.

#5
import math
print(math.sqrt(25))   #5.0

#from math import *   //imports all math functions

#6
def biggest_number(*args):
  print (max(args))
  return max(args)
    
def smallest_number(*args):
  print (min(args))
  return min(args)

def distance_from_zero(arg):
  print (abs(arg))
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#OUTPUT
#10
#-10
#10


