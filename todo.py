tasks = []
# DONE BY = SHAIK FARDEEN BASHA, VYSHNAVI TALLAM, SHREEYANSHI GAUTAM, JAYA SHANKAR, PRASANNA KUMAR NAYAK, RAJENDRA PRASAD
def addTask():
    task_name = input("Please enter a task: ")
    priority = input("Enter priority (high, medium, low): ").lower()
    task_time = input('Enter the time of task (hrs): ')
    tasks.append({"name": task_name, "priority": priority, "time": task_time})
    print(f"Task '{task_name}' with priority '{priority}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index + 1}: {task['name']} [{task['priority']}] at {task['time']}")

def deleteTask():
    if not tasks:
        print("There are no tasks to delete.")
        return
    listTasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"Task #{index + 1} '{deleted_task['name']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def searchTask():
    search_query = input("Enter search term: ").lower()
    found_tasks = [task for task in tasks if search_query in task['name'].lower()]
    if found_tasks:
        print("Matching Tasks:")
        for idx, task in enumerate(found_tasks, 1):
            print(f"{idx}. {task['name']} [{task['priority']}] at {task['time']}")
    else:
        print("No tasks found matching the search term.")

def sortTasksByPriority():
    priority_order = {"high": 1, "medium": 2, "low": 3}
    tasks.sort(key=lambda task: priority_order.get(task['priority'], 4))
    print("Tasks sorted by priority.")

def backupTasks():
    try:
        with open('SAPNUPUAS/backup_todo_data.txt', 'a') as file:
            for task in tasks:
                file.write(f"{task['name']}|{task['priority']}|{task['time']}\n")
        print("Tasks backed up successfully!")
    except Exception as e:
        print(f"An error occurred while backing up tasks: {e}")

def restoreTasks():
    try:
        with open('SAPNUPUAS/backup_todo_data.txt', 'r') as file:
            lines = file.readlines()
            tasks.clear()
            for line in lines:
                name, priority, time = line.strip().split('|')
                tasks.append({"name": name, "priority": priority, "time": time})
        print("Tasks restored successfully!")
    except FileNotFoundError:
        print("No backup data found.")
    except Exception as e:
        print(f"An error occurred while restoring tasks: {e}")

if __name__ == "__main__":
    print("Welcome to the to-do list app :)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Search tasks")
        print("5. Sort tasks by priority")
        print("6. Backup tasks")
        print("7. Restore tasks")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            searchTask()
        elif choice == "5":
            sortTasksByPriority()
        elif choice == "6":
            backupTasks()
        elif choice == "7":
            restoreTasks()
        elif choice == "8":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye 👋👋")