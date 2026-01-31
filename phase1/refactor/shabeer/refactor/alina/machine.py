class Machine:
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass

class MultifuncPrinter(Machine):
    def print(self):
        print("Printing")

    def scan(self):
        print("Scanning")

    def fax(self):
        print("Faxing")
class OldPrinter(Machine):
    def print(self):
        print("Printing")

    def scan(self):
        raise Exception("Scan not supported")

    def fax(self):
        raise Exception("Fax not supported")
if __name__ == "__main__":
    mfp = MultifuncPrinter()
    mfp.print()  # Output: Printing
    mfp.scan()   # Output: Scanning
    mfp.fax()    # Output: Faxing

    old_printer = OldPrinter()
    old_printer.print()  # Output: Printing
    try:
        old_printer.scan()
    except Exception as e:
        print(e)  # Output: Scan not supported
    try:
        old_printer.fax()
    except Exception as e:
        print(e)  # Output: Fax not supported