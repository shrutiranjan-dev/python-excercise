# AI Engineer Preparation Console App - Capstone Project

## Overview

This capstone project consolidates everything learned across the 13-module Python Phase 1 curriculum into a single, production‑quality console application. You will build an **AI Engineer Preparation Console App** that manages user profiles, tracks learning topics, monitors projects, sets goals, generates progress reports, and persists all data to disk.

The project is intentionally open‑ended: it provides a complete skeleton with type hints and docstrings, and you must implement the core logic. By the end, you will have a portfolio‑worthy application demonstrating mastery of Python fundamentals.

## Prerequisites

You must have completed all 13 modules of **Python Phase 1 – Fundamentals**:

1. Python Basics & Environment Setup
2. Variables & Data Types
3. Strings & String Manipulation
4. Lists & List Operations
5. Dictionaries & Dictionary Methods
6. Conditionals & Decision Making
7. Loops & Iteration
8. Functions & Modular Programming
9. Classes & Object‑Oriented Programming
10. File I/O & Working with Files
11. Exception Handling & Debugging
12. Modules, Packages & Imports
13. Working with Dates & Times (datetime)

## Features

### 1. User Profile Manager
- Create a profile with name, email, experience level, and interests
- View a single profile or list all profiles
- Update any profile field
- Delete a profile

### 2. Learning Tracker
- Add learning topics with difficulty and status (`not_started`, `in_progress`, `completed`)
- Update topic status
- View topics grouped by status
- Display overall completion percentage

### 3. Project Tracker
- Add projects with description, technologies used, and status
- Update project status
- List all projects, optionally filtered by status or technology

### 4. Goal Tracker
- Set daily, weekly, or monthly goals with deadlines
- Mark goals as completed
- View current (incomplete) goals
- Track goal streaks (consecutive days with completed goals)
- Detect and highlight overdue goals

### 5. Progress Reports
- Overall progress summary
- Topics completed vs. total
- Projects grouped by status
- Goal completion rate
- Activity timeline (recent additions/completions)
- Export report as a plain‑text file

### 6. Data Persistence
- Auto‑save to a JSON file after every change
- Load data automatically on startup
- Graceful handling of corrupt or missing data files
- Automatic backup before saving

## Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│                   AIPrepApp (Main)                   │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│  │UserProfile   │ │ Learning     │ │ Project      │ │
│  │Manager       │ │ Tracker      │ │ Tracker      │ │
│  └──────────────┘ └──────────────┘ └──────────────┘ │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│  │ GoalTracker  │ │ Progress     │ │ Data         │ │
│  │              │ │ Report       │ │ Persistence  │ │
│  └──────────────┘ └──────────────┘ └──────────────┘ │
└─────────────────────────────────────────────────────┘
```

The app follows a **modular manager pattern**. Each domain concern is encapsulated in its own class. `DataPersistence` acts as a centralised I/O layer. `AIPrepApp` orchestrates everything and drives the CLI menu loop.

## How to Run

```bash
# Navigate to the capstone directory
cd python-phase-1-fundamentals/final_capstone_project

# Run the starter skeleton (stub implementation)
python starter_code.py

# Run the completed solution
python completed_solution.py
```

No external dependencies are required—only the Python standard library.

## Expected Learning Outcomes

After completing this capstone you will be able to:

- Design and structure a multi‑class Python application from scratch
- Use dictionaries, lists, and custom objects to model real‑world data
- Write modular, reusable functions and methods
- Handle files and JSON serialisation with proper error handling
- Implement a text‑based user interface with input validation
- Generate formatted textual reports
- Debug and extend an existing codebase confidently

## Grading Rubric

| Criterion                    | Points | Description                                                |
|------------------------------|--------|------------------------------------------------------------|
| Profile Manager              | 15     | CRUD operations work, data validates, edge cases handled   |
| Learning Tracker             | 15     | Topics can be added, updated, grouped, percentage computed |
| Project Tracker              | 15     | Projects CRUD, filtering by status / technology            |
| Goal Tracker                 | 15     | Goals CRUD, streak tracking, overdue detection             |
| Progress Reports             | 15     | All report sections present, export works                  |
| Data Persistence             | 10     | Save / load / backup, corrupted file handling              |
| Code Quality                 | 10     | Type hints, docstrings, naming conventions, no dead code   |
| Error Handling & UX          | 5      | Invalid input handled gracefully, informative messages     |
| **Total**                    | **100**|                                                            |

## Extension Ideas

- Add CLI argument parsing with `argparse` for headless operation
- Replace JSON storage with SQLite (`sqlite3`)
- Wrap the app with a FastAPI REST API
- Build a simple analytics dashboard with `matplotlib`
- Add multi‑user support with login/authentication
- Containerise with Docker
- Write unit tests with `pytest`
