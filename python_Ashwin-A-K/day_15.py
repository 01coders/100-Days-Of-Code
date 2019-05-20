#!/usr/bin/python

# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

d = {
    "Name": "ABC",
    "Roll No.": "XYZ",
    "Class": 11
}
print(d)

x = d["Name"]  # Acessing the items
y = d.get("Name")  # Acessing the items
print(x, y)

d["Class"] = 10
print(d)  # editing the values of key

for x in d:
    print(x)  # looping dict and print keys
for x in d:
    print(d[x])  # looping dict and print values
for x in d.values():
    print(x)  # looping dict and print values
for x, y in d.items():
    print(x, y)  # looping dict and print items

if "Roll No." in d:
    print("Present")
