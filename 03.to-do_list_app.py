# To-Do List App
def todo_list_app():
    # Initialize an empty list to store tasks
    tasks = []

    # Main loop for the To-Do List App
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Quit")

        # Get user input for menu choice
        choice = input("Enter your choice: ")

        # Add a new task to the list
        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
        # View and display existing tasks
        elif choice == '2':
            print("Tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
        # Quit the app
        elif choice == '3':
            print("Goodbye!")
            break
        # Handle invalid choices
        else:
            print("Invalid choice. Try again.")

# Run the To-Do List App
todo_list_app()
