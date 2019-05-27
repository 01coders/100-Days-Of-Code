#!/usr/bin/python

# Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.


class Person:  # parent class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("XYZ", "ABC")
x.printname()


class Student(Person):  # inherit the properties and methods from the Person class
    pass  # pass keyword when you do not want to add any other properties or methods to the class


class CSstudent(Person):
    def __init__(self, fname, lname, domain):
        Person.__init__(self, fname, lname)
        self.subject = domain

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.subject)


y = CSstudent("ASD", "QWE", "ML")
y.printname()
y.welcome()
