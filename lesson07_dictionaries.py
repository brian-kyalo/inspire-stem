#!/usr/bin/python

##################
#  dictionaries
#  Name : Brian kyalo
#  Date : 23 / 5 / 20
##################


# Initalizing dictionaries
# dictionaries use calibracates
Student = {"Name": "Brian","Age":19, "Gender": "Male"}
#print(Student["Name"])
#print(Student["Age"])
# How to add a pairs 
Student["ID No"] = 12864973
Student["Hobby"] = "swimming"
Student["Club"] = " Rugby"
#print(Student)

Student['fav.food'] = "Briani"
Student["Home_City"] = "Nairobi"
#print(Student)
# To modify values is to change
Student["Name"] = "Kyalo"
Student["Age"] = "18" 
#print(Student)
Student["ID No"] = "1234567"

#To remove use the key word_ 'DEL'
del Student["Name"]
#print(Student)
del Student["Age"]
print(Student)









