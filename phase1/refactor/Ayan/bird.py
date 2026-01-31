class Bird:
    def walk(self):
        print("walking")

class Ostrich(Bird):
    def walk(self):
        raise Exception("Ostrich can't fly")
bird = Bird()
bird.walk()  # Output: walking

ostrich = Ostrich()
ostrich.walk()  # Output: Exception - Ostrich can't fly    