from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def save(self, name, amount):
        pass

class Database(DatabaseInterface):
    def save(self, name, amount):
        print(f"Saving {name} - {amount}")

class FeeService:
    def __init__(self, database):
        self.database = database
    
    def pay_fee(self, student_name, amount):
        self.database.save(student_name, amount)

# Usage
db = Database()
fee_service = FeeService(db)
fee_service.pay_fee("Ali", 1500)

# For testing - inject mock database
class MockDatabase(DatabaseInterface):
    def save(self, name, amount):
        print(f"Mock: Saving {name} - {amount}")

mock_db = MockDatabase()
test_service = FeeService(mock_db)
test_service.pay_fee("Test", 100)
