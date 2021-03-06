# -*- coding: utf-8 -*-
"""
Created on Wed May 14 19:00:32 2019

@author: Parikshith.H
"""

counter = 1
while counter<=3:
    print(counter)
    counter+=1
print("end")
# =============================================================================
# #output:
# 1
# 2
# 3
# end
# =============================================================================
 
for i in range(10):
    print(i)   #range is 0 to 9
# =============================================================================
# #output:0
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# =============================================================================

for i in range(1,12):
    print(i)   #1 to 11  ((12-1)=> 11 times executed)
# =============================================================================
# #output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# =============================================================================

for i in range(1,12,2): #increment in terms of 2
    print(i) 
# =============================================================================
# #output: 1 3 5 7 9 11   
# =============================================================================


for i in range(1,12,3): #increment in terms of 3
    print(i) 
# =============================================================================
# #output: 1 4 7 10
# =============================================================================


for j in range(12,1,-2):  #to decrement loop in reverse
    print(j) 
# =============================================================================
# #output 12 10 8 6 4 2
# =============================================================================
 
 
#program to find sum of 1st n natural numbers
n=10
sum = 0
for counter in range(1,n+1):
    sum = sum + counter
print(sum)
# =============================================================================
# #output: 55
# =============================================================================

n= 20
sum = 0
while n!=0:
    sum = sum + n
    n=n-1
print(sum)
# =============================================================================
# #output:210
# =============================================================================
 
n=100
sum=0
counter=1
while counter<=n:
    sum =sum+counter
    counter+=1
print(sum)
# =============================================================================
# #output:5050
# =============================================================================
