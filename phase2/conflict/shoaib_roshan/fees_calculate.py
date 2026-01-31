def calculate_fee(student_type, base_fee):
    if student_type == "science":
        return base_fee + 600
    elif student_type == "commerce":
        return base_fee + 300
    else:
        return base_fee
