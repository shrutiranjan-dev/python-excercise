"""AI Engineer Preparation Console App — Complete Solution.

A production‑quality CLI application demonstrating mastery of Python
fundamentals across all 13 Phase 1 modules.
"""

import json
import os
import shutil
from datetime import datetime, date, timedelta
from typing import Optional, Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DATA_FILE = "data.json"
BACKUP_FILE = "data.json.bak"

TOPIC_STATUSES = ("not_started", "in_progress", "completed")
PROJECT_STATUSES = ("planning", "in_progress", "completed", "on_hold")
GOAL_TYPES = ("daily", "weekly", "monthly")
VALID_DIFFICULTIES = ("beginner", "intermediate", "advanced")


# ---------------------------------------------------------------------------
# Data Persistence
# ---------------------------------------------------------------------------

class DataPersistence:
    """Handles all JSON file read/write operations with error handling."""

    @staticmethod
    def save(data: dict) -> bool:
        """Save data dict to JSON file. Creates a backup of the existing file first.

        Args:
            data: The full application state dict.

        Returns:
            True if save succeeded, False otherwise.
        """
        try:
            if os.path.exists(DATA_FILE):
                shutil.copy2(DATA_FILE, BACKUP_FILE)
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            return True
        except IOError as e:
            print(f"Error saving data: {e}")
            return False

    @staticmethod
    def load() -> dict:
        """Load data from the JSON file.

        Returns:
            The data dict if loading succeeded, otherwise an empty dict.
        """
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Warning: Data file is corrupt. Starting with empty state.")
            return {}
        except IOError as e:
            print(f"Error loading data: {e}")
            return {}


# ---------------------------------------------------------------------------
# User Profile Manager
# ---------------------------------------------------------------------------

class UserProfileManager:
    """Manage user profiles. Profiles stored as dict[name -> profile_dict]."""

    def __init__(self):
        self.profiles: dict[str, dict] = {}

    def create_profile(self, name: str, email: str, experience_level: str,
                       interests: str) -> Optional[dict]:
        """Create a new user profile.

        Args:
            name: Profile name (must be non-empty and unique).
            email: Email address.
            experience_level: e.g. 'beginner', 'intermediate', 'advanced'.
            interests: Comma-separated interests.

        Returns:
            The created profile dict on success, or None if validation fails.
        """
        name = name.strip()
        if not name:
            print("Error: Name cannot be empty.")
            return None
        if name in self.profiles:
            print(f"Error: Profile '{name}' already exists.")
            return None
        profile = {
            "name": name,
            "email": email.strip(),
            "experience_level": experience_level.strip(),
            "interests": interests.strip(),
            "created_at": datetime.now().isoformat(),
        }
        self.profiles[name] = profile
        return profile

    def get_profile(self, name: str) -> Optional[dict]:
        """Retrieve a profile by name.

        Returns:
            The profile dict if found, or None.
        """
        return self.profiles.get(name)

    def update_profile(self, name: str, **kwargs) -> Optional[dict]:
        """Update fields on an existing profile.

        Accepted kwargs: email, experience_level, interests.
        Empty string values are ignored (field not updated).

        Returns:
            The updated profile dict, or None if profile not found.
        """
        profile = self.profiles.get(name)
        if not profile:
            print(f"Error: Profile '{name}' not found.")
            return None
        for key in ("email", "experience_level", "interests"):
            if key in kwargs and kwargs[key]:
                profile[key] = kwargs[key].strip()
        return profile

    def list_profiles(self) -> list[dict]:
        """Return all profiles as a list."""
        return list(self.profiles.values())

    def delete_profile(self, name: str) -> bool:
        """Delete a profile by name.

        Returns:
            True if deleted, False if not found.
        """
        if name in self.profiles:
            del self.profiles[name]
            return True
        print(f"Error: Profile '{name}' not found.")
        return False


# ---------------------------------------------------------------------------
# Learning Tracker
# ---------------------------------------------------------------------------

