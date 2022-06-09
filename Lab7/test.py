class Student:
    #
    def __init__(self,name,age):
        self.name = name # public member
        self.__age = age # private member age >=18
        self.__major = 'MT' # protected
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
        print(f'Name: {self.name} Age: {self.__age} '
            f'Major: {self.__major}')


# std1 = Student('Jatuphon',21)
# std1.display_info()
#
# print(std1.get_age(),type(std1.get_age()))
#
# # setter
# std1.set_age('18a')
# print(std1.get_age())

# std1.set_age('Hello')
# print(std1.get_age())

print('Enter your student detail')

name = input('Student name: ')
age = int(input('age: '))

std2 = Student(name,age)
std2.display_info()

std2.set_age(10)
# # print(std2.get_age())