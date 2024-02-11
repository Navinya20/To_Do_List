from task import Task
from todolist import ToDoList

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task = Task(description)
            todo_list.add_task(task)

        elif choice == "2":
            description = input("Enter task description to remove: ")
            task = next((t for t in todo_list.tasks if t.description == description), None)
            if task:
                todo_list.remove_task(task)
            else:
                print("Task not found.")

        elif choice == "3":
            description = input("Enter task description to mark as completed: ")
            task = next((t for t in todo_list.tasks if t.description == description), None)
            if task:
                todo_list.mark_task_completed(task)
            else:
                print("Task not found.")

        elif choice == "4":
            print("\nTasks:")
            todo_list.display_tasks()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
