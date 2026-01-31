class Bird:
    def fly(self):
        print("Flying")

class FlyingBird(Bird):
    pass

class NonFlyingBird(Bird):
    def fly(self):
        raise Exception("This bird cannot fly")

class Ostrich(NonFlyingBird):
    pass