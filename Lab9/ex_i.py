"""
student Name:jatuphon chit
ID :021
Group :mit211
"""



class Person:
    def __init__(self,name,pid,email):
        self.name = name
        self.pid = pid
        self.email = email

    def __str__(self):
        print(f'Name: {self.name} PID: {self.pid} Email: {self.email}')

    def introduce(self):
        print(f'My name is {self.name} i Person ')

class Student(Person):
    def __init__(self,name,pid,email,sid,major):
        # method 1
        Person.__init__(self,name,pid,email)

        self.sid = sid
        self.major = major

    def __str__(self):
        print(f'Name: {self.name} PID: {self.pid} Email: {self.email} SID: {self.sid} Major: {self.major}')

    def introduce(self):
        print(f'My name is {self.name} i Student ')




p1 = Person('SAM','001','sam@gmail.com')
p1.__str__()

s1 = Student('Fair','021','fair@gmail.com','s211','MIT')
s1.__str__()

p1.introduce()
s1.introduce()

