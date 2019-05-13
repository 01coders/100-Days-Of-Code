"""
Created on Mon May 13  20:01:23 2019

@author: Manoj Athreya
"""
#Given below is a Dictionary customer_details representing customer Details from Retail Application - Customer Id is key and Customer Name is value.  
#customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" } Write Python code to perform below mentioned operations: 
#Print details of Customers 
#Print number of Customers 
#Print Customer names in ascending order 
#Delete the details of customer with customer id = 1005 and print updated dictionary 
#Update the name of customer with customer id = 1003 to “Mary” and print updated dictionary 
#Check whether details of customer with customer id 1002 exists in the dictionary


customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }

print("1]",customer_details)
print("2]",len(customer_details))
print("3]",sorted(customer_details.values()))
del(customer_details[1005])
print("4]",customer_details)
customer_details[1003] = "Mary"
print("5]",customer_details)
print("6]",1002 in customer_details)
==============================================
# OUTPUT:
# 1] {1001: 'John', 1004: 'Jill', 1005: 'Joe', 1003: 'Jack'}
# 2] 4
# 3] ['Jack', 'Jill', 'Joe', 'John']
# 4] {1001: 'John', 1004: 'Jill', 1003: 'Jack'}
# 5] {1001: 'John', 1004: 'Jill', 1003: 'Mary'}
# 6] False
# ==============================================


#To find top three scorers for the course and also display average marks. 

marks = {"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1}
sort_marks = sorted(marks.values())
sort_marks.reverse()
print(sort_marks)
top_three=[]
for i in range(0,3):
    top_three.append(sort_marks[i])
print("Top 3 Courses are :",top_three)
print("Average marks is:",sum(top_three)/3)

===========================================
# OUTPUT:
# [91.2, 86.5, 84.5, 72.1]
# Top 3 Courses are > [91.2, 86.5, 84.5]
# Average marks > 87.39999999999999
============================================