class LearningTracker:
    """Track learning topics with status and difficulty."""

    def __init__(self):
        self.topics: list[dict] = []

    def add_topic(self, name: str, difficulty: str,
                  status: str = "not_started") -> Optional[dict]:
        """Add a new learning topic.

        Args:
            name: Topic name (non-empty).
            difficulty: 'beginner', 'intermediate', or 'advanced'.
            status: One of TOPIC_STATUSES.

        Returns:
            The created topic dict on success, or None if validation fails.
        """
        name = name.strip()
        difficulty = difficulty.strip().lower()
        status = status.strip().lower()
        if not name:
            print("Error: Topic name cannot be empty.")
            return None
        if difficulty not in VALID_DIFFICULTIES:
            print(f"Error: Difficulty must be one of {VALID_DIFFICULTIES}.")
            return None
        if status not in TOPIC_STATUSES:
            print(f"Error: Status must be one of {TOPIC_STATUSES}.")
            return None
        now = datetime.now().isoformat()
        topic = {
            "name": name,
            "difficulty": difficulty,
            "status": status,
            "created_at": now,
            "updated_at": now,
        }
        self.topics.append(topic)
        return topic

    def update_status(self, name: str, new_status: str) -> bool:
        """Change the status of a topic.

        Returns:
            True if updated, False if topic not found or invalid status.
        """
        new_status = new_status.strip().lower()
        if new_status not in TOPIC_STATUSES:
            print(f"Error: Status must be one of {TOPIC_STATUSES}.")
            return False
        for topic in self.topics:
            if topic["name"] == name:
                topic["status"] = new_status
                topic["updated_at"] = datetime.now().isoformat()
                return True
        print(f"Error: Topic '{name}' not found.")
        return False

    def get_topics_by_status(self) -> dict[str, list[dict]]:
        """Group topics by their status.

        Returns:
            Dict like {'not_started': [...], 'in_progress': [...], 'completed': [...]}
        """
        result: dict[str, list[dict]] = {
            "not_started": [],
            "in_progress": [],
            "completed": [],
        }
        for topic in self.topics:
            result[topic["status"]].append(topic)
        return result

    def completion_percentage(self) -> float:
        """Calculate the percentage of completed topics.

        Returns:
            Float 0.0–100.0. Returns 0.0 if there are no topics.
        """
        if not self.topics:
            return 0.0
        completed = sum(1 for t in self.topics if t["status"] == "completed")
        return round((completed / len(self.topics)) * 100, 1)

    def list_topics(self) -> list[dict]:
        """Return all topics."""
        return self.topics


# ---------------------------------------------------------------------------
# Project Tracker
# ---------------------------------------------------------------------------

class ProjectTracker:
    """Manage AI/ML projects with status tracking and filtering."""

    def __init__(self):
        self.projects: list[dict] = []

    def add_project(self, name: str, description: str,
                    technologies: str, status: str = "planning") -> Optional[dict]:
        """Add a new project.

        Args:
            name: Project name (non-empty).
            description: Project description.
            technologies: Comma-separated technologies.
            status: One of PROJECT_STATUSES.

        Returns:
            The created project dict, or None if validation fails.
        """
        name = name.strip()
        status = status.strip().lower()
        if not name:
            print("Error: Project name cannot be empty.")
            return None
        if status not in PROJECT_STATUSES:
            print(f"Error: Status must be one of {PROJECT_STATUSES}.")
            return None
        project = {
            "name": name,
            "description": description.strip(),
            "technologies": technologies.strip(),
            "status": status,
            "created_at": datetime.now().isoformat(),
        }
        self.projects.append(project)
        return project

    def update_status(self, name: str, new_status: str) -> bool:
        """Update the status of a project.

        Returns:
            True if updated, False if not found or invalid status.
        """
        new_status = new_status.strip().lower()
        if new_status not in PROJECT_STATUSES:
            print(f"Error: Status must be one of {PROJECT_STATUSES}.")
            return False
        for project in self.projects:
            if project["name"] == name:
                project["status"] = new_status
                return True
        print(f"Error: Project '{name}' not found.")
        return False

    def list_projects(self, status: Optional[str] = None,
                      technology: Optional[str] = None) -> list[dict]:
        """List projects, optionally filtered by status or technology.

        Args:
            status: If provided, only return projects with this status.
            technology: If provided, only return projects that list this tech
                        (case-insensitive partial match).

        Returns:
            Filtered (or full) list of project dicts.
        """
        result = self.projects
        if status:
            status = status.strip().lower()
            result = [p for p in result if p["status"] == status]
        if technology:
            tech = technology.strip().lower()
            result = [
                p for p in result
                if tech in p["technologies"].lower()
            ]
        return result


