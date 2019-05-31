#!/usr/bin/python

# The try block lets you test a block of code for errors. The except block lets you handle the error. The finally block lets you execute code, regardless of the result of the try and except blocks.

try:
    print(x)
except:
    print("An exception occurred")  # x is not defined

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")  # if no error occurs

try:
    print(x)
except:
    print("Something went wrong")
finally:  # executes even if error is raises
    print("The 'try except' is finished")
