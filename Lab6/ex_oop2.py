"""
student Name:jatuphon chit
ID :021
Group :mit211
"""

#Class attributes

class Student:
    major = 'MT'

    def __init__(self,name,group):
        self.name = name
        self.group = group

        def introduce(self):
            print(f'My name is {self.name}, I\'m in {self.group} and'
                  f'studying in {self.major} major.')


std1 = Student('Puriwat Lartkrai','MIT211')
std1.introduce()

Student.major = 'LM'

std1.introduce()