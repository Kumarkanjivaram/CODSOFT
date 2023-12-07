def show_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def add_task():
    new_task = input("Enter a task: ")
    tasks.append(new_task)

def remove_task():
    task_num = int(input("Enter task number to remove: "))
    del tasks[task_num-1]

def mark_completed():
    task_num = int(input("Enter task number to mark completed: "))
    tasks[task_num-1] += " [Completed]"

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

tasks = []  # Initialize empty task list
load_tasks()  # Load tasks from file if exists

menu_options = {
    "1": show_tasks,
    "2": add_task,
    "3": remove_task,
    "4": mark_completed,
    "5": save_tasks,
    "6": exit,
}

while True:
    print("\nTo-Do List")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark completed")
    print("5. Save tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")