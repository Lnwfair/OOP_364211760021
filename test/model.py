"""
Name : Jatuphon Chit
ID: 021
Group: MIT 211
"""
class Person:
    def __init__(self,name,c,email,tel):
        # object attributes
        self.__name = name # private member
        self.__c = c
        self.__email = email
        self.__tel = tel

    # getter and setter method
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_class(self):
        return self.__c
    def set_class(self, c):
        self.__c = c
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email
    def get_tel(self):
        return self.__tel
    def set_tel(self, tel):
        self.__tel = tel

    # display Person object
    def __str__(self):
        print(f'\tName: {self.__name}\n'
                  f'\tCourses: {self.__c}\n'
                  f'\tEmail: {self.__email}\n'
                  f'\tTel: {self.__tel}\n')

class Student(Person):
    def __init__(self,name,c,email,tel,id,major):
        super().__init__(name,c,email,tel)
        #Person.__init__(self,name,age,weight,height)
        self.__id = id
        self.__major = major

    # getter and setter
    def get_id(self):
        return  self.__id
    def set_id(self,id):
        self.__id = id
    def get_major(self):
        return  self.__major
    def set_major(self,major):
        self.__major = major

    def __str__(self):
        print('MT  Passport (Student):')
        super().__str__()
        print(f'\tSID: {self.__id}\n'
              f'\tMajor: {self.__major}\n')

class Courses():

    all_courses = ['Digital Marketing for Small Business','Accounting for SME','Chatbot for E-Commerce','Data Analytics for Small Business']

    def __init__(self,courses_name):
        self.__courses_name = courses_name

    #getter and setter method
    def get_courses(self):
        return self.__courses_name
    def set_courses(self,new_name):
        self.__courses_name = new_name

    def __str__(self):
        print(f'Courses name: {self.__courses_name}')

class CoursesR():
    def __init__(self, owner):
        self.owner = owner
        self.coursesated = list() # [] ==> [[v1,'11/7/2564'],[v2,10/10/2564]]

    def add_coursesated(self,courses):
        self.coursesated = courses

    def __str__(self):

        self.owner.__str__()
        for x in self.coursesated:
            print(f'\tcourses {self.coursesated.index(x)+1}: {x[0].get_courses()}  \t\tdate: {x[1]}')

class Employee(Person):
    def __init__(self,name,c,email,tel,position):
        super().__init__(name,c,email,tel)
        self.__position = position

    def get_position(self):
        return self.__position
    def set_position(self,position):
        self.__position = position

    def __str__(self):
        print('MT  Passport (Employee):')
        super().__str__()
        print(f'\tPosition: {self.__position}\n')


print('Hello, from model.')