"""
student Name:jatuphon chit
ID :021
Group :mit211
"""

class Teacher:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f'My name is {self.name}, I am Teacher.')

class Student:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f'My name is {self.name}, I am Student.')

myList = []
t = Teacher('Purwat')
s = Student('Jatuphon')

myList.append(t)
myList.append(s)

#print(myList, len(myList))

for x in myList:
    print(x.introduce())