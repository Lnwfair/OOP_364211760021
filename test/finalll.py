"""
Name : Jatuphon Chit
ID: 021
Group: MIT 211
"""

from model import Student,Courses,CoursesR,Employee

def display_courses():
    n = 1
    for x in Courses.all_courses:
        print(f'\t{n}. {x} ')
        n += 1

def validate_c(a):
    if a <= 3:
        return True
    else:
        return False

def input_person():
    name = input('Name: ')

    while True:
        c = int(input('Courses: '))
        if validate_c(c):
            break
        else:
            print('no more than three classes. ')

    email = (input('Email: '))
    tel = (input('Tel: '))

    return name,c,email,tel

def input_student():
    id = input('Student ID: ')
    major = input('Major: ')
    return id,major

def input_employee():
    position = input('Position: ')
    return position

def input_courses():
    num = int(input('How many classes do you need : '))

    coursesate_date = list()

    for x in range(num):
        display_courses()
        n = len(Courses.all_courses)
        while True:
            select = int(input(f'select(1-{n}): '))
            if select >= 1 and select <= n:
                break
            print(f'Please, enter number 1-{n} only.')

        d = input('Date: ')

        coursesate_date.append([Courses(Courses.all_courses[select - 1]), d])

    return coursesate_date


if __name__ == '__main__':
    print('Enter your information: ')
    p = input_person()

    x = input('Are you Student(s) or Employee(e) :: (s/e): ?')
    if x.lower() == 's':
        s = input_student()
        s = Student(p[0], p[1], p[2], p[3], s[0], s[1])
    else:
        position = input_employee()
        s = Employee(p[0], p[1], p[2], p[3],position)

    v_s = CoursesR(s)
    v_s.add_coursesated(input_courses())

    v_s.__str__()
