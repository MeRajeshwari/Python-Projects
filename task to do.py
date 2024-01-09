# Create an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to display all tasks
def show_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks added yet.")

# Function to remove a task by its index
def remove_task(index):
    if index >= 1 and index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid index.")

# Sample usage:
add_task("Buy groceries")
add_task("Finish homework")
show_tasks()
remove_task(1)
show_tasks()