# ---------------------------------------------------------------------------
# Goal Tracker
# ---------------------------------------------------------------------------

class GoalTracker:
    """Set and track daily/weekly/monthly goals with streak tracking."""

    def __init__(self):
        self.goals: list[dict] = []

    def add_goal(self, description: str, goal_type: str,
                 deadline: Optional[str] = None) -> Optional[dict]:
        """Add a new goal.

        Args:
            description: Goal description.
            goal_type: 'daily', 'weekly', or 'monthly'.
            deadline: Optional date string in YYYY-MM-DD format.
                      If not provided, defaults to a sensible value:
                      daily -> tomorrow, weekly -> 7 days from now,
                      monthly -> 30 days from now.

        Returns:
            The created goal dict, or None on validation failure.
        """
        description = description.strip()
        goal_type = goal_type.strip().lower()
        if not description:
            print("Error: Goal description cannot be empty.")
            return None
        if goal_type not in GOAL_TYPES:
            print(f"Error: Goal type must be one of {GOAL_TYPES}.")
            return None
        if deadline:
            try:
                deadline_date = datetime.strptime(deadline.strip(), "%Y-%m-%d").date()
            except ValueError:
                print("Error: Deadline must be in YYYY-MM-DD format.")
                return None
        else:
            today = date.today()
            if goal_type == "daily":
                deadline_date = today + timedelta(days=1)
            elif goal_type == "weekly":
                deadline_date = today + timedelta(weeks=1)
            else:
                deadline_date = today + timedelta(days=30)
        goal = {
            "description": description,
            "type": goal_type,
            "deadline": deadline_date.isoformat(),
            "completed": False,
            "completed_at": None,
            "created_at": datetime.now().isoformat(),
        }
        self.goals.append(goal)
        return goal

    def mark_completed(self, description: str) -> bool:
        """Mark a goal as completed.

        Sets both 'completed' to True and 'completed_at' to the current ISO date.

        Returns:
            True if found and updated, False otherwise.
        """
        for goal in self.goals:
            if goal["description"] == description and not goal["completed"]:
                goal["completed"] = True
                goal["completed_at"] = date.today().isoformat()
                return True
        print(f"Error: Incomplete goal '{description}' not found.")
        return False

    def get_current_goals(self) -> list[dict]:
        """Return all goals that are not yet completed, sorted by deadline ascending."""
        incomplete = [g for g in self.goals if not g["completed"]]
        incomplete.sort(key=lambda g: g["deadline"])
        return incomplete

    def get_streak(self) -> int:
        """Calculate the current goal streak.

        A streak is the number of consecutive days (up to today) on which
        AT LEAST ONE goal was completed.

        Returns:
            Integer streak count.
        """
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
            yesterday = today - timedelta(days=1)
            if sorted_dates[0] != yesterday:
                return 0
        streak = 0
        check_date = sorted_dates[0]
        for d in sorted_dates:
            if d == check_date:
                streak += 1
                check_date -= timedelta(days=1)
            else:
                break
        return streak

    def get_overdue_goals(self) -> list[dict]:
        """Return incomplete goals whose deadline is before today."""
        today = date.today().isoformat()
        return [
            g for g in self.goals
            if not g["completed"] and g["deadline"] < today
        ]


