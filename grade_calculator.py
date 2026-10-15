
print("================================")
print("    STUDENT GRADE CALCULATOR")
print("================================")

try:
    name = input("Enter student name: ")

    subjects = ["Maths", "Python", "Physics", "English", "Electronics"]
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100!")

            except ValueError:
                print("Please enter a valid number!")

    total = sum(marks)
    percentage = total / len(subjects)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\n================================")
    print("         RESULT REPORT")
    print("================================")
    print(f"Student: {name}")
    print(f"Total Marks: {total:g}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("================================")

except KeyboardInterrupt:
    print("\nCalculation cancelled.")
