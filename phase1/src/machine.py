from abc import ABC, abstractmethod
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass
class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass
class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass

class OldPrinter(Printer):
    def print(self):
        print("Printing")
class ModernPrinter(Printer,Scanner,Fax):
    def print(self):
        print("Modern printing")

    def scan(self):
        print("scanning")

    def fax(self):
        print("faxing")
