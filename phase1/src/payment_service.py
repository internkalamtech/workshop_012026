class Database:
    def save(self, name, amount):
        print(f"Saving {name} - {amount}")

class FeeService:
    def pay_fee(self, student_name, amount):
        db = Database()
        db.save(student_name, amount)
