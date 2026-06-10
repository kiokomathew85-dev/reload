from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

tasks = []


def display_all_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\nAll Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(
            f"{index}. {task['title']} | "
            f"{task['description']} | "
            f"Due: {task['due_date']} | "
            f"Status: {status}"
        )


while True:
    print("\n===== TASK MANAGEMENT SYSTEM =====")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. Track Progress")
    print("5. View All Tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")

        add_task(tasks, title, description, due_date)

    elif choice == "2":
        display_all_tasks()

        try:
            task_number = int(
                input("Enter task number to complete: ")
            )
            mark_task_as_complete(tasks, task_number)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        view_pending_tasks(tasks)

    elif choice == "4":
        progress = calculate_progress(tasks)
        print(f"Progress: {progress:.2f}% Complete")

    elif choice == "5":
        display_all_tasks()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")