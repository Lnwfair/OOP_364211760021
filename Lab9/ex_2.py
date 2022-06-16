"""
student Name:jatuphon chit
ID :021
Group :mit211
"""


class Student:
    s_name = ''
    t_list = list()


class Teacher:
    t_name = ''
    s_list = list()

    def __str__(self):
        print(f'')

s1 = Student()
s1.s_name = 'Jatuphon'

s2 = Student()
s2.s_name = 'Pornprasort'


print(s1.s_name)

t1 = Teacher()
t1.t_name = 'Puriwat'

t2 = Teacher()
t2.t_name = 'Phetcharat'

print(t1.t_name,t2.t_name)


s1.t_list = [t1,t2]

print(f'{s1.s_name} มีที่ปรึกษา คือ')
for x in s1.t_list:
    print(f'อาจารย์ {x.t_name}')

t1.s_list = [s1,s2]

print(f'{t1.s_name} เป็นที่ปรึกษาของ')
for x in t1.t_list:
    print(f'นักเรียน {x.s_name}')
