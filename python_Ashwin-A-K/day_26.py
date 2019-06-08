#!/usr/bin/python

# File Handling function for working with files in Python is the open() function which takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

f = open("day26.txt")
# f = open("demofile.txt", "rt") #r for and t for text

# print(f.read())  # read() method for reading the content of the file
# print(f.read(5))  # Return the 5 first characters of the file
# print(f.readline()) # Read one line of the file

# By calling readline() two times, you can read the two first lines
# print(f.readline())
# print(f.readline())

for x in f:  # Loop through the file line by line
    print(x)

f.close()  # Close the file when you are finish
