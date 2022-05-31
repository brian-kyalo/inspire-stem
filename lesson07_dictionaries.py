#!/usr/bin/python

##################
#  dictionaries
#  Name : Brian kyalo
#  Date : 23 / 5 / 20
##################


# Initalizing dictionaries
# dictionaries use calibracaes
from turtle import color


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
#print(Student)

#printing stars in pymarid shape
#print("        ***** ")
##print(" ***** ")
#print(" ***** ")
#print(" ***** ")
#print("        ***** ")
#print("        ***** ")
#print("        ***** ")
#print("        ***** ")


# how to create an empty List
#a dictionary is a collection of key value pairs
#syntax: dictionary = {'key':'value'}

list_names ='Brian Kyalo'
colors= {'color':'red'}
vehicle= {'type':'toyota','plate number':'KBD2343'}
#print(type(colors)) ##we use the type method to read the
# how to access values inside a dictionary
#print(vehicle['type']) # you can access the value of an element inside a dictionary using the key 
#print(vehicle['type'] , vehicle['plate number'])
#print vehicle type and plate number 


#dictionary person
person= {'name':'Brian kyalo'}
person['age']= '18'
person={'name':'Brian kyalo', 'gender':'male','address':'1234-675','ID':'123546','age':'18','fav color':'red'}
ID_NO= {'ID':'123546'}
Address= {'address':'1234-675'}
gender= {'gender':'Male'}
#print(person)


#print(ID_NO['ID'] , Address['address'] ,gender['gender'] , phone_number['NO'])
#print(Name ,ID_NO['ID'] , Address['address'] ,gender['gender'] , phone_number['NO'])

#looping over dictionaries 

    #print(f"{key}:{value}")

      #print(colors[1].upper())
  
#dictionary person
person= {'name':'Brian kyalo'}
person['age']= '18'
person={'name':'Brian kyalo', 'gender':'male','address':'1234-675','ID':'123546','age':'18','fav color':'red'}
ID_NO= {'ID':'123546'}
Address= {'address':'1234-675'}
gender= {'gender':'Male'}
#print(person)

#print(person.get['password','the location key is non existent'])
#using get to acess the value in a dic


#self analisation 
vehicle=  {'brand':'BMW','model':'E30'}

#print(vehicle['model'])

mary_fav_food =['ugali','nyama','machungwa']
jane_fav_food =['rice','supergetti','ice-cream']

fav_food ={
  'mary':['ugali','nyama','machungwa'],
  'jane':['rice','supergetti','ice-cream']
}
#print(fav_food)

for mary_fav_food in fav_food:
   for jane_fav_food in fav_food:
    # print(fav_food)

#print the keys and the value
    for key,value in fav_food.items():
      print(key,value)













