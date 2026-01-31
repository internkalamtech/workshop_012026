class Bird:
    def walk(self):
        print("Walking")

class Ostrich(Bird):
    def walk(self):
        print("Ostrich walking")

bird=Bird()
bird.walk()
ostrich=Ostrich()
ostrich.walk()
