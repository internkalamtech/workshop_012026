# Student data is now structured and clear
students = [
    {"name": "Ali", "course": "Science", "base_fee": 1200},
    {"name": "Sara", "course": "Commerce", "base_fee": 1500},
    {"name": "John", "course": "Science", "base_fee": 1000},
]

# Fee rules are separated
def calculate_fee(course, base_fee):
    if course == "Science":
        return base_fee + 500
    elif course == "Commerce":
        return base_fee + 300
    return base_fee


# Printing is separated
def print_student(student, total_fee):
    print("Student:", student["name"])
    print("Course:", student["course"])
    print("Total Fee:", total_fee)
    print("-----")


# Main process function
def process_students():
    for student in students:
        total_fee = calculate_fee(student["course"], student["base_fee"])
        print_student(student, total_fee)


process_students()
