"""AI Engineer Preparation Console App — Capstone Project Starter Code.

Fill in every # TODO block to complete the application.
Type hints and docstrings are provided; implement the logic below each one.
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

# Valid status values for topics and projects
TOPIC_STATUSES = ("not_started", "in_progress", "completed")
PROJECT_STATUSES = ("planning", "in_progress", "completed", "on_hold")
GOAL_TYPES = ("daily", "weekly", "monthly")


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
        # TODO: Implement save with backup
        # 1. If DATA_FILE exists, copy it to BACKUP_FILE (use shutil.copy2)
        # 2. Write data to DATA_FILE with json.dump (indent=2)
        # 3. Handle (catch) IOError and print an error message
        # 4. Return True on success, False on failure
        return True

    @staticmethod
    def load() -> dict:
        """Load data from the JSON file.

        Returns:
            The data dict if loading succeeded, otherwise an empty dict.
        """
        # TODO: Implement load
        # 1. Try to open DATA_FILE for reading
        # 2. Parse JSON with json.load
        # 3. Catch FileNotFoundError — return {}
        # 4. Catch json.JSONDecodeError — print warning, return {}
        # 5. Catch IOError — print warning, return {}
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
            experience_level: e.g. "beginner", "intermediate", "advanced".
            interests: Comma-separated interests.

        Returns:
            The created profile dict on success, or None if name is empty
            or a profile with that name already exists.
        """
        # TODO: Implement
        # 1. Validate name is non-empty
        # 2. Check name not already in self.profiles
        # 3. Create profile dict with all fields + created_at timestamp
        # 4. Store in self.profiles[name]
        # 5. Return the profile dict
        return None

    def get_profile(self, name: str) -> Optional[dict]:
        """Retrieve a profile by name.

        Returns:
            The profile dict if found, or None.
        """
        # TODO: Implement
        return None

    def update_profile(self, name: str, **kwargs) -> Optional[dict]:
        """Update fields on an existing profile.

        Accepted kwargs: email, experience_level, interests.
        Empty string values are ignored (field not updated).

        Returns:
            The updated profile dict, or None if profile not found.
        """
        # TODO: Implement
        return None

    def list_profiles(self) -> list[dict]:
        """Return all profiles as a list."""
        # TODO: Implement
        return []

    def delete_profile(self, name: str) -> bool:
        """Delete a profile by name.

        Returns:
            True if deleted, False if not found.
        """
        # TODO: Implement
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
            difficulty: "beginner", "intermediate", or "advanced".
            status: One of TOPIC_STATUSES.

        Returns:
            The created topic dict on success, or None if validation fails.
        """
        # TODO: Implement
        # 1. Validate name non-empty
        # 2. Validate difficulty in ("beginner", "intermediate", "advanced")
        # 3. Validate status in TOPIC_STATUSES
        # 4. Create topic dict with name, difficulty, status, created_at, updated_at
        # 5. Append to self.topics
        # 6. Return the topic dict
        return None

    def update_status(self, name: str, new_status: str) -> bool:
        """Change the status of a topic.

        Returns:
            True if updated, False if topic not found or invalid status.
        """
        # TODO: Implement
        return False

    def get_topics_by_status(self) -> dict[str, list[dict]]:
        """Group topics by their status.

        Returns:
            Dict like {"not_started": [...], "in_progress": [...], "completed": [...]}
        """
        # TODO: Implement
        return {"not_started": [], "in_progress": [], "completed": []}

    def completion_percentage(self) -> float:
        """Calculate the percentage of completed topics.

        Returns:
            Float 0.0–100.0. Returns 0.0 if there are no topics.
        """
        # TODO: Implement (guard against empty list)
        return 0.0

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
        # TODO: Implement
        return None

    def update_status(self, name: str, new_status: str) -> bool:
        """Update the status of a project.

        Returns:
            True if updated, False if not found or invalid status.
        """
        # TODO: Implement
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
        # TODO: Implement
        return []


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
            goal_type: "daily", "weekly", or "monthly".
            deadline: Optional date string in YYYY-MM-DD format.
                      If not provided, defaults to a sensible value:
                      daily → tomorrow, weekly → 7 days from now,
                      monthly → 30 days from now.

        Returns:
            The created goal dict, or None on validation failure.
        """
        # TODO: Implement
        return None

    def mark_completed(self, description: str) -> bool:
        """Mark a goal as completed.

        Sets both 'completed' to True and 'completed_at' to the current ISO date.

        Returns:
            True if found and updated, False otherwise.
        """
        # TODO: Implement
        return False

    def get_current_goals(self) -> list[dict]:
        """Return all goals that are not yet completed, sorted by deadline ascending."""
        # TODO: Implement
        return []

    def get_streak(self) -> int:
        """Calculate the current goal streak.

        A streak is the number of consecutive days (up to today) on which
        AT LEAST ONE goal was completed.

        Returns:
            Integer streak count.
        """
        # TODO: Implement
        # Hint: collect completed_at dates, remove duplicates, sort descending,
        # count consecutive days from today backwards
        return 0

    def get_overdue_goals(self) -> list[dict]:
        """Return incomplete goals whose deadline is before today."""
        # TODO: Implement
        return []


