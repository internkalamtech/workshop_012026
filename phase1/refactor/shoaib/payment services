# Storage rule (what to do, not how to do)

class FeeRepository:
    def save(self, name, amount):
        pass


# Actual database implementation

class Database(FeeRepository):
    def save(self, name, amount):
        print(f"Saving {name} - {amount}")


# Fee service (business logic only)

class FeeService:
    def __init__(self, repository):
        self.repository = repository

    def pay_fee(self, student_name, amount):
        self.repository.save(student_name, amount)


# Usage

db = Database()
fee_service = FeeService(db)

fee_service.pay_fee("Shoaib", 5000)
