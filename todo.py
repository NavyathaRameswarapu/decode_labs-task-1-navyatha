# ==============================
# SIMPLE TO-DO LIST PROJECT
# ==============================

# Empty list to store tasks
tasks = []

# Infinite loop
while True:

    # Menu
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    # User input
    choice = input("Enter your choice: ")

    # ==============================
    # ADD TASK
    # ==============================
    if choice == "1":

        task = input("Enter task: ")

        tasks.append(task)

        print("Task added successfully!")

    # ==============================
    # VIEW TASKS
    # ==============================
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for index, task in enumerate(tasks, start=1):
                print(index, ".", task)

    # ==============================
    # REMOVE TASK
    # ==============================
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to remove.")

        else:
            print("\nTasks:")

            for index, task in enumerate(tasks, start=1):
                print(index, ".", task)

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):

                removed_task = tasks.pop(task_number - 1)

                print(removed_task, "removed successfully!")

            else:
                print("Invalid task number.")

    # ==============================
    # EXIT
    # ==============================
    elif choice == "4":

        print("Exiting To-Do List...")

        break

    # ==============================
    # INVALID CHOICE
    # ==============================
    else:

        print("Invalid choice. Please try again.")
