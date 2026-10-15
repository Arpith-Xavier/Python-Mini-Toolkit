
import json
from pathlib import Path

FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if FILE.exists():
        try:
            with FILE.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved tasks.")
    return []


def save_tasks(tasks):
    with FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    print("\n========= YOUR TASKS =========")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. [{status}] {task['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST APP ======")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            title = input("Enter your task: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                save_tasks(tasks)
                print("Task added!")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    number = int(input("Task number to complete: "))
                    if 1 <= number <= len(tasks):
                        tasks[number - 1]["completed"] = True
                        save_tasks(tasks)
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid whole number.")

        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                try:
                    number = int(input("Task number to delete: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        save_tasks(tasks)
                        print(f"Deleted: {removed['title']}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid whole number.")

        elif choice == "5":
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
