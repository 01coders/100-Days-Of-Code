#!/usr/bin/python

# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets

s = {"a", "b", "c"}
print(s)

for x in s:
    print(x)  # iterating the set

print("banana" in s)  # check for presence of item

s.add("d")  # add item to set
s.update(["e", "f", "g"])  # adding multiple items

s.remove("c")  # remove item ... if not present, error
s.discard("d")  # remove item ... if not present, no error
x = s.pop()  # to remove item but doesn't know which item has been removed
print(x)  # so it is stored as a var

s.clear()  # to empty the set
del s  # to delete the set

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others
