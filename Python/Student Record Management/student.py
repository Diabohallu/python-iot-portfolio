students = []


def add(students):
    print("\nAdd a student:")
    name = input("Enter student's name: ").title().strip()
    roll = input(f"Enter the roll no for {name}: ").strip()

    for stu in students:
        if stu["roll"] == roll:
            print("This roll number is already taken")
            return

    subject = input(f"What subjects did {name} score in: ")
    subjects = subject.split(",")
    marks = {}

    print("Enter marks for each subject")
    for sub in subjects:
        subject = sub.strip().title()
        mark = int(input(f"Marks for {subject}: "))
        marks[subject] = mark

    student_record = {
        "name": name,
        "roll": roll,
        "subjects": subjects,
        "marks": marks
    }

    students.append(student_record)
    print(f"{name} added successfully to the record")


def view(students):
    print("\nList of students:")
    if len(students) == 0:
        print("No students recorded")
        return

    count = 1
    for stu in students:
        print("\nStudent", str(count), ":")
        print("Name    :", stu["name"])
        print("Roll No :", stu["roll"])
        print("Marks   :")
        total = 0

        for subject in stu["marks"]:
            mark = stu["marks"][subject]
            print(" ", subject, ":", str(mark))
            total = total + mark

        print("Total Marks:", str(total))
        count = count + 1


def search(students):
    print("\nSearch for Student:")
    roll = input("Enter roll number to search: ").strip()

    for stu in students:
        if stu["roll"] == roll:
            print("\nStudent Found:")
            print("Name    :", stu["name"])
            print("Roll No :", stu["roll"])
            print("Marks   :")
            total = 0

            for subject in stu["marks"]:
                mark = stu["marks"][subject]
                print(" ", subject, ":", str(mark))
                total = total + mark

            print("Total Marks:", str(total))
            return

    print("Student not found")


def save(students):

    with open("student_record.txt", "a") as file:
        for stu in students:
            file.write(f"{stu["name"]}\nRoll.no:{stu["roll"]}\nMarks:{stu["marks"]}\n")
    print(f"\nStudent Record saved to \"student_record.txt\"")


def load():
    with open("student_record.txt", "r") as file:
        print(file.read())
        print(f"\nLoad Student Record from \"student_record.txt\"")