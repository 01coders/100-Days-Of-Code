#!/usr/bin/python

# # "a" will append to the end of the file
# f1 = open("day26.txt", "a")
# f1.write("New Line.....!")  # write function will add the string to the file
# f1.close()

# # open and read the file after the appending:
# f2 = open("day26.txt", "r")
# print(f2.read())

import os
# f3 = open("day26.txt", "w")
# f3.write("File overwritten")
# f3.close()

# f4 = open("day26.txt", "r")
# print(f4.read())

# # "x" will create a file, returns an error if the file exist
# f = open("day27.txt", "x")

# os.remove("day26.txt")  # Remove the file

print(os.path.exists("day26.txt"))  # Check if file exists
os.rmdir("foldername")  # To delete an entire folder
