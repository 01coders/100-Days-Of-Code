#!/usr/bin/python

# An iterator is an object that can be iterated upon which can traverse through all the values. It consist of the methods __iter__() and __next__().
# Lists, tuples, dictionaries, and sets are all iterable objects. All these objects have a iter() method which is used to get an iterator

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = Numbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
