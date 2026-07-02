# Task Manager

A command-line task manager built in Python with JSON-based file persistence. Add, list, complete, and delete tasks that persist between sessions.

## Features

- Add tasks with an auto-assigned ID
- List all tasks with completion status
- Mark tasks as complete
- Delete tasks by ID
- Data persists between sessions via a local JSON file

## Tech Stack

- Python 3
- JSON (file-based persistence)
- Standard library only (no external dependencies)

## Usage

```bash
python3 tasks.py add 'buy groceries'   # Add a task
python3 tasks.py list                  # Show all tasks
python3 tasks.py done 1                # Mark task 1 as complete
python3 tasks.py delete 1              # Delete task 1
```

## What I Learned

- Reading and writing structured data with the JSON module
- Persisting application state to disk between sessions
- Parsing command-line arguments with sys.argv
- Structuring a CLI application with clean, single-purpose functions
- Handling edge cases (missing IDs, empty task lists) gracefully

## Next Steps

- Add due dates and priority levels
- Add a search/filter command
- Migrate persistence from JSON to SQLite
