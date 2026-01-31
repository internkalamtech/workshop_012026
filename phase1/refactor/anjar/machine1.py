class Printer:
    def print(self):
        pass


class Scanner:
    def scan(self):
        pass


class Fax:
    def fax(self):
        pass


class OldPrinter(Printer):
    def print(self):
        print("Printing")


class ModernPrinter(Printer, Scanner, Fax):
    def print(self):
        print("Printing")

    def scan(self):
        print("Scanning")

    def fax(self):
        print("Faxing")
