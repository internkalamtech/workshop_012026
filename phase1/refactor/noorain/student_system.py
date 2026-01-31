def process_students():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details for student {i + 1}")
        name = input("Name: ")
        course = input("Course (Science/Commerce): ")
        fee = input("Base Fee: ")

        

        students.append(f"{name},{course},{fee}")

    for s in students:
        data = s.split(",")
        name = data[0]
        course = data[1]
        fee = int(data[2])

        if course == "Science":
            fee += 500
        elif course == "Commerce":
            fee += 300

        print("\nStudent:", name)
        print("Course:", course)
        print("Total Fee:", fee)
        print("-----")


process_students()

