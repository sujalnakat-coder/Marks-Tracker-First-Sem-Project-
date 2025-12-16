students = {}

print("===== Student Marks Management System =====")

while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        marks1 = int(input("Enter marks of Subject 1 maths : "))
        marks2 = int(input("Enter marks of Subject 2 english: "))
        marks3 = int(input("Enter marks of Subject 3 hindi : "))

        total = marks1 + marks2 + marks3
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"

        students[roll] = {
            "Name": name,
            "Marks": [marks1, marks2, marks3],
            "Total": total,
            "Percentage": percentage,
            "Grade": grade
        }

        print("Student record added successfully!")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")

        if roll in students:
            s = students[roll]
            print("\nStudent Details")
            print("Name:", s["Name"])
            print("Marks:", s["Marks"])
            print("Total:", s["Total"])
            print("Percentage:", s["Percentage"])
            print("Grade:", s["Grade"])
        else:
            print("Student not found!")

    elif choice == "3":
        if not students:
            print("No student records available.")
        else:
            for roll, s in students.items():
                print("\nRoll No:", roll)
                print("Name:", s["Name"])
                print("Percentage:", s["Percentage"])
                print("Grade:", s["Grade"])

    elif choice == "4":
        print("Thank you! Program exited.")
        break

    else:
        print("Invalid choice! Try again.")
        
