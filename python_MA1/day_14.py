#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 00:03:03 2019

@author: athreya
"""

#Vacation Caluclator
def hotel_cost(days):
  return 140 * days

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print (trip_cost("Los Angeles", 5, 600))
#1955

#Break & Continue
count=0
result=0
for count in range(1,10):
    result=result+count
    if result>6:
        break
print("result=",result)         #result=10

count=0
for count in range(0,10):
    if count<5:
        continue
    print(count)        #5,6,7,8,9

