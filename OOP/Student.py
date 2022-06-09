class Student:
    #
    def __init__(self,name,age,id,weight,height):
        self.name = name
        self.__age = age
        self.id = id
        self.weight = weight
        self.height = height
    def __int__(self):
        pass

    # getter and setter methods
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        if new_age >= 18:
            self.__age = new_age
        else:
            print('Age should be higher 18.')

    def display_info(self):
        print(f'Name: {self.name} Age: {self.__age} ID: {self.id} Weight: {self.weight}'
            f' Height: {self.height}')

print('Enter your student detail')

name = input('name: ')
age = int(input('age: '))
id = int(input('ID:'))
weight = int(input('Weight: '))
height = int(input('Height: '))


std = Student(name,age,id,weight,height)
std.display_info()
#
# std2.set_age(18)
print(std)