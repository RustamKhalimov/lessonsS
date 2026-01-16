grades = {}
while True :
    task = int(input("Enter task number (1-3) or type 4 for exit: "))
    if task == 1:
        def celsius_to_fahrenheit(celsius):
            return (celsius * 9/5) + 32

        def fahrenheit_to_celsius(fahrenheit):
            return (fahrenheit - 32) * 5/9

        temperature = float(input("Enter temperature: "))
        direction = input("Convert to (Celsius/Fahrenheit): ").strip().lower()

        if direction == "celsius":
            result = fahrenheit_to_celsius(temperature)
            print(f"Result: {result:.1f} °C")
        elif direction == "fahrenheit":
            result = celsius_to_fahrenheit(temperature)
            print(f"Result: {result:.1f} °F")
        else:
            print("Invalid conversion direction.")


    elif task == 2:
        def add_grade(grades, student, subject, grade):
            if student not in grades:
                grades[student] = {}
            grades[student][subject] = grade
            print("Grade added.")

        def view_grades(grades):
            if not grades:
                print("No data available.")
                return
            for student, subjects in grades.items():
                print(f"\nStudent: {student}")
                for subject, grade in subjects.items():
                    print(f"  {subject}: {grade}")

        def remove_student(grades, student):
            if student in grades:
                del grades[student]
                print("Student removed.")
            else:
                print("Student not found.")


        while True:
            action = input("\nChoose action: add, view, remove, quit\n> ").strip().lower()

            if action == "add":
                student = input("Enter student name: ")
                subject = input("Enter subject: ")
                grade = input("Enter grade: ")
                add_grade(grades, student, subject, grade)

            elif action == "view":
                view_grades(grades)

            elif action == "remove":
                student = input("Enter student name to remove: ")
                remove_student(grades, student)

            elif action == "quit":
                break

            else:
                print("Invalid action.")

        
    elif task == 3:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        number = int(input("Enter a number: "))

        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

    elif task == 4:
        break
    else:
        print("Invalid task number. Please enter a number between 1 and 3.")
