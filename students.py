#!/usr/bin/python

##################
#  operations(students.py)
#  Name : Brian kyalo
#  Date : 6 / 6 / 22
##################


import operations


from teachers import Teachers 
class Student:
     


    def __init__(self,name,hobby,year_of_birth):
         self.name = name 
         self.hobby = hobby
         self.year_of_birth = year_of_birth

    def greet_student():
       print("hello from student ")  


new_student = student("brian kyalo")
student.greet_student()

new_teacher = Teachers("Brian",128649,"chemistry")
print(new_teacher.get_tsc_number())




