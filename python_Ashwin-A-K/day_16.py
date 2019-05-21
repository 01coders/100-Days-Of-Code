#!/usr/bin/python

d = {
    "Name": "ABC",
    "Roll No.": "XYZ",
    "Class": 11
}
d2 = dict()
print(len(d))  # print no. of items
d["Section"] = "A"
print(d)  # Adding an item to the dict

d2 = d.copy()  # constructor class

d.pop("Section")  # remove items from a dict
d.popitem()  # removes the last inserted item
d.clear()  # empties the dict
del d  # delete dict

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and values
# get()	Returns the value of the specified key
# items()	Returns a list containing the a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
