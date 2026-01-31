# Both students do exactly this:
# Create a branch
# Open fee_calculator.py
# Modify the same function 
    # Student 1: update the function to add 600 for science students
    # Student 2: update the function to add 400 for commerce students
# Commit & push
    # student 1: commits first and then student 2 commits, leading to a conflict, student 2 has to resolve the conflict

def calculate_fee(student_type, base_fee):
    if student_type == "science":
        return base_fee + 500
    elif student_type == "commerce":
        return base_fee + 300
    else:
        return base_fee
