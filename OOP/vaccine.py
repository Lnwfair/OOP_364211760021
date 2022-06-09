class vaccine:
    def __init__(self,name):
        # object attributes
        self.name = name

    def vaccine_detail(self):
        print(f'name:{self.name} ')



c1 = vaccine("sinovac")
c2 = vaccine("astrazeneca")
c3 = vaccine("johnson")
c4 = vaccine("moderna")
c5 = vaccine("sinopharm")
c6 = vaccine("pfizer")


c1.vaccine_detail()
c2.vaccine_detail()
c3.vaccine_detail()
c4.vaccine_detail()
c5.vaccine_detail()
c6.vaccine_detail()

myvaccine = []

for x in myvaccine:
    print(x.vaccine_detail())