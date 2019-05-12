"""
Created on May 11 20:45:13 2019

@author: Manoj Athreya A
"""

str1 = "ABaBCbGc"
str2 = str1.upper();
d=dict()
for ch in str2:
    if ch not in d:
        d[ch]=1
    else:
        d[ch]=d[ch]+1
for key in d:
    print(key,d[key])

# =============================================================================
# OUTPUT:
# A 2
# B 3
# C 2
# G 1
# =============================================================================

str1 = "I Like C"
str2 = "Mary Likes Python"
str3 = str1 + str2
print(str3)
merged=""
for ch in str3:
    if ch.isupper():
        merged=merged+ch
print("Merged string containing capital letters from both strings is:",merged)


# =============================================================================
# OUTPUT:
# I Like CMary Likes Python
# Merged string containing capital letters from both strings is: ILCMLP
# =============================================================================

lst = [["Sofa set",20000],["Dining table",8500],["T.V. Stand",4599],["Cupboard",13920]]

item = input("Enter ITEM to be purchased > ")
index=0
for i,l2 in enumerate(lst):
   if item in l2:
       index = i
if item in [j for i in lst for j in i]:
   qnt = int(input("Enter Quantity: "))
   if qnt > 0:
       print("Bill amount is:Rs",qnt*lst[index][1])
   else:
       print("Bill amount is:Rs 0")
else:
   print("Item Not Available")
   
=============================================
# OUTPUT:
# Enter ITEM to be purchased > Sofa set
#
# Enter Quantity: 4
# Bill amount is:Rs 80000
=============================================
