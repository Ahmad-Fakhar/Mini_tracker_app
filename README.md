# Task Tracker

A simple menu-based Python Task Tracker that allows users to add, view, complete, and delete tasks. The application stores tasks in a JSON file so that saved tasks can be loaded again when the program runs.

## Features

- Add new tasks with a title.
- View all tasks with their numbers and statuses.
- Mark tasks as completed.
- Delete selected tasks.
- Save tasks in a JSON file using `json.dump()`.
- Load saved tasks using `json.load()`.
- Handle empty task titles and invalid menu choices.
- Validate task numbers and handle missing or invalid JSON files.

## Technologies Used

- Python 3
- JSON
- `pathlib`
- Python standard library

## Project Structure

```text
task-tracker/
├── mini_task_tracker.py
├── README.md
└── tasks.json
```

**Note:** The `tasks.json` file is created automatically when tasks are saved.

## How to Run

1. Install Python 3.
2. Open the project folder in a terminal.
3. Run the following command:

   ```bash
   python mini_task_tracker.py
   ```

4. Follow the menu instructions to manage your tasks.

## Menu Options

1. **Add Task:** Enter a title to create a new task.
2. **View Tasks:** Display all tasks and their current statuses.
3. **Complete Task:** Select a task number to mark it as Done.
4. **Delete Task:** Select a task number to remove it.
5. **Exit:** Close the application.

## Data Storage

Tasks are stored in `tasks.json` as a list of dictionaries. Each task contains a `title` and a `done` status.

Example:

```json
[
    {
        "title": "Read Python notes",
        "done": false
    },
    {
        "title": "Complete assignment",
        "done": true
    }
]
```

The program loads saved tasks at startup and updates the JSON file whenever a task is added, completed, or deleted.

## Concepts Demonstrated

- Functions and docstrings
- Lists and dictionaries
- Loops and conditional statements
- User input and validation
- File handling
- JSON data storage
- Exception handling
- Modular programming

## Project Goal

The goal of this mini project is to practise Python fundamentals by building a practical task management application with persistent JSON storage.

## Author

AI Engineering — Week 1, Day 2 Python Mini Project
