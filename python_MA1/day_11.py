#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:59:47 2019

@author: athreya
"""

# Sample Program1
original = input("Enter a word:")
if(len(original)>0):
  print(original)
else:
  print("empty")
  
#Sample Program2
x='maps'
if(len(x)>0 and len(x)>1):
  print(x)
else:
  print("empty")
a=x.isalpha()
print(a)

#Sample Program3
original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  print(word)
  print(first)
else:
    print ('empty')
#maps
#m
    
#Sample Program4
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  print(new_word)
else:
    print('empty')
#Output
#Enter a word:MAPS
#mapsmay
    
