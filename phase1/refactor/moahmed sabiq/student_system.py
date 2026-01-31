class Student:
    def __init__(self, name, course, base_fee):
        self.name = name
        self.course = course
        self.base_fee = base_fee

class FeeCalculator:
    def __init__(self, surcharge_map):
        self.surcharge_map = surcharge_map
    
    def calculate_total_fee(self, student):
        surcharge = self.surcharge_map.get(student.course, 0)
        return student.base_fee + surcharge

class StudentParser:
    def parse(self, data):
        parts = data.split(",")
        return Student(parts[0], parts[1], int(parts[2]))

class StudentDisplay:
    def display(self, student, total_fee):
        print("Student:", student.name)
        print("Course:", student.course)
        print("Total Fee:", total_fee)
        print("-----")

class StudentService:
    def __init__(self, parser, calculator, display):
        self.parser = parser
        self.calculator = calculator
        self.display = display
    
    def process_students(self, students_data):
        for data in students_data:
            student = self.parser.parse(data)
            total_fee = self.calculator.calculate_total_fee(student)
            self.display.display(student, total_fee)

# Usage
students = [
    "Ali,Science,1200",
    "Sara,Commerce,1500",
    "John,Science,1000"
]

surcharge_map = {
    "Science": 500,
    "Commerce": 300
}

parser = StudentParser()
calculator = FeeCalculator(surcharge_map)
display = StudentDisplay()
service = StudentService(parser, calculator, display)

service.process_students(students)