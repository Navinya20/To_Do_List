# todolist.py
from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_task_completed(self, task):
        task.completed = True

    def display_tasks(self):
        for task in self.tasks:
            print(task)
