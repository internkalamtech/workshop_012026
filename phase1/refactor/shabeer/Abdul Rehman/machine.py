#Break the big Machine class into smaller, specific interfaces. This way, a class only implements what it actually supports.
class Printer:
    def print_doc(self):
        pass

class Scanner:
    def scan_doc(self):
        pass

class OldPrinter(Printer):
    def print_doc(self):
        print("Printing...")

class SmartMachine(Printer, Scanner):
    def print_doc(self):
        print("Smart Printing...")

    def scan_doc(self):
        print("Smart Scanning...")

