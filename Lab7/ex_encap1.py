"""
student Name:jatuphon chit
ID :021
Group :mit211
"""


# Encapsulation

class Student:
    def __init__(self,name,age):
        self.name = name # public member
        self.__age = age # private member
        self.__major = 'MT' # protected

    def display_info(self):
        print(f'Name: {self.name}\nAge: {self.__age}')

# create object of student
std = Student('Jatuphon','21')
print(std.name)  # direct access
#print(std.__age) # 21
# 1. use public methdo to access private member
std.display_info()
# 2. name mangling -->_className__attributeName
print(std._Student__age)


std._Student__age = 40
print(std._Student__age)
std.display_info()

# std.age = 22
# print(std.age)  # 22
# std.age = -100
# print(std.age)
# std.display_info()
