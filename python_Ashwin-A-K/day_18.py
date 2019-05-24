#!/usr/bin/python

# A lambda function is a small anonymous function which can take any number of arguments, but can only have one expression.
# Use lambda functions when an anonymous function is required for a short period of time.
# x = lambda a : a + 1
# # print(x(1)) #This syntax is not supported by my linter


def x(a): return 1 + a


print(x(2))


def y(a, b, c): return a + b + c


print(y(1, 2, 3))  # Lambda functions can take any number of arguments:

# power of lambda is better shown when you use them as an anonymous function inside another function.


def double(n):
    return lambda a: a * n


doubler = double(2)
print(doubler(10))


def triple(n):
    return lambda a: a * n


mytripler = triple(3)
print(mytripler(10))
