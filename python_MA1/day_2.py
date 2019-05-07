#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 23:45:40 2019

@author: athreya
"""

#create a simple calculator that determines the price of a meal after tax and tip.
meal = 44.50
tax = 0.0675
tip = 0.15
meal+=meal*tax
total=meal+meal*tip
print(total)               #54.6293125

#String:  A string can contain letters, numbers, and symbols.

name = "Ryan"
age = "19"
food = "cheese"

#Escaping Character
#'There\'s a snake in my boot!'

#INDEX

fifth_letter = "MORNING"[4]
print(fifth_letter)                #I

#String Methods

parrot = "Norwegian Blue"
print(len(parrot))            #14

mango = "ALphonsO"
print(mango.lower())     #alphonso

mango = "ALphonsO"
print(mango.upper())   #ALPHONSO

pi = 3.14
print(str(pi))          #3.14

#STRING CONCATENATION
print("Spam " + "and " + "eggs")    #Spam and eggs

#Explicit String Conversion
#Sometimes you need to combine a string with something that isn’t a string. 

print("The value of pi is around " + str(3.14))
#The value of pi is around 3.14

#String Formatting with %

name = "MA1"
print("Hello %s" % (name))

day = 6
print("03 - %s - 2019" %  (day))
# 03 - 6 - 2019
print("03 - %02d - 2019" % (day))
# 03 - 06 - 2019

name = 'MA1'
color = 'BLACK'
print("Ah, so your name is %s and your favorite color is %s." % (name, color))
#Ah, so your name is MA1 and your favorite color is BLACK.

my_string = "Hello People!!"
print(len(my_string))                   #14
print(my_string.upper())                #HELLO PEOPLE!!
print(my_string.lower())                #hello people!!



