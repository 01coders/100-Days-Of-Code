#!/usr/bin/python

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

t = ("a", "b", "c")
print(t)
print(t[1])  # accessing tuple

for x in t:  # iterating tuple
    print(x)

if "a" in t:  # check presence of ele in tuple
    print("A is Present")

# t[3] = "d" This will raise an error
del t  # we can delete the tuple

t1 = tuple(("1", "2", "3"))  # note the double round-brackets
print(t1)

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
