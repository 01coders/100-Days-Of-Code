# -*- coding: utf-8 -*-
"""
Created on Mon May 20 19:44:26 2019

@author: Parikshith.H
"""
fhand = open('input.txt') #open will open the file if no option then it is 
                          # opened in read mode
inp = fhand.read() #reads entire contents of file
print(inp)
# =============================================================================
# #output:
# This is python class conducted@mysuru conducted@mysuru conducted@mysuru
# From: BNMNBXV 123123e12 qwdsadaw
# From: ASDFVDS 123241431 dfsgdfsf
# From: ZVFGFSF 765787676 nivdnnnv
# =============================================================================

 
fhand = open('input.txt')
for line in fhand:    #loop iterates as many number of lines are in file
    print(line) #each time for loop runs the first line is taken as string
    print("********")
# =============================================================================
# #output:
# This is python class conducted@mysuru conducted@mysuru conducted@mysuru
# 
# ********
# From: BNMNBXV 123123e12 qwdsadaw
# 
# ********
# From: ASDFVDS 123241431 dfsgdfsf
# 
# ********
# From: ZVFGFSF 765787676 nivdnnnv
# ********
# =============================================================================

 
count=0
fhand = open('input.txt')
for line in fhand:
    count = count+1  #to find number of lines in file
print(count)
# =============================================================================
# #output:
# 4
# =============================================================================

 
fhand = open('input.txt')
inp = fhand.read()  #inp is a string
print(inp)
print(len(inp))
print(inp[0:10])
print(inp[::-1])  #print in reverse
print(inp[:10:-1])
# =============================================================================
# #output:
# This is python class conducted@mysuru conducted@mysuru conducted@mysuru
# From: BNMNBXV 123123e12 qwdsadaw
# From: ASDFVDS 123241431 dfsgdfsf
# From: ZVFGFSF 765787676 nivdnnnv
# 170
# This is py
# vnnndvin 676787567 FSFGFVZ :morF
# fsfdgsfd 134142321 SDVFDSA :morF
# wadasdwq 21e321321 VXBNMNB :morF
# urusym@detcudnoc urusym@detcudnoc urusym@detcudnoc ssalc nohtyp si sihT
# vnnndvin 676787567 FSFGFVZ :morF
# fsfdgsfd 134142321 SDVFDSA :morF
# wadasdwq 21e321321 VXBNMNB :morF
# urusym@detcudnoc urusym@detcudnoc urusym@detcudnoc ssalc noh
# =============================================================================
 
 

N = int(input("Enter the number of lines:"))
count = 0
fhand = open("input.txt")
for line in fhand:
    count+=1
    if count < N:
        print(line)
# =============================================================================
# #output:
# Enter the number of lines:2
# This is python class conducted@mysuru conducted@mysuru conducted@mysuru
# =============================================================================