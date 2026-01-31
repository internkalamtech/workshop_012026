#Good code for birds module.
class bird:
    def fly(self):
        print("Bird is flying")

class ostrich(bird):
    def fly(self):
         raise Exception("ostrich can't fly")
if __name__ == "__main__":
     bird = bird()
     bird.fly()

     ostrich = ostrich()
     try:
         ostrich.fly()
     except Exception as e:
         print(e)