
class Student:
    class Vehicle:
        def __init__(self, name, id, age, weight, height):
            # object Student
            self.name = name
            self.id = id
            self.age = age
            self.weight = weight
            self.height = height
            pass

        def get_age(self):
            return self.age
        def set_age(self, n_age):
            if n_age >= 18:
                self.age = n_age
            else:
                print('Age should be higher 18.')



        def displayDetail(self):
            print(f'f{self.name} {self.id} {self.age} {self.weight} {self.height }')

S = input('Name: ')
I = int(input('ID:'))
A = int(input('Age: '))
W = float(input('Weight: '))
H = int(input('Height: '))

vac = input('How many are you vaccianted: ')
print('1.sinovac')
print('2.astrazeneca')
print('3.johnson&johnson')
print('4.moderna')
print('5.sinopharm')
print('6.pfizer')
s1 = int(input('select: '))
d1 = input('Date(dd/mm/yyyy): ')
print('1.sinovac')
print('2.astrazeneca')
print('3.johnson&johnson')
print('4.moderna')
print('5.sinopharm')
print('6.pfizer')
s2 = int(input('select: '))
d2 = input('Date(dd/mm/yyyy): ')

print('Student Infomation: ')
print('Student Name: ',S)
print('Age: ',A)
print('Weight: ',W)
print('vaccine 1: ',s1,'date: ',d1)
print('vaccine 2: ',s2,'date: ',d2)