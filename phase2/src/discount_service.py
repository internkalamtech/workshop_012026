# Both students do exactly this:
# Create a branch
# Open fee_calculator.py
# Modify the same function 
    # Student 1: if amount > 500, reduce by 100
    # Student 2: if amount > 1000, reduce by 200
# Commit & push
    # student 2: commits first and then student 1 commits, leading to a conflict, student 1 has to resolve the conflict

def apply_discount(amount):
    if amount > 1000:
        return amount - 200
    return amount - 100