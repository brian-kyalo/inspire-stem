import random
print("welcome to our password generation ")

char = 'Brian@123'
num_password = int(input("how many numbers do you want"))
len_password = int(input("ask user for password length"))
#print(num_password)
#print(len_password)


for password in range (num_password):
    password="    "
for c in range (len_password):
    password += random.choice(char)
print(password)

