

class Ractangle:
    def cal_area(self,x,y):
        print('Area of rectangle is: ',(x*y))
class Triangle:
    def cal_area(self,d,h):
        print('Area of triangle is:',(0.5*d*h))

def calArea(obj,a,b):
    obj.cal_area(a,b)

r  = Ractangle()
t = Triangle()
# Solution 1
# r.cal_area(5,10)
# t.cal_area(10,20)

# Solution 2
calArea(r,5,10)
calArea(t,10,20)

# Solution 3
# for obj in (r,t):
#     obj.cal_area()