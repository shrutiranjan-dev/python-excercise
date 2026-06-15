"""
Module 12: File Handling - Examples
Level 0-5 progressing from basic to production-ready.
"""

import json
import csv
import os
from datetime import datetime
from pathlib import Path

# ============================================================
# LEVEL 0: Basic File Writing and Reading
# ============================================================

def level_0_basic_file_io():
    print("=== LEVEL 0: Basic File I/O ===")

    # Writing to a file
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write("Hello, File!\n")
        f.write("This is line 2.\n")
        f.write("Line 3 here.\n")

    # Reading the entire file
    with open("sample.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print("Full content:")
    print(content)

    # Appending to a file
    with open("sample.txt", "a", encoding="utf-8") as f:
        f.write("Appended line.\n")

    # Reading again to see the append
    with open("sample.txt", "r") as f:
        print(f.read())

    # Clean up
    Path("sample.txt").unlink(missing_ok=True)


# ============================================================
# LEVEL 1: Reading Line by Line with Context Manager
# ============================================================

def level_1_line_by_line():
    print("\n=== LEVEL 1: Line by Line Reading ===")

    lines = ["First line\n", "Second line\n", "Third line\n"]

    with open("lines.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)

    # Read line by line (memory efficient for large files)
    print("Reading line by line:")
    with open("lines.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(f"  -> {line.strip()}")

    # Using readline()
    print("\nUsing readline():")
    with open("lines.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(f"  -> {line.strip()}")

    # Using readlines() (all lines at once - small files only)
    print("\nUsing readlines():")
    with open("lines.txt", "r") as f:
        all_lines = f.readlines()
    for i, line in enumerate(all_lines, 1):
        print(f"  Line {i}: {line.strip()}")

    Path("lines.txt").unlink(missing_ok=True)


# ============================================================
# LEVEL 2: Working with JSON Files
# ============================================================

def level_2_json_files():
    print("\n=== LEVEL 2: JSON Files ===")

    data = {
        "name": "AI Assistant",
        "version": "2.1.0",
        "capabilities": ["chat", "code", "translate"],
        "settings": {
            "temperature": 0.7,
            "max_tokens": 2048,
            "stream": True
        },
        "active": True
    }

    # Write JSON to file
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("JSON written to config.json")

    # Read JSON from file
    with open("config.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print(f"Loaded: {loaded['name']} v{loaded['version']}")
    print(f"Capabilities: {', '.join(loaded['capabilities'])}")

    # json.loads / json.dumps (string operations)
    json_string = '{"prompt": "Hello", "role": "user"}'
    parsed = json.loads(json_string)
    print(f"Parsed string: {parsed['role']} said '{parsed['prompt']}'")

    back_to_string = json.dumps(parsed)
    print(f"Back to string: {back_to_string}")

    # Error handling for JSON
    bad_json = "{invalid: true}"
    try:
        json.loads(bad_json)
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")

    Path("config.json").unlink(missing_ok=True)


# ============================================================
# LEVEL 3: Real World - LLM Conversation Logger
# ============================================================

class LLMConversationLogger:
    """Logs LLM conversations with timestamps to a JSON file."""

    def __init__(self, log_file="conversations.json"):
        self.log_file = Path(log_file)
        self.conversations = []
        self._load_existing()

    def _load_existing(self):
        if self.log_file.exists():
            with open(self.log_file, "r", encoding="utf-8") as f:
                self.conversations = json.load(f)

    def log_message(self, role, content, model="gpt-4", tokens=0):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "role": role,
            "content": content,
            "model": model,
            "tokens": tokens
        }
        self.conversations.append(entry)
        self._save()

    def _save(self):
        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(self.conversations, f, indent=2)

    def get_recent(self, n=5):
        return self.conversations[-n:]

    def total_tokens_used(self):
        return sum(c["tokens"] for c in self.conversations)

    def export_formatted(self, output_file="chat_log.txt"):
        with open(output_file, "w", encoding="utf-8") as f:
            for c in self.conversations:
                timestamp = c["timestamp"][:19]
                f.write(f"[{timestamp}] {c['role'].upper()}: {c['content']}\n")


def level_3_llm_logger():
    print("\n=== LEVEL 3: LLM Conversation Logger ===")

    logger = LLMConversationLogger("chat_history.json")

    logger.log_message("user", "What is Python?", tokens=5)
    logger.log_message("assistant", "Python is a programming language.", model="gpt-4", tokens=8)
    logger.log_message("user", "Show me file handling.", tokens=4)
    logger.log_message("assistant", "Use open() and context managers.", model="gpt-4", tokens=7)

    print(f"Total conversations: {len(logger.conversations)}")
    print(f"Total tokens used: {logger.total_tokens_used()}")

    print("\nRecent messages:")
    for msg in logger.get_recent(2):
        print(f"  [{msg['role']}] {msg['content'][:50]}...")

    logger.export_formatted("chat_log.txt")
    with open("chat_log.txt", "r") as f:
        print("\nExported chat log:")
        print(f.read())

    Path("chat_history.json").unlink(missing_ok=True)
    Path("chat_log.txt").unlink(missing_ok=True)


# ============================================================
# LEVEL 4: Mini Challenge - CSV Dataset Analyzer
# ============================================================

def level_4_csv_analyzer():
    print("\n=== LEVEL 4: CSV Dataset Analyzer ===")

    # Create sample CSV
    sample_data = [
        ["name", "age", "city", "salary"],
        ["Alice", "30", "NYC", "75000"],
        ["Bob", "25", "SF", "82000"],
        ["Charlie", "35", "NYC", "95000"],
        ["Diana", "28", "Chicago", "68000"],
        ["Eve", "32", "SF", "91000"],
        ["Frank", "40", "NYC", "105000"],
    ]

    with open("employees.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)

    # Analyze with DictReader
    records = []
    with open("employees.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["age"] = int(row["age"])
            row["salary"] = int(row["salary"])
            records.append(row)

    print(f"Total employees: {len(records)}")

    # Stats by city
    city_stats = {}
    for r in records:
        city = r["city"]
        if city not in city_stats:
            city_stats[city] = {"count": 0, "total_salary": 0}
        city_stats[city]["count"] += 1
        city_stats[city]["total_salary"] += r["salary"]

    print("\nSalary stats by city:")
    for city, stats in city_stats.items():
        avg = stats["total_salary"] / stats["count"]
        print(f"  {city}: {stats['count']} employees, avg salary ${avg:,.0f}")

    # Write analysis to CSV
    with open("city_analysis.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["city", "employee_count", "avg_salary"])
        for city, stats in city_stats.items():
            avg = stats["total_salary"] / stats["count"]
            writer.writerow([city, stats["count"], round(avg, 2)])

    print("\nAnalysis written to city_analysis.csv")

    Path("employees.csv").unlink(missing_ok=True)
    Path("city_analysis.csv").unlink(missing_ok=True)


# ============================================================
# LEVEL 5: Production - Multi-Format Data Exporter
# ============================================================

class DataExporter:
    """Export data to multiple formats with validation and error handling."""

    def __init__(self, data, output_dir="exports"):
        self.data = data
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def _validate(self):
        if not self.data:
            raise ValueError("No data to export")
        if not isinstance(self.data, list):
            raise TypeError("Data must be a list of dictionaries")
        if not all(isinstance(row, dict) for row in self.data):
            raise TypeError("Each row must be a dictionary")

    def to_json(self, filename="export.json", indent=2):
        self._validate()
        filepath = self.output_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=indent, default=str)
        print(f"JSON exported: {filepath}")
        return filepath

    def to_csv(self, filename="export.csv"):
        self._validate()
        filepath = self.output_dir / filename
        if not self.data:
            raise ValueError("No data to export")
        fieldnames = list(self.data[0].keys())
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)
        print(f"CSV exported: {filepath}")
        return filepath

    def to_txt(self, filename="export.txt", template=None):
        self._validate()
        if template is None:
            template = "{id}. {name} - {description}"
        filepath = self.output_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            for item in self.data:
                try:
                    line = template.format(**item)
                except KeyError as e:
                    line = f"Missing key {e} for item {item.get('id', '?')}"
                f.write(line + "\n")
        print(f"TXT exported: {filepath}")
        return filepath

    def export_all(self):
        base = "data_export"
        return {
            "json": self.to_json(f"{base}.json"),
            "csv": self.to_csv(f"{base}.csv"),
            "txt": self.to_txt(f"{base}.txt"),
        }

    def cleanup(self):
        import shutil
        shutil.rmtree(self.output_dir, ignore_errors=True)


def level_5_data_exporter():
    print("\n=== LEVEL 5: Multi-Format Data Exporter ===")

    items = [
        {"id": 1, "name": "Python Basics", "description": "Variables, loops, functions", "difficulty": "easy"},
        {"id": 2, "name": "File Handling", "description": "Read/write files, JSON, CSV", "difficulty": "medium"},
        {"id": 3, "name": "OOP", "description": "Classes, inheritance, polymorphism", "difficulty": "hard"},
    ]

    exporter = DataExporter(items, output_dir="exports_demo")

    try:
        results = exporter.export_all()
        print(f"\nExported {len(results)} files successfully")

        # Read back and verify
        for fmt, path in results.items():
            print(f"  Verified: {fmt} -> {path.name}")

    except (ValueError, TypeError, OSError) as e:
        print(f"Export failed: {e}")
    finally:
        exporter.cleanup()
        print("Cleanup complete")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    level_0_basic_file_io()
    level_1_line_by_line()
    level_2_json_files()
    level_3_llm_logger()
    level_4_csv_analyzer()
    level_5_data_exporter()
