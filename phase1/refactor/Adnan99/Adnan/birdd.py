class Bird:
    def walk(self):
        print("walking")

class Ostrich(Bird):
    def walk(self):
        print("Ostrich can't fly")
bird=Bird()
bird.walk()

ostrich=Ostrich()
ostrich.walk()