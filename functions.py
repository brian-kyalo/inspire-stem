#!/usr/bin/python

##################
#  functions
#  Name : Brian kyalo
#  Date : 23 / 5 / 20
##################


#defining a function
from cmath import sqrt


def say_hello():
    #print("hello!")
    x=4
    y=7
    z=x+y
    #print(z)
say_hello()    


def bark():
    #print("dogs bark woof! woof!")
    x=4
    y=7
    z=x+y
   # print(z)
bark()    

def cars():
    #print("cars go vroom! vroom!")
    cars()

#adding numbers using def 
def add_numbers(x,y):
    sum_nums = x + y
   # print("the sum of numbers:",sum_nums)
    add_numbers(40,50) 
    add_numbers(60,50)  
    add_numbers(70,80)    
        

def product(x,y):
    sum_nums = x * y
   # print("the product of numbers:",sum_nums)
product(40,50) 
product(60,50)  
product(70,80)   


import math
a =int(input("Enter the coefficient of first term (a) "))
b =int(input("Enter the coefficient of second term (b) "))
c =int(input("Enter the coefficient of the costant (c) "))
w = math.sqrt((b**2)-4*a*c)

y_1 =(-b + w)/(2*a)
y_2 =(-b - w)/(2*a)
    
   
print("the answer is :",y_1, y_2)


    


