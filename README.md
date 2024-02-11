# To-Do List Application

A simple console-based to-do list application implemented in Python. This project is designed to help beginners grasp fundamental programming concepts such as classes, file handling, and user interaction.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Code Structure](#code-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This to-do list application allows users to manage their tasks through a console-based interface. Users can add tasks, mark them as completed, remove tasks, and view the list of tasks.

## Key Features

- **Task Management:** Add, remove, and mark tasks as completed.
- **Persistent Storage:** Tasks are saved to a file for future use.
- **Simple User Interface:** Console-based interface for ease of use.

## Code Structure

### `task.py`

```python
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.description} - {status}"
```

### `todolist.py`

```python
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
```

### `todo.py`

```python
from task import Task
from todolist import ToDoList

def main():
    todo_list = ToDoList()

    # ... (rest of the code)
```

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ToDoListApp.git
   cd ToDoListApp
   ```

2. Run the application:

   ```bash
   python todo.py
   ```

## Usage

Follow the on-screen prompts to interact with the to-do list application. Choose options to add tasks, remove tasks, mark tasks as completed, and view the list of tasks.

## Contributing

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request.


