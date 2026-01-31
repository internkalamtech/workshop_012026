
class Machine:
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass

class OldPrinter(Machine):
    def print(self):
        print("Printing")

    def scan(self):
        raise Exception("Scan not supported")

    def fax(self):
        raise Exception("Fax not supported")