
import student

students = []

print("\n------Student Record Marksheet------")
print("You can do the following")
while True:
    print("\n1. Add a student")
    print("2. View all students")
    print("3. Search by roll number")
    print("4. Save the student data file from a File")
    print("5. Load the student data file from a File")
    print("6. Exit")

    opt = input("\nWhat do you want to do: ")

    if opt == "1":
        student.add(students)
    elif opt == "2":
        student.view(students)
    elif opt == "3":
        student.search(students)
    elif opt == "4":
        student.save(students)
    elif opt == "5":
        student.load(students)
    elif opt == "6":
        print("\nGoodbye\n")
        break
    else:
        print("Invalid option, enter one of the given options")


    