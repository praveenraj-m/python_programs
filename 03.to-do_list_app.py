# To-Do List App

# Function to add a task to the tasks list
def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully.")

# Function to view tasks in the tasks list
def view_tasks(tasks):
    print("Tasks:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

# Function to delete a task from the tasks list
def delete_task(tasks, index_to_delete):
    if 1 <= index_to_delete <= len(tasks):
        del tasks[index_to_delete - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number. No task deleted.")

# Main function for the To-Do List App
def todo_list_app():
    tasks = []

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            try:
                index_to_delete = int(input("Enter the task number to delete: "))
                delete_task(tasks, index_to_delete)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the To-Do List App
todo_list_app()
