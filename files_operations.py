f = open("lesson2.txt",'x')
print(f.read())
f.close()

with open("lesson2.txt", 'r+w')as f:
    f.write("this is my new file\n")
    f.write("i am happy\n")


#read line by line 

    