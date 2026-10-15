
print("Welcome to my Python Mini Toolkit!")

while True:
    print("\n--- MENU ---")
    print("1. Check even or odd")
    print("2. Check prime number")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print("Even number!")
        else:
            print("Odd number!")

    elif choice == "2":
        number = int(input("Enter a number: "))

        if number < 2:
            print("Not a prime number.")
        else:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print("Prime number!")
            else:
                print("Not a prime number.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
