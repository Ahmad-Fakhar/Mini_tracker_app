"""
Task Tracker
A simple menu-based task manager that stores tasks in tasks.json.

Run:
    python mini_task_tracker.py
"""

import json
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load saved tasks; return an empty list if the file does not exist."""
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            raise ValueError("The top-level JSON value must be a list.")

        for task in tasks:
            if (
                not isinstance(task, dict)
                or not isinstance(task.get("title"), str)
                or not isinstance(task.get("done"), bool)
            ):
                raise ValueError("Each task must have a title and a done status.")

        return tasks

    except (json.JSONDecodeError, ValueError, OSError) as error:
        print(f"Warning: tasks.json could not be loaded ({error}).")
        print("Starting with an empty task list.")
        return []


def save_tasks(tasks):
    """Write all tasks to the JSON file."""
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
    except OSError as error:
        print(f"Error: tasks could not be saved ({error}).")


def add_task(tasks):
    """Ask for a title and add a new pending task."""
    title = input("Task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Display all tasks with their current status."""
    print("\n--- TASK LIST ---")

    if not tasks:
        print("No tasks yet. Choose Add to create your first task.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def select_task(tasks):
    """Return the selected task's list index, or None for invalid input."""
    if not tasks:
        print("There are no tasks to select.")
        return None

    view_tasks(tasks)

    try:
        task_number = int(input("Task number: ").strip())
    except ValueError:
        print("Please enter a valid whole number.")
        return None

    if not 1 <= task_number <= len(tasks):
        print(f"Invalid task number. Choose a number from 1 to {len(tasks)}.")
        return None

    return task_number - 1


def complete_task(tasks):
    """Mark the selected task as done and save the change."""
    index = select_task(tasks)
    if index is None:
        return

    if tasks[index]["done"]:
        print("That task is already marked Done.")
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"Task completed: {tasks[index]['title']}")


def delete_task(tasks):
    """Remove the selected task and save the updated list."""
    index = select_task(tasks)
    if index is None:
        return

    removed_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Task deleted: {removed_task['title']}")


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 36)
    print("           TASK TRACKER")
    print("=" * 36)
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    """Run the task tracker until the user chooses Exit."""
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s).")

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Your tasks are saved in tasks.json.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
