class Printer:
    def print(self):
        print("Printing")
class Scanner:
    def scan(self):
        print("Scanning")
class Fax:
    def fax(self):
        print("Faxing")
class OldPrinter(Printer):
    def print(self):
        print("Printing")   
class modernMachine(Printer, Scanner, Fax):
    def print(self):
        print("Printing")
    def scan(self):
        print("Scanning")
    def fax(self):
        print("Faxing")