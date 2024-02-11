# task.py

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.description} - {status}"