# ---------------------------------------------------------------------------
# Progress Reports
# ---------------------------------------------------------------------------

class ProgressReport:
    """Generate formatted progress reports from all data sources."""

    @staticmethod
    def _fmt_bool(val: bool) -> str:
        return "Yes" if val else "No"

    @staticmethod
    def overall_summary(profiles: dict, topics: list, projects: list,
                        goals: list) -> str:
        """Return a multi-line string summarising overall progress."""
        total_topics = len(topics)
        completed_topics = sum(1 for t in topics if t["status"] == "completed")
        total_projects = len(projects)
        completed_projects = sum(1 for p in projects if p["status"] == "completed")
        total_goals = len(goals)
        completed_goals = sum(1 for g in goals if g["completed"])
        topic_pct = round((completed_topics / total_topics * 100), 1) if total_topics else 0.0
        goal_pct = round((completed_goals / total_goals * 100), 1) if total_goals else 0.0

        lines = [
            "=" * 50,
            "  OVERALL PROGRESS SUMMARY",
            "=" * 50,
            f"  Profiles:          {len(profiles)}",
            f"  Topics:            {completed_topics}/{total_topics} ({topic_pct}%)",
            f"  Projects:          {completed_projects}/{total_projects}",
            f"  Goals:             {completed_goals}/{total_goals} ({goal_pct}%)",
            "=" * 50,
        ]
        return "\n".join(lines)

    @staticmethod
    def topic_report(topics: list) -> str:
        """Return a formatted report of topics grouped by status.

        Includes completion percentage.
        """
        groups: dict[str, list[dict]] = {
            "not_started": [],
            "in_progress": [],
            "completed": [],
        }
        for t in topics:
            groups[t["status"]].append(t)

        lines = [
            "-" * 50,
            "  TOPIC REPORT",
            "-" * 50,
        ]
        total = len(topics)
        completed = len(groups["completed"])
        pct = round((completed / total * 100), 1) if total else 0.0
        lines.append(f"  Completion: {completed}/{total} ({pct}%)\n")
        for status, label in [("not_started", "NOT STARTED"),
                              ("in_progress", "IN PROGRESS"),
                              ("completed", "COMPLETED")]:
            items = groups[status]
            lines.append(f"  [{label}] ({len(items)}):")
            if not items:
                lines.append("    (none)")
            else:
                for t in items:
                    lines.append(f"    - {t['name']} ({t['difficulty']})")
            lines.append("")
        return "\n".join(lines)

    @staticmethod
    def project_report(projects: list) -> str:
        """Return a formatted report of projects grouped by status."""
        groups: dict[str, list[dict]] = {s: [] for s in PROJECT_STATUSES}
        for p in projects:
            groups[p["status"]].append(p)

        lines = [
            "-" * 50,
            "  PROJECT REPORT",
            "-" * 50,
        ]
        for status in PROJECT_STATUSES:
            items = groups[status]
            lines.append(f"  [{status.upper()}] ({len(items)}):")
            if not items:
                lines.append("    (none)")
            else:
                for p in items:
                    lines.append(f"    - {p['name']} | Tech: {p['technologies']}")
            lines.append("")
        return "\n".join(lines)

    @staticmethod
    def goal_report(goals: list) -> str:
        """Return a formatted report of goals with completion rate and streak."""
        total = len(goals)
        completed = sum(1 for g in goals if g["completed"])
        pct = round((completed / total * 100), 1) if total else 0.0
        overdue = [g for g in goals if not g["completed"] and g["deadline"] < date.today().isoformat()]

        lines = [
            "-" * 50,
            "  GOAL REPORT",
            "-" * 50,
            f"  Total:     {total}",
            f"  Completed: {completed} ({pct}%)",
            f"  Overdue:   {len(overdue)}",
            "-" * 50,
        ]
        if goals:
            lines.append("\n  All Goals:")
            for g in goals:
                status = "Done" if g["completed"] else ("OVERDUE" if g["deadline"] < date.today().isoformat() else "Pending")
                expiry = " (overdue!)" if status == "OVERDUE" else ""
                lines.append(
                    f"    [{g['type']:7}] {g['description']} "
                    f"- Deadline: {g['deadline']} [{status}]{expiry}"
                )
        return "\n".join(lines)

    @staticmethod
    def activity_timeline(profiles: dict, topics: list, projects: list,
                          goals: list) -> str:
        """Return recent activity (last 10 events) sorted by timestamp descending.

        Events include: profile creation, topic added/updated, project added,
        goal added/completed.
        """
        events: list[tuple[str, str]] = []

        for p in profiles.values():
            events.append((p["created_at"], f"Profile created: {p['name']}"))
        for t in topics:
            events.append((t["created_at"], f"Topic added: {t['name']}"))
            events.append((t["updated_at"], f"Topic updated: {t['name']} -> {t['status']}"))
        for p in projects:
            events.append((p["created_at"], f"Project added: {p['name']}"))
        for g in goals:
            events.append((g["created_at"], f"Goal added: {g['description']}"))
            if g["completed"] and g["completed_at"]:
                events.append((f"{g['completed_at']}T00:00:00",
                              f"Goal completed: {g['description']}"))

        events.sort(key=lambda x: x[0], reverse=True)
        events = events[:10]

        lines = [
            "-" * 50,
            "  ACTIVITY TIMELINE (last 10 events)",
            "-" * 50,
        ]
        if not events:
            lines.append("  (no activity yet)")
        else:
            for ts, desc in events:
                try:
                    dt = datetime.fromisoformat(ts)
                    formatted_ts = dt.strftime("%Y-%m-%d %H:%M")
                except (ValueError, TypeError):
                    formatted_ts = ts
                lines.append(f"  [{formatted_ts}] {desc}")
        return "\n".join(lines)

    @staticmethod
    def export_report(profiles: dict, topics: list, projects: list,
                      goals: list) -> str:
        """Return a complete report suitable for writing to a text file."""
        sections = [
            ProgressReport.overall_summary(profiles, topics, projects, goals),
            "\n" + ProgressReport.topic_report(topics),
            "\n" + ProgressReport.project_report(projects),
            "\n" + ProgressReport.goal_report(goals),
            "\n" + ProgressReport.activity_timeline(profiles, topics, projects, goals),
        ]
        return "\n".join(sections)


