# Architecture Document

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           AIPrepApp (Orchestrator)                       │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                          CLI Menu Loop                           │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────┐  │    │
│  │  │ Profile  │ │ Learning │ │ Project  │ │   Goal   │ │Report│  │    │
│  │  │  Menu    │ │  Menu    │ │  Menu    │ │  Menu    │ │ Menu │  │    │
│  │  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └──┬───┘  │    │
│  └───────┼────────────┼────────────┼────────────┼───────────┼──────┘    │
│          │            │            │            │           │           │
│  ┌───────▼────────────▼────────────▼────────────▼───────────▼──────┐   │
│  │                          Data Layer                               │   │
│  │  ┌──────────────────────────────────────────────────────────┐    │   │
│  │  │                  DataPersistence (JSON)                   │    │   │
│  │  │  save() → data.json + data.json.bak                      │    │   │
│  │  │  load() ← data.json                                      │    │   │
│  │  └──────────────────────────────────────────────────────────┘    │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘

Memory Layout (in‑app data):

┌─────────────────────────────────────────┐
│  data = {                                │
│    "profiles": {                         │
│      "alice": { name, email, ... },      │
│      "bob":   { name, email, ... }       │
│    },                                    │
│    "topics": [                           │
│      { name, difficulty, status, ts }    │
│    ],                                    │
│    "projects": [                         │
│      { name, desc, tech, status }        │
│    ],                                    │
│    "goals": [                            │
│      { desc, type, deadline, done, ts }  │
│    ]                                     │
│  }                                       │
└─────────────────────────────────────────┘
```

## Component Overview

| Component            | Responsibility                                                      |
|----------------------|---------------------------------------------------------------------|
| `AIPrepApp`          | Orchestrator; owns the main loop and sub‑menu dispatch              |
| `UserProfileManager` | CRUD for user profiles stored as `dict[name → profile_dict]`        |
| `LearningTracker`    | Manage list of topics with status tracking and completion stats     |
| `ProjectTracker`     | Manage list of projects with status updates and filtering           |
| `GoalTracker`        | Manage list of goals with deadlines, streaks, and overdue detection |
| `ProgressReport`     | Read‑only; aggregates data from all managers to produce reports     |
| `DataPersistence`    | Static methods to serialise/deserialise the full app state as JSON  |

## Data Flow

1. **Startup**: `AIPrepApp.run()` calls `DataPersistence.load()`. If the file exists and is valid JSON, the returned dict populates every manager. If the file is missing or corrupt, an empty state is used.
2. **Runtime**: The user interacts via the menu loop. Every mutating operation (create, update, delete) calls `_save_state()` immediately after the change.
3. **Shutdown**: When the user selects "Save & Exit", `DataPersistence.save()` is called one final time, creating a backup of the previous data first.

## Module Descriptions

### 1. User Profile Manager
- **Key concepts**: Variables, dictionaries, string manipulation, input handling
- **Data structure**: `dict[str, dict]` — name maps to profile dict with keys: `name`, `email`, `experience_level`, `interests`
- **Operations**: Create, read (single + list), update, delete
- **Edge cases**: Duplicate names, empty strings, missing fields on update

### 2. Learning Tracker
- **Key concepts**: Functions, lists, conditionals, loops
- **Data structure**: `list[dict]` — each dict: `name`, `difficulty`, `status`, `created_at`, `updated_at`
- **Operations**: Add topic, update status, view grouped, completion %
- **Edge cases**: Invalid status values, empty topic list (division by zero)

### 3. Project Tracker
- **Key concepts**: Classes, file I/O preparation, error handling
- **Data structure**: `list[dict]` — each dict: `name`, `description`, `technologies`, `status`, `created_at`
- **Operations**: Add, update status, list all, filter by status or tech
- **Edge cases**: Filter with no matches, updating non‑existent project

### 4. Goal Tracker
- **Key concepts**: Strings, datetime, persistence interaction
- **Data structure**: `list[dict]` — each dict: `description`, `type` (daily/weekly/monthly), `deadline`, `completed`, `created_at`, `completed_at`
- **Operations**: Add goal, mark complete, view current (incomplete), streaks, overdue detection
- **Edge cases**: Past deadlines, multiple completions on same day (streak logic), no goals yet

### 5. Progress Reports
- **Key concepts**: Loops, calculations, string formatting
- **Data**: Aggregated read‑only view across all managers
- **Sections**: Overall summary, topic stats, project breakdown, goal stats, timeline, text export
- **Edge cases**: Empty data (friendly messages instead of zeros)

### 6. Data Persistence
- **Key concepts**: JSON file handling, exceptions, backups
- **Methods**: `save(data)` → writes `data.json`, creates `data.json.bak` from existing file; `load()` → reads and parses `data.json`
- **Error handling**: `FileNotFoundError` → return `{}`; `json.JSONDecodeError` → warn and return `{}`; `IOError` → print error

## Design Decisions

1. **Manager pattern**: Each domain is a separate class, making testing and future replacement (e.g., SQLite backend) straightforward.
2. **Single JSON file**: Simple for a console app; no external database needed. The in‑memory representation is always a single `dict`, so serialisation is trivial.
3. **Auto‑save on every mutation**: Avoids data loss. The trade‑off (many small writes) is acceptable for this scale.
4. **Backup before write**: Renaming the existing file to `.bak` before writing prevents total data loss on write failure.
5. **Match‑case menu dispatch**: Cleaner than if‑elif chains; requires Python ≥ 3.10.
6. **Type hints everywhere**: Serves as documentation and enables static checking with `mypy`.

## Future Improvements

- Replace JSON with SQLite for concurrent access and querying
- Add an abstraction layer (`StorageBackend`) so the app is storage‑agnostic
- Implement logging instead of `print` for audit trails
- Add a GUI (Tkinter / PyQt) or web frontend (FastAPI + HTML)
- Introduce user authentication for multi‑user support
- Write property‑based tests with `hypothesis`
- Add CI/CD pipeline (GitHub Actions) for automated linting and testing
