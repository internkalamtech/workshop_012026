#Good code for birds module.
class Bird:
    def fly(self):
        print("Flying")
class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostrich can't fly")        
if __name__ == "__main__":
    bird = Bird()
    bird.fly()  # Output: Flying

    ostrich = Ostrich()
    try:
        ostrich.fly()
    except Exception as e:
        print(e)  # Output: Ostrich can't fly