
from teachers import Teachers 
class Teachers():
    def __init__(self,name,tsc_number,subject,salary):
        self.name = name
        self.tsc_number = tsc_number
        self.subject = subject 
        self.salary = salary

    def get_tsc_number(tsc_number):
        return tsc_number

new_teacher = Teachers("Brian",128649,"chemistry")
print(new_teacher.get_tsc_number())        
