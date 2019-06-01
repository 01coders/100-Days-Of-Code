#!/usr/bin/python

import re  # regular expressions

txt = "Hi there, How are you"
x = re.search("^Hi.*you$", txt)
print(x)  # output : <re.Match object; span=(0, 21), match='Hi there, How are you'>

# Functions :
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# Metacharacters :
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"world$"
# *	Zero or more occurrences	"aix*"
# +	One or more occurrences	"aix+"
# {}	Exactly the specified number of occurrences	"al{2}"
# |	Either or	"falls|stays"
# ()	Capture and group

# Sets :
# [arn]	Returns a match where one of the specified characters (a, r, or n) are present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
