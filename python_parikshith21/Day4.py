# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:26:52 2019

@author: Parikshith.H
"""

a = input("Enter a number:")
b = input("Enter a number:")
c = input("Enter a number:")
if (a>b and a>c):
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")

# =============================================================================
# Output
# Enter a number:2
# 
# Enter a number:3
# 
# Enter a number:1
# b is greatest
# =============================================================================


a = "Python"
b = "Python"
if a == b:
    print("True1")
else:
    print("False")
c = "Hello"
if c == "Hi":
    print("True2")
else:
    print("False2") 

# =============================================================================
# Output:True1
# =============================================================================

a = 10
b = 20
print(id (a))
print(id (b))
# =============================================================================
# Output:
# 140718423076896
# 140718423077216
# =============================================================================

a = 10
b = 20
print(id (a))
print(id (b))
c = 30
d = 30
print(id(c))
print(id(d))
# =============================================================================
# Output:
# 140718423076896
# 140718423077216
# 140718423077536
# 140718423077536
# =============================================================================

a = 10
b = 20
print(id (a))
print(id (b))
c = 30
d = 40
print(id(c))
print(id(d))

# =============================================================================
# Output:
# 140718423076896
# 140718423077216
# 140718423077536
# 140718423077856
# =============================================================================

a = 10
b = 10
if a is b:
    print("Both are same")
else:
    print("Both are different")

# =============================================================================
# Output:
# Both are same
# =============================================================================

 
