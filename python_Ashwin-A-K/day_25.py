#!/usr/bin/python

import re  # regular expressions

str1 = "Hi there, How are you?"
# findall() function returns a list containing all matches
x1 = re.findall("re", str1)
print(x1)  # prints list of all matches else returns empty list

# search() function searches the string for a match, and returns a Match object if there is a match else return None
x2 = re.search("re", str1)
print(x2)

# split() function returns a list where the string has been split at each match:
x3 = re.split("re", str1)
print(x3)
# we can specify number of occurrences using maxsplit param
x4 = re.split("re", str1, 1)
print(x4)

# sub() function replaces the matches with the text specified
x5 = re.sub("re", "Spec", str1)
print(x5)
# we can specify number of replacements by specifying the count param
x6 = re.sub("re", "Spec", str1, 1)
print(x6)
