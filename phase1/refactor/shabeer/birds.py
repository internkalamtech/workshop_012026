class bird:
    def fly(self):
        print("bird is flying")
class Ostrich(bird):
    def fly(self):
        raise Exception("Ostrich can't fly")    
if __name__ == "__main__":
    bird = bird()
    bird.fly()
    ostrich = Ostrich()
    try:
         ostrich.fly()   
    except Exception as e:
            print(e)