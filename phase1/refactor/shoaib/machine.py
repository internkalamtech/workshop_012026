# Base capability classes

class Printer:
    def print(self):
        pass


class Scanner:
    def scan(self):
        pass


class Fax:
    def fax(self):
        pass


# Machines

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


# Usage

def use_printer(printer: Printer):
    printer.print()


old_printer = OldPrinter()
modern_printer = ModernPrinter()

use_printer(old_printer)
use_printer(modern_printer)

modern_printer.scan()
modern_printer.fax()
