import json
import os
import sys

# The file where tasks are saved between sessions
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. Return empty list if file doesn't exist yet."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    """Add a new task with a title."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added: '{title}'")

def list_tasks():
    """Print all tasks to the terminal."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: python3 tasks.py add 'your task'")
        return
    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "✓" if task["done"] else "○"
        print(f"  [{status}] {task['id']}. {task['title']}")
    print()

def complete_task(task_id):
    """Mark a task as done by its ID number."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"✓ Completed: '{task['title']}'")
            return
    print(f"No task found with ID {task_id}")

def delete_task(task_id):
    """Remove a task permanently by its ID number."""
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"No task found with ID {task_id}")
        return
    save_tasks(new_tasks)
    print(f"🗑 Deleted task {task_id}")

def show_help():
    print("""
Task Manager — Commands:
  python3 tasks.py add 'buy groceries'   → Add a task
  python3 tasks.py list                  → Show all tasks
  python3 tasks.py done 1                → Mark task 1 as complete
  python3 tasks.py delete 1             → Delete task 1
""")

# --- Entry point: read what the user typed ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    elif sys.argv[1] == "add" and len(sys.argv) > 2:
        add_task(sys.argv[2])
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "done" and len(sys.argv) > 2:
        complete_task(int(sys.argv[2]))
    elif sys.argv[1] == "delete" and len(sys.argv) > 2:
        delete_task(int(sys.argv[2]))
    else:
        show_help()