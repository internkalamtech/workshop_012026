#Good code for birds module.
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

b = Bird()
b.fly()

o = Ostrich()
o.fly()
