print("==============================")
print("       SMART CALCULATOR")
print("==============================")

while True:
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thanks for using Smart Calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        continue

    if choice == "1":
        result = num1 + num2
        print(f"Result: {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"Result: {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"Result: {result}")

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"Result: {result}")