# ---------------------------------------------------------------------------
# Progress Reports
# ---------------------------------------------------------------------------

class ProgressReport:
    """Generate formatted progress reports from all data sources."""

    @staticmethod
    def overall_summary(profiles: dict, topics: list, projects: list,
                        goals: list) -> str:
        """Return a multi-line string summarising overall progress."""
        # TODO: Implement
        lines = [
            "=" * 50,
            "  OVERALL PROGRESS SUMMARY",
            "=" * 50,
        ]
        # Add sections for profiles, topics, projects, goals
        return "\n".join(lines)

    @staticmethod
    def topic_report(topics: list) -> str:
        """Return a formatted report of topics grouped by status.

        Includes completion percentage.
        """
        # TODO: Implement
        return ""

    @staticmethod
    def project_report(projects: list) -> str:
        """Return a formatted report of projects grouped by status."""
        # TODO: Implement
        return ""

    @staticmethod
    def goal_report(goals: list) -> str:
        """Return a formatted report of goals with completion rate and streak."""
        # TODO: Implement
        return ""

    @staticmethod
    def activity_timeline(profiles: dict, topics: list, projects: list,
                          goals: list) -> str:
        """Return recent activity (last 10 events) sorted by timestamp descending.

        Events include: profile creation, topic added/updated, project added,
        goal added/completed.
        """
        # TODO: Implement
        return ""

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
        # Convert string timestamps back to date objects where needed
        # (goal completed_at and deadline are stored as strings for JSON)

    def _load_state(self):
        """Load persisted data on startup."""
        data = self.persistence.load()
        if data:
            self._restore_state(data)

    def _save_state(self):
        """Persist current state to disk."""
        self.persistence.save(self._build_state())

    # ---- Main menu --------------------------------------------------------

    def display_menu(self):
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

    # ---- Sub-menus --------------------------------------------------------

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
                case "1":
                    # TODO: Get inputs, call profile_mgr.create_profile(...)
                    # Validate and print success/error
                    pass
                case "2":
                    # TODO: Get name, call profile_mgr.get_profile(name)
                    pass
                case "3":
                    # TODO: Get name, then get optional fields, call update_profile
                    pass
                case "4":
                    # TODO: List all profiles
                    pass
                case "5":
                    # TODO: Get name, delete profile
                    pass
                case "6":
                    break
                case _:
                    print("Invalid choice!")

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
                case "1":
                    pass  # TODO: Implement
                case "2":
                    pass  # TODO: Implement
                case "3":
                    # TODO: Display topics grouped by status
                    pass
                case "4":
                    # TODO: Show completion percentage
                    pass
                case "5":
                    break
                case _:
                    print("Invalid choice!")

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
                case "1":
                    pass  # TODO: Implement
                case "2":
                    pass  # TODO: Implement
                case "3":
                    # TODO: Display all projects
                    pass
                case "4":
                    # TODO: Filter by status or technology
                    pass
                case "5":
                    break
                case _:
                    print("Invalid choice!")

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
                case "1":
                    pass  # TODO: Implement
                case "2":
                    pass  # TODO: Implement
                case "3":
                    pass  # TODO: Implement
                case "4":
                    pass  # TODO: Implement
                case "5":
                    pass  # TODO: Implement
                case "6":
                    break
                case _:
                    print("Invalid choice!")

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
                    # TODO: Get filename, write export, handle errors
                    pass
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
