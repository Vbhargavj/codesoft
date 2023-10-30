def add_task(todo_list, task):
    todo_list.append({"task": task, "completed": False})

def view_tasks(todo_list):
    for i, task in enumerate(todo_list, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']}")

def update_task(todo_list, task_index, new_task):
    if 0 < task_index <= len(todo_list):
        todo_list[task_index - 1]["task"] = new_task

def mark_completed(todo_list, task_index):
    if 0 < task_index <= len(todo_list):
        todo_list[task_index - 1]["completed"] = True

def main():
    todo_list = []

    while True:
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark as Completed")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter a new task: ")
            add_task(todo_list, task)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            view_tasks(todo_list)
            task_index = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            update_task(todo_list, task_index, new_task)
        elif choice == "4":
            view_tasks(todo_list)
            task_index = int(input("Enter the task number to mark as completed: "))
            mark_completed(todo_list, task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
