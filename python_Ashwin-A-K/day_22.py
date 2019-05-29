#!/usr/bin/python

import datetime

x = datetime.datetime.now()
print(x)  # current date and time
print(x.year)  # current year
print(x.strftime("%A"))  # current day

y = datetime.datetime(2020, 5, 17)  # set date
print(y)
print(y.strftime("%B"))  # Month name, full version
