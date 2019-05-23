#!/usr/bin/python

# A function is a block of code which only runs when it is called. It can pass parameters and can return data as a result.


def func():
    print("Hello function")  # function is defined using the def keyword


func()  # calling a func

# Information can be passed to functions as parameter.You can add as many parameters as you want, just separate them with a comma.
# This function has one parameter fname. When the function is called, we pass along a first name, which is used inside the function to print the full name


def func2(fname):
    print("HI " + fname)


func2("X")
func2("Y")
func2("Z")


def func3(game="Football"):  # default parameter
    print("I play " + game)


func3("Cricket")
func3()  # it takes football as default parameter


def func4(y=1):
    return y + 1  # function return a value


print(func4(3))

# We can send any data as parameter to a function like string, number, list, dictionary etc. and it will be treated as the same data type inside the function.


def func5(grocery):
    for x in grocery:
        print(x)


grocery_list = ["Sugar", "Banana", "Dal"]

func5(grocery_list)
