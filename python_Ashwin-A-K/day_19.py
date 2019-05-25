#!/usr/bin/python

# Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.
# A Class is like blueprint for creating objects and objects are instances of those classes


class Myclass:
    x = 1


obj1 = Myclass()
print(obj1.x)

# the __init__() function is used to do operations that are necessary when the object is being created which is always executed when the class is being initiated.
# Objects can also contain methods. Methods in objects are functions that belongs to the object.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It does not have to be named self but it has to be the first parameter of any function in the class


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)


s1 = Student("ABC", 16)

print(s1.name)
print(s1.age)
s1.myfunc()

s1.age = 20  # modify property of an object

del s1.age  # delete property of an object
del s1  # delete object
