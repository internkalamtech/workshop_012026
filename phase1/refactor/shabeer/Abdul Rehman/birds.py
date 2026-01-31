#To fix the Liskov Substitution Principle (LSP), we simply move fly() to a specific class that only flying birds use.
class Bird:
    def eat(self):
        print("Eating")

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def run(self):
        print("Ostrich running")

