students = []

print("Welcome to student register!")
while True:
    print("--MENU--")
    print("1. Add student")
    print("2. List students")
    print("3. Quit program")
    print("4. Search name")
    print("5. Total age")
    print("6. Remove student")
    choice = int(input("Pick a number 1-5: "))

    if choice == 1:
        student_name = input("Enter student's name: ")
        student_age = int(input("Enter student's age: "))
        student = {"name": student_name, "age": student_age}
        students.append(student)
        print(f"Student added: {student}")

    elif choice == 2:
        for student in students:
            print(student['name'], student['age'])

    elif choice == 4:
        find_student = input("Search user by name: ")
        found = False
        for student in students:
            if find_student == student['name']:
                print(student)
                found = True
        if not found:
            print("No student found with that name.")

    elif choice == 5:
      if students:
          total_age = sum(student['age'] for student in students)
          print(f"Total age is: {total_age}")
      else:
          print("No students added yet.")

    elif choice == 6:
      delete_user = input("Enter student name that you want to remove: ")
      found = False
      for student in students:
          if delete_user == student['name']:
              students.remove(student)
              print(f"Removed {delete_user}")
              found = True
              break   
      if not found:
          print("No student found with that name.")

    elif choice == 3:
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
