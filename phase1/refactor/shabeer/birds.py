class Bird:
    def eat(self):
        print("Eating")

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Sparrow(FlyingBird):
    pass

class Ostrich(Bird):
    def run(self):
        print("Running fast!")