# ---------------------------------------------------------------------------
# Main Application
# ---------------------------------------------------------------------------

class AIPrepApp:
    """Console application orchestrator."""

    def __init__(self):
        self.profile_mgr = UserProfileManager()
        self.learning_tracker = LearningTracker()
        self.project_tracker = ProjectTracker()
        self.goal_tracker = GoalTracker()
        self.reporter = ProgressReport()
        self.persistence = DataPersistence()
        self._load_state()

    # ---- State persistence helpers ----------------------------------------

    def _build_state(self) -> dict:
        """Collect all manager data into a single dict for saving."""
        return {
            "profiles": self.profile_mgr.profiles,
            "topics": self.learning_tracker.topics,
            "projects": self.project_tracker.projects,
            "goals": self.goal_tracker.goals,
        }

    def _restore_state(self, data: dict):
        """Restore manager data from a dict."""
        self.profile_mgr.profiles = data.get("profiles", {})
        self.learning_tracker.topics = data.get("topics", [])
        self.project_tracker.projects = data.get("projects", [])
        self.goal_tracker.goals = data.get("goals", [])

    def _load_state(self):
        """Load persisted data on startup."""
        data = self.persistence.load()
        if data:
            self._restore_state(data)

    def _save_state(self):
        """Persist current state to disk."""
        self.persistence.save(self._build_state())

    # ---- Main menu --------------------------------------------------------

    @staticmethod
    def display_menu():
        """Print the main menu."""
        print("\n" + "=" * 50)
        print("  AI ENGINEER PREPARATION CONSOLE")
        print("=" * 50)
        print("1. User Profile Manager")
        print("2. Learning Tracker")
        print("3. Project Tracker")
        print("4. Goal Tracker")
        print("5. Progress Reports")
        print("6. Save & Exit")
        print("=" * 50)

    def run(self):
        """Main application loop."""
        while True:
            self.display_menu()
            choice = input("Select option (1-6): ").strip()
            match choice:
                case "1":
                    self._profile_menu()
                case "2":
                    self._learning_menu()
                case "3":
                    self._project_menu()
                case "4":
                    self._goal_menu()
                case "5":
                    self._report_menu()
                case "6":
                    print("\nSaving data... Goodbye!")
                    self._save_state()
                    break
                case _:
                    print("\nInvalid choice! Please select 1-6.")

    # ---- Profile sub-menu helpers -----------------------------------------

    def _profile_create(self):
        print("\n--- Create Profile ---")
        name = input("Name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return
        email = input("Email: ").strip()
        exp = input("Experience Level (beginner/intermediate/advanced): ").strip()
        interests = input("Interests (comma-separated): ").strip()
        result = self.profile_mgr.create_profile(name, email, exp, interests)
        if result:
            print(f"Profile '{name}' created successfully!")
            self._save_state()

    def _profile_view(self):
        print("\n--- View Profile ---")
        name = input("Name: ").strip()
        profile = self.profile_mgr.get_profile(name)
        if profile:
            print(f"  Name:             {profile['name']}")
            print(f"  Email:            {profile['email']}")
            print(f"  Experience Level: {profile['experience_level']}")
            print(f"  Interests:        {profile['interests']}")
            print(f"  Created:          {profile['created_at']}")
        else:
            print(f"Profile '{name}' not found.")

    def _profile_update(self):
        print("\n--- Update Profile ---")
        name = input("Name: ").strip()
        if not self.profile_mgr.get_profile(name):
            print(f"Profile '{name}' not found.")
            return
        email = input("New Email (leave empty to keep): ").strip()
        exp = input("New Experience Level (leave empty to keep): ").strip()
        interests = input("New Interests (leave empty to keep): ").strip()
        result = self.profile_mgr.update_profile(
            name, email=email, experience_level=exp, interests=interests
        )
        if result:
            print(f"Profile '{name}' updated successfully!")
            self._save_state()

    def _profile_list(self):
        print("\n--- All Profiles ---")
        profiles = self.profile_mgr.list_profiles()
        if not profiles:
            print("  No profiles found.")
            return
        for p in profiles:
            print(f"  - {p['name']} | {p['email']} | {p['experience_level']}")

    def _profile_delete(self):
        print("\n--- Delete Profile ---")
        name = input("Name: ").strip()
        if self.profile_mgr.delete_profile(name):
            print(f"Profile '{name}' deleted.")
            self._save_state()

    def _profile_menu(self):
        """User Profile Manager sub-menu."""
        while True:
            print("\n--- User Profile Manager ---")
            print("1. Create Profile")
            print("2. View Profile")
            print("3. Update Profile")
            print("4. List All Profiles")
            print("5. Delete Profile")
            print("6. Back to Main Menu")
            choice = input("Select option (1-6): ").strip()
            match choice:
                case "1": self._profile_create()
                case "2": self._profile_view()
                case "3": self._profile_update()
                case "4": self._profile_list()
                case "5": self._profile_delete()
                case "6": break
                case _: print("Invalid choice!")

    # ---- Learning sub-menu helpers ----------------------------------------

    def _topic_add(self):
        print("\n--- Add Topic ---")
        name = input("Topic name: ").strip()
        diff = input("Difficulty (beginner/intermediate/advanced): ").strip()
        status = input("Status (not_started/in_progress/completed) [not_started]: ").strip() or "not_started"
        result = self.learning_tracker.add_topic(name, diff, status)
        if result:
            print(f"Topic '{name}' added!")
            self._save_state()

    def _topic_update_status(self):
        print("\n--- Update Topic Status ---")
        name = input("Topic name: ").strip()
        status = input("New status (not_started/in_progress/completed): ").strip()
        if self.learning_tracker.update_status(name, status):
            print(f"Topic '{name}' status updated to '{status}'.")
            self._save_state()

    def _topic_view_grouped(self):
        print("\n--- Topics by Status ---")
        grouped = self.learning_tracker.get_topics_by_status()
        for status, label in [("not_started", "NOT STARTED"),
                              ("in_progress", "IN PROGRESS"),
                              ("completed", "COMPLETED")]:
            items = grouped[status]
            print(f"\n  [{label}] ({len(items)}):")
            if not items:
                print("    (none)")
            for t in items:
                print(f"    - {t['name']} ({t['difficulty']})")

    def _topic_percentage(self):
        pct = self.learning_tracker.completion_percentage()
        total = len(self.learning_tracker.topics)
        completed = sum(1 for t in self.learning_tracker.topics if t["status"] == "completed")
        print(f"\n  Topics: {completed}/{total} completed ({pct}%)")

    def _learning_menu(self):
        """Learning Tracker sub-menu."""
        while True:
            print("\n--- Learning Tracker ---")
            print("1. Add Topic")
            print("2. Update Topic Status")
            print("3. View Topics (by status)")
            print("4. View Completion Percentage")
            print("5. Back to Main Menu")
            choice = input("Select option (1-5): ").strip()
            match choice:
                case "1": self._topic_add()
                case "2": self._topic_update_status()
                case "3": self._topic_view_grouped()
                case "4": self._topic_percentage()
                case "5": break
                case _: print("Invalid choice!")

    # ---- Project sub-menu helpers -----------------------------------------

    def _project_add(self):
        print("\n--- Add Project ---")
        name = input("Project name: ").strip()
        desc = input("Description: ").strip()
        tech = input("Technologies (comma-separated): ").strip()
        status = input("Status (planning/in_progress/completed/on_hold) [planning]: ").strip() or "planning"
        result = self.project_tracker.add_project(name, desc, tech, status)
        if result:
            print(f"Project '{name}' added!")
            self._save_state()

    def _project_update_status(self):
        print("\n--- Update Project Status ---")
        name = input("Project name: ").strip()
        status = input("New status (planning/in_progress/completed/on_hold): ").strip()
        if self.project_tracker.update_status(name, status):
            print(f"Project '{name}' status updated to '{status}'.")
            self._save_state()

    def _project_list(self):
        print("\n--- All Projects ---")
        projects = self.project_tracker.list_projects()
        if not projects:
            print("  No projects found.")
            return
        for p in projects:
            print(f"  - {p['name']} [{p['status']}] | Tech: {p['technologies']}")
            print(f"    {p['description']}")

    def _project_filter(self):
        print("\n--- Filter Projects ---")
        print("1. Filter by Status")
        print("2. Filter by Technology")
        print("3. Both")
        fchoice = input("Select: ").strip()
        status = None
        technology = None
        match fchoice:
            case "1":
                status = input("Status: ").strip().lower()
            case "2":
                technology = input("Technology: ").strip()
            case "3":
                status = input("Status: ").strip().lower()
                technology = input("Technology: ").strip()
            case _:
                print("Invalid choice.")
                return
        projects = self.project_tracker.list_projects(status=status, technology=technology)
        if not projects:
            print("  No matching projects found.")
            return
        print(f"\n  Found {len(projects)} project(s):")
        for p in projects:
            print(f"  - {p['name']} [{p['status']}] | Tech: {p['technologies']}")

    def _project_menu(self):
        """Project Tracker sub-menu."""
        while True:
            print("\n--- Project Tracker ---")
            print("1. Add Project")
            print("2. Update Project Status")
            print("3. List All Projects")
            print("4. Filter Projects")
            print("5. Back to Main Menu")
            choice = input("Select option (1-5): ").strip()
            match choice:
                case "1": self._project_add()
                case "2": self._project_update_status()
                case "3": self._project_list()
                case "4": self._project_filter()
                case "5": break
                case _: print("Invalid choice!")

    # ---- Goal sub-menu helpers --------------------------------------------

    def _goal_add(self):
        print("\n--- Add Goal ---")
        desc = input("Description: ").strip()
        gtype = input("Type (daily/weekly/monthly): ").strip().lower()
        deadline = input("Deadline (YYYY-MM-DD, optional): ").strip() or None
        result = self.goal_tracker.add_goal(desc, gtype, deadline)
        if result:
            print(f"Goal '{desc}' added!")
            self._save_state()

    def _goal_complete(self):
        print("\n--- Mark Goal Completed ---")
        desc = input("Goal description: ").strip()
        if self.goal_tracker.mark_completed(desc):
            print(f"Goal '{desc}' marked as completed!")
            self._save_state()

    def _goal_current(self):
        print("\n--- Current (Incomplete) Goals ---")
        goals = self.goal_tracker.get_current_goals()
        if not goals:
            print("  No incomplete goals. Well done!")
            return
        for g in goals:
            overdue = " (OVERDUE!)" if g["deadline"] < date.today().isoformat() else ""
            print(f"  - {g['description']} [{g['type']}] Deadline: {g['deadline']}{overdue}")

    def _goal_overdue(self):
        print("\n--- Overdue Goals ---")
        goals = self.goal_tracker.get_overdue_goals()
        if not goals:
            print("  No overdue goals. Great job!")
            return
        for g in goals:
            print(f"  - {g['description']} [{g['type']}] Deadline was: {g['deadline']}")

    def _goal_streak(self):
        streak = self.goal_tracker.get_streak()
        print(f"\n  Current goal streak: {streak} day(s)")

    def _goal_menu(self):
        """Goal Tracker sub-menu."""
        while True:
            print("\n--- Goal Tracker ---")
            print("1. Add Goal")
            print("2. Mark Goal Completed")
            print("3. View Current Goals")
            print("4. View Overdue Goals")
            print("5. View Goal Streak")
            print("6. Back to Main Menu")
            choice = input("Select option (1-6): ").strip()
            match choice:
                case "1": self._goal_add()
                case "2": self._goal_complete()
                case "3": self._goal_current()
                case "4": self._goal_overdue()
                case "5": self._goal_streak()
                case "6": break
                case _: print("Invalid choice!")

    # ---- Report sub-menu helpers ------------------------------------------

    def _report_export(self):
        print("\n--- Export Report ---")
        filename = input("Filename (default: progress_report.txt): ").strip() or "progress_report.txt"
        report = self.reporter.export_report(
            self.profile_mgr.profiles,
            self.learning_tracker.topics,
            self.project_tracker.projects,
            self.goal_tracker.goals,
        )
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"Report exported to '{filename}'.")
        except IOError as e:
            print(f"Error writing file: {e}")

    def _report_menu(self):
        """Progress Reports sub-menu."""
        while True:
            print("\n--- Progress Reports ---")
            print("1. Overall Summary")
            print("2. Topic Report")
            print("3. Project Report")
            print("4. Goal Report")
            print("5. Activity Timeline")
            print("6. Export Full Report to File")
            print("7. Back to Main Menu")
            choice = input("Select option (1-7): ").strip()
            profiles = self.profile_mgr.profiles
            topics = self.learning_tracker.topics
            projects = self.project_tracker.projects
            goals = self.goal_tracker.goals
            match choice:
                case "1":
                    print(self.reporter.overall_summary(profiles, topics, projects, goals))
                case "2":
                    print(self.reporter.topic_report(topics))
                case "3":
                    print(self.reporter.project_report(projects))
                case "4":
                    print(self.reporter.goal_report(goals))
                case "5":
                    print(self.reporter.activity_timeline(profiles, topics, projects, goals))
                case "6":
                    self._report_export()
                case "7":
                    break
                case _:
                    print("Invalid choice!")


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app = AIPrepApp()
    app.run()
