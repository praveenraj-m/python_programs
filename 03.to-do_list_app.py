# To-Do List App
def todo_list_app():
    tasks = []

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
        elif choice == '2':
            print("Tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
todo_list_app()
