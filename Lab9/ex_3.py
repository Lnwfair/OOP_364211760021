"""
student Name:jatuphon chit
ID :021
Group :mit211
"""

class Department:
    d_name = ''
    list_of_teacher = list()

class Teacher:
    t_name = ''

t1 = Teacher()
t1.t_name = 'sam'
t2 = Teacher()
t2.t_name = 'fair'

d1 = Department()
d1.d_name = 'Jatuphon Chit'

d1.list_of_teacher = [t1,t2]

print(d1.d_name,'and here is list of teacher: ')
for x in d1.list_of_teacher:
    print(x.t_name)


