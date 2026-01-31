class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostrich can't fly")
b=Bird()
b.fly()
o=Ostrich()
o.fly()
