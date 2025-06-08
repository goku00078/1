# Global task list
todo_list = []

# Function to add a new task
def add_task():
    task = input("Enter a Task: ")
    todo_list.append({"task": task, "status": "pending"})
    print("New Task Added Successfully!\n")

# Function to view all tasks
def view_task():
    print("Your To-Do List:")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1): 
            print(f"{index}: {task['task']} - {task['status']}")
    print("\n")

# Function to remove a task
def remove_task():
    if len(todo_list) == 0:
        print("\nList is empty!")
    else:
        try:
            search_index = int(input("Enter the task number you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task removed: {removed_task['task']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

# Function to mark a task as done
def mark_done():
    if len(todo_list) == 0:
        print("\nList is empty!")
    else:
        try:
            search_index = int(input("Enter the task number you want to mark as complete: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]["status"] = 'done' 
                print(f"Task '{todo_list[search_index]['task']}' has been marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

# Menu loop
def menu():
    while True:
        print("*** Main Menu ***")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task") 
        print("4. Mark a task as completed") 
        print("5. Exit") 

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the task manager.")
            break
        else:
            print("Invalid choice! Try again.")

# Start the program
print(menu)
