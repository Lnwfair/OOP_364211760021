"""
student Name:jatuphon chit
ID :021
Group :mit211
"""


class Dapartment:
    d_name = ''

class University:
    u_name = ''
    list_fo_dapartment = list()

    def get_department(self):

        d1 = Dapartment()
        d1.d_name = 'MT'
        d2 = Dapartment()
        s2.d_name = 'Sci'

        self.list_fo_dapartment.append(d1)
        self.list_fo_dapartment.append(d2)

    def __str__(self):
        print(f'Dapartment in {self.u_name}: ')
        for x in self.list_fo_dapartment:
            print(x.d_name)