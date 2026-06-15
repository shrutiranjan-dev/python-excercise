# Capstone Exercises — Post‑Project Reinforcement

## Reflection Questions

Answer each question in 2–5 sentences. These are designed to test your understanding of the design decisions made in the capstone.

1. **Why is `DataPersistence` implemented with static methods rather than instance methods?** What advantage does this give when saving/loading state from multiple places in the app?

2. **The `UserProfileManager` stores profiles in a `dict[str, dict]` keyed by name, while `LearningTracker` stores topics in a `list[dict]`. Why were different collection types chosen?** When would you use one over the other?

3. **The streak calculation in `GoalTracker.get_streak()` counts consecutive *days* even for weekly goals. Is this correct behaviour?** How would you change the logic if you wanted a weekly goal to contribute to a "weeks" streak instead?

4. **The `_save_state()` method is called after every mutating operation. What are the trade‑offs of this approach vs. saving only on explicit "Save & Exit"?**

5. **In `ProgressReport.activity_timeline()`, duplicate timestamps can appear (e.g., a topic's `created_at` and `updated_at` could be the same). How could you deduplicate events to show a cleaner timeline?**

6. **The `completed_solution.py` uses `match`/`case` for menu dispatch. Rewrite option 4 of the main menu using `if`/`elif`/`else`. Which style do you prefer and why?**

7. **The project uses a single JSON file for all data. What problems would arise if two instances of the app ran simultaneously?** How would you solve this?

8. **Type hints are used throughout but never enforced at runtime. What is the purpose of type hints if Python ignores them?** Name one tool that checks them statically.

9. **The `GoalTracker.add_goal` method defaults the deadline based on goal type. Is it a good idea to compute defaults inside the model layer?** When might you want the UI to control the default instead?

10. **Looking at the `completed_solution.py` as a whole, what is the single most important refactoring you would do next to improve maintainability?** Justify your answer.

---

## Enhancement Challenges

Each challenge adds a significant new capability. Attempt them in order.

### Challenge 1: CLI Argument Support (`argparse`)

Add command‑line argument parsing so the app can run in **headless mode**. Support the following arguments:

```
python completed_solution.py --add-profile "Alice" --email alice@example.com --exp intermediate
python completed_solution.py --report --export report.txt
python completed_solution.py --topic-stats
```

Hints:
- Use the `argparse` module from the standard library.
- When CLI flags are provided, perform the action and exit without showing the interactive menu.
- When no flags are provided, fall back to the normal interactive loop.

### Challenge 2: SQLite Database Backend

Replace the JSON file persistence with a **SQLite database** (`sqlite3` module). Keep the same `DataPersistence` interface so the rest of the app does not change.

Schema:

```sql
CREATE TABLE profiles (
    name TEXT PRIMARY KEY,
    email TEXT,
    experience_level TEXT,
    interests TEXT,
    created_at TEXT
);

CREATE TABLE topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    difficulty TEXT,
    status TEXT,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    technologies TEXT,
    status TEXT,
    created_at TEXT
);

CREATE TABLE goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    type TEXT,
    deadline TEXT,
    completed INTEGER,
    completed_at TEXT,
    created_at TEXT
);
```

### Challenge 3: API Endpoints (FastAPI Integration Prep)

Add a lightweight HTTP API using `http.server` so the app's data can be queried over HTTP.

Endpoints to implement:

```
GET  /profiles          → JSON list of all profiles
GET  /profiles/{name}   → JSON single profile
GET  /topics            → JSON list of all topics
GET  /projects          → JSON list of all projects
GET  /goals             → JSON list of all goals
GET  /stats             → JSON overall summary stats
POST /goals/{id}/complete → mark goal as completed
```

Hints:
- Use `http.server.BaseHTTPRequestHandler`.
- Run the server on `localhost:8000` in a background thread.
- The app's data structures can be accessed in‑memory; no need to load from disk for every request.

### Challenge 4: Analytics Dashboard

Generate simple text‑based charts using the data. Add a new section to the report menu.

Features:
- **Bar chart of topics by difficulty** (`beginner`, `intermediate`, `advanced`)
- **Bar chart of projects by status** (`planning`, `in_progress`, `completed`, `on_hold`)
- **Goal completion trend** — number of goals completed per day for the last 7 days

Example output:

```
Topics by Difficulty:
  beginner    ████████████ 5
  intermediate ██████ 3
  advanced    ██ 1

Projects by Status:
  planning    ████████████████████ 3
  in_progress ██████████ 2
  completed   ██████████████████████████████ 5
  on_hold     ██ 1
```

Hints:
- Use unicode characters `█` (U+2588), `▄`, `▀` for the bars.
- Scale bars so the maximum value fills 30 characters.
- No external plotting library needed.

### Challenge 5: Multi‑User Support

Extend the app so multiple users can each have their own *entirely separate* set of data (profiles, topics, projects, goals).

Implementation ideas:
- Add a login screen on startup (choose or create a username).
- Store data per user: `data_{username}.json` instead of `data.json`.
- The `UserProfileManager` becomes redundant (or becomes a global settings store).
- All other managers are scoped to the logged‑in user.

---

## Debugging Challenges

Each snippet contains at least one bug. Identify the bug, explain why it is a bug, and write the corrected line(s).

### Debugging Challenge 1 — Streak Off‑by‑One

```python
def get_streak(self) -> int:
    completed_dates: set[date] = set()
    for goal in self.goals:
        if goal["completed"] and goal["completed_at"]:
            completed_dates.add(
                datetime.strptime(goal["completed_at"], "%Y-%m-%d").date()
            )
    if not completed_dates:
        return 0
    sorted_dates = sorted(completed_dates, reverse=True)
    today = date.today()
    if sorted_dates[0] != today:
        return 0
    streak = 0
    check_date = sorted_dates[0]
    for d in sorted_dates:
        if d == check_date:
            streak += 1
            check_date -= timedelta(days=1)
    return streak
```

**Bug?** (Write your answer, then check the solution below.)

<details>
<summary>Solution</summary>

The loop never breaks when a gap is found. If dates are `[2026-06-16, 2026-06-15, 2026-06-13]`, it will count `2026-06-16` (streak=1), then `2026-06-15` (streak=2), then `2026-06-13` — which does not equal `check_date` (`2026-06-14`), but the loop continues and when `d (2026-06-13) == check_date (2026-06-14)` is false, it proceeds to the next iteration without breaking. However, since it's the last element, the loop ends anyway, and the streak is incorrectly 2.

**Fix**: Add `else: break` inside the loop after the streak check.

```python
    for d in sorted_dates:
        if d == check_date:
            streak += 1
            check_date -= timedelta(days=1)
        else:
            break
```
</details>

---

### Debugging Challenge 2 — JSON Serialisation Error

```python
import json
from datetime import date

data = {
    "goals": [
        {
            "description": "Study transformers",
            "completed": False,
            "deadline": date(2026, 7, 1),
        }
    ]
}

with open("goals.json", "w") as f:
    json.dump(data, f)
```

**Bug?** (Write your answer, then check the solution below.)

<details>
<summary>Solution</summary>

`date` objects are not JSON serialisable by default. Running this code raises `TypeError: Object of type date is not JSON serializable`.

**Fix**: Either convert the date to a string before serialising, or provide a custom default encoder.

```python
data = {
    "goals": [
        {
            "description": "Study transformers",
            "completed": False,
            "deadline": "2026-07-01",   # use string
        }
    ]
}
```

Alternatively, use a custom encoder:

```python
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

json.dump(data, f, cls=DateEncoder)
```
</details>

---

### Debugging Challenge 3 — Menu Infinite Loop

```python
def run(self):
    while True:
        self.display_menu()
        choice = input("Select option (1-6): ")
        match choice:
            case "1":
                self._profile_menu()
            case "2":
                self._learning_menu()
            case "6":
                print("Goodbye!")
                break
```

Assume `_profile_menu()` and `_learning_menu()` each have their own inner `while True` loops with a "Back" option that simply `break`s out of the inner loop.

**Bug?** (Write your answer, then check the solution below.)

<details>
<summary>Solution</summary>

There is no bug in the code as shown — but the *assumption* is dangerous. If any sub‑menu's "Back" option uses `return` instead of `break`, it would return from `run()` entirely, ending the program. The actual bug here is a **design fragility**: the outer loop relies on sub‑menu methods returning normally after the user picks "Back". A student might accidentally use `return` in a sub‑menu, thinking it returns to the main menu.

A more defensive pattern is to catch unexpected returns:

```python
while True:
    self.display_menu()
    choice = input("Select option (1-6): ")
    if choice not in ("1", "2", "3", "4", "5", "6"):
        print("Invalid choice!")
        continue
    if choice == "6":
        print("Goodbye!")
        break
    # dispatch, but don't assume sub-menu will return
    try:
        match choice:
            case "1": self._profile_menu()
            case "2": self._learning_menu()
            # ...
    except SystemExit:  # allow deliberate exit
        raise
    except Exception:
        print("Unexpected error in sub‑menu, returning to main menu.")
```
</details>
