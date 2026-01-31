# Both students do exactly this:
# Create a branch
# Open fee_calculator.py
# Modify the same function 
    # Student 1: update thee function to add 600 for science students
    # Student 2: update the function to add 400 for commerce students
# Commit & push
# Raise PR

def calculate_fee(student_type, base_fee):
    if student_type == "science":
        return base_fee + 600
    elif student_type == "commerce":
        return base_fee + 300
    else:
        return base_fee
