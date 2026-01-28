def process_students():
    students = [
        "Ali,Science,1200",
        "Sara,Commerce,1500",
        "John,Science,1000"
    ]

    for s in students:
        data = s.split(",")
        name = data[0]
        course = data[1]
        fee = int(data[2])

        if course == "Science":
            fee += 500
        elif course == "Commerce":
            fee += 300

        print("Student:", name)
        print("Course:", course)
        print("Total Fee:", fee)
        print("-----")


process_students()
