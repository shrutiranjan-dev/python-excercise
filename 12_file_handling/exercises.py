"""
Module 12: File Handling - Exercises
35 exercises total: Easy(10), Medium(10), Hard(10), Expert(5)
Solutions at the bottom.
"""

import json
import csv
import os
from pathlib import Path


# ============================================================
# EASY (1-10)
# ============================================================

# 1. Write "Hello World" to a file named "hello.txt"
def exercise_1():
    pass  # Your code here


# 2. Read the contents of "hello.txt" and print them
def exercise_2():
    pass


# 3. Append "Line 2" to a file named "lines.txt"
def exercise_3():
    pass


# 4. Read the first line of "lines.txt"
def exercise_4():
    pass


# 5. Count the number of lines in "data.txt" (create it first with 3 lines)
def exercise_5():
    pass


# 6. Write a list of strings to a file using writelines
def exercise_6():
    fruits = ["apple\n", "banana\n", "cherry\n"]
    pass


# 7. Check if "hello.txt" exists before opening it
def exercise_7():
    pass


# 8. Read an entire file and print each line with its line number
def exercise_8():
    pass


# 9. Write a JSON string {"name": "Student"} to a file
def exercise_9():
    pass


# 10. Create a file only if it doesn't exist (use 'x' mode)
def exercise_10():
    pass


# ============================================================
# MEDIUM (11-20)
# ============================================================

# 11. Read a JSON file and print all keys
def exercise_11():
    pass


# 12. Append 5 lines from a list to a file, one at a time
def exercise_12():
    lines = ["Line A", "Line B", "Line C", "Line D", "Line E"]
    pass


# 13. Read a CSV file and calculate the average of a numeric column
def exercise_13():
    pass


# 14. Copy contents of one file to another
def exercise_14():
    pass


# 15. Write a list of dicts to a CSV file with headers
def exercise_15():
    students = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
    ]
    pass


# 16. Find and replace a word in a file
def exercise_16():
    pass


# 17. Read a file in reverse order (lines reversed)
def exercise_17():
    pass


# 18. Count word frequency in a text file
def exercise_18():
    pass


# 19. Merge two CSV files with the same columns
def exercise_19():
    pass


# 20. Use pathlib to list all .txt files in a directory
def exercise_20():
    pass


# ============================================================
# HARD (21-30)
# ============================================================

# 21. Create a logging decorator that writes function calls to a log file
def exercise_21():
    pass


# 22. Split a large file into multiple smaller files of N lines each
def exercise_22():
    pass


# 23. Validate JSON files in a directory (report which are valid/invalid)
def exercise_23():
    pass


# 24. Create a simple key-value store backed by a JSON file
def exercise_24():
    pass


# 25. Parse a log file and extract all ERROR-level messages with timestamps
def exercise_25():
    pass


# 26. Convert a CSV file to JSON format
def exercise_26():
    pass


# 27. Watch a file for changes (check modification time periodically)
def exercise_27():
    pass


# 28. Implement a simple CSV query: filter rows where column value matches
def exercise_28():
    pass


# 29. Create a file-based queue (append jobs, pop from top)
def exercise_29():
    pass


# 30. Read a binary file and print its first N bytes as hex
def exercise_30():
    pass


# ============================================================
# EXPERT (31-35)
# ============================================================

# 31. Build a minimal JSON database with CRUD operations backed by file
def exercise_31():
    pass


# 32. Implement incremental file backup (only copy changed files)
def exercise_32():
    pass


# 33. Create a CSV validator that checks types, required columns, ranges
def exercise_33():
    pass


# 34. Build a file-based configuration system with env variable override
def exercise_34():
    pass


# 35. Implement a streaming log parser that processes a file line by line
#     and aggregates stats (counts by level, top errors, timeline)
def exercise_35():
    pass


# ============================================================
# SOLUTIONS
# ============================================================

def solution_1():
    with open("hello.txt", "w") as f:
        f.write("Hello World")


def solution_2():
    with open("hello.txt", "r") as f:
        print(f.read())


def solution_3():
    with open("lines.txt", "w") as f:
        f.write("Line 1\n")
    with open("lines.txt", "a") as f:
        f.write("Line 2\n")


def solution_4():
    with open("lines.txt", "r") as f:
        print(f.readline())


def solution_5():
    with open("data.txt", "w") as f:
        f.writelines(["a\n", "b\n", "c\n"])
    with open("data.txt", "r") as f:
        count = sum(1 for _ in f)
    print(count)


def solution_6():
    fruits = ["apple\n", "banana\n", "cherry\n"]
    with open("fruits.txt", "w") as f:
        f.writelines(fruits)


def solution_7():
    import os
    if os.path.exists("hello.txt"):
        with open("hello.txt") as f:
            print(f.read())
    else:
        print("File not found")


def solution_8():
    with open("data.txt", "r") as f:
        for i, line in enumerate(f, 1):
            print(f"{i}: {line.strip()}")


def solution_9():
    import json
    with open("student.json", "w") as f:
        json.dump({"name": "Student"}, f)


def solution_10():
    try:
        with open("new_unique.txt", "x") as f:
            f.write("created")
    except FileExistsError:
        print("File already exists")


def solution_11():
    with open("config.json", "r") as f:
        data = json.load(f)
    for key in data:
        print(key)


def solution_12():
    lines = ["Line A", "Line B", "Line C", "Line D", "Line E"]
    with open("output.txt", "w") as f:
        for line in lines:
            f.write(line + "\n")


def solution_13():
    total = 0
    count = 0
    with open("scores.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += int(row["score"])
            count += 1
    print(f"Average: {total / count}")


def solution_14():
    with open("source.txt", "r") as src, open("dest.txt", "w") as dst:
        dst.write(src.read())


def solution_15():
    students = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
    ]
    with open("students.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "grade"])
        writer.writeheader()
        writer.writerows(students)


def solution_16():
    with open("article.txt", "r") as f:
        content = f.read()
    content = content.replace("old_word", "new_word")
    with open("article.txt", "w") as f:
        f.write(content)


def solution_17():
    with open("data.txt", "r") as f:
        lines = f.readlines()
    for line in reversed(lines):
        print(line.strip())


def solution_18():
    from collections import Counter
    with open("text.txt", "r") as f:
        words = f.read().split()
    freq = Counter(words)
    for word, count in freq.most_common(10):
        print(f"{word}: {count}")


def solution_19():
    all_rows = []
    for fname in ["file1.csv", "file2.csv"]:
        with open(fname, "r") as f:
            reader = csv.DictReader(f)
            all_rows.extend(list(reader))
    with open("merged.csv", "w", newline="") as f:
        if all_rows:
            writer = csv.DictWriter(f, fieldnames=all_rows[0].keys())
            writer.writeheader()
            writer.writerows(all_rows)


def solution_20():
    from pathlib import Path
    for p in Path(".").glob("*.txt"):
        print(p)


def solution_21():
    def log_calls(func):
        def wrapper(*args, **kwargs):
            with open("calls.log", "a") as f:
                f.write(f"Called {func.__name__}\n")
            return func(*args, **kwargs)
        return wrapper


def solution_22():
    def split_file(filename, lines_per_file=100):
        with open(filename, "r") as f:
            for i, line in enumerate(f):
                if i % lines_per_file == 0:
                    out = open(f"{filename}.part{i//lines_per_file}", "w")
                out.write(line)
            out.close()


def solution_23():
    from pathlib import Path
    import json
    for p in Path(".").glob("*.json"):
        try:
            with open(p) as f:
                json.load(f)
            print(f"{p}: VALID")
        except json.JSONDecodeError as e:
            print(f"{p}: INVALID - {e}")


def solution_24():
    class JSONKVStore:
        def __init__(self, path="store.json"):
            self.path = path
            if not Path(path).exists():
                with open(path, "w") as f:
                    json.dump({}, f)

        def get(self, key):
            with open(self.path, "r") as f:
                data = json.load(f)
            return data.get(key)

        def set(self, key, value):
            with open(self.path, "r") as f:
                data = json.load(f)
            data[key] = value
            with open(self.path, "w") as f:
                json.dump(data, f, indent=2)


def solution_25():
    import re
    pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*ERROR:(.*)")
    with open("app.log", "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                print(f"[{match.group(1)}] {match.group(2).strip()}")


def solution_26():
    with open("input.csv", "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open("output.json", "w") as f:
        json.dump(data, f, indent=2)


def solution_27():
    import time
    path = Path("watch.txt")
    last_mtime = path.stat().st_mtime if path.exists() else 0
    while True:
        if path.exists() and path.stat().st_mtime != last_mtime:
            last_mtime = path.stat().st_mtime
            print("File changed!")
            print(path.read_text())
        time.sleep(1)


def solution_28():
    def query_csv(filename, column, value):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            return [row for row in reader if row[column] == value]


def solution_29():
    class FileQueue:
        def __init__(self, path="queue.txt"):
            self.path = path

        def enqueue(self, item):
            with open(self.path, "a") as f:
                f.write(item + "\n")

        def dequeue(self):
            with open(self.path, "r") as f:
                lines = f.readlines()
            if not lines:
                return None
            first = lines[0].strip()
            with open(self.path, "w") as f:
                f.writelines(lines[1:])
            return first


def solution_30():
    n = 16
    with open("file.bin", "rb") as f:
        data = f.read(n)
    print(data.hex(" "))


def solution_31():
    class JSONDatabase:
        def __init__(self, path="db.json"):
            self.path = path
            if not Path(path).exists():
                with open(path, "w") as f:
                    json.dump({}, f)

        def create(self, key, value):
            data = self._read()
            if key in data:
                raise KeyError(f"Key '{key}' exists")
            data[key] = value
            self._write(data)

        def read(self, key):
            return self._read().get(key)

        def update(self, key, value):
            data = self._read()
            data[key] = value
            self._write(data)

        def delete(self, key):
            data = self._read()
            del data[key]
            self._write(data)

        def all(self):
            return self._read()

        def _read(self):
            with open(self.path, "r") as f:
                return json.load(f)

        def _write(self, data):
            with open(self.path, "w") as f:
                json.dump(data, f, indent=2)


def solution_32():
    import hashlib
    from pathlib import Path

    def incremental_backup(src_dir, backup_dir):
        src = Path(src_dir)
        dst = Path(backup_dir)
        dst.mkdir(exist_ok=True)

        for f in src.rglob("*"):
            if f.is_file():
                rel = f.relative_to(src)
                backup_file = dst / rel
                backup_file.parent.mkdir(parents=True, exist_ok=True)

                if backup_file.exists():
                    src_hash = hashlib.md5(f.read_bytes()).hexdigest()
                    dst_hash = hashlib.md5(backup_file.read_bytes()).hexdigest()
                    if src_hash == dst_hash:
                        continue

                backup_file.write_bytes(f.read_bytes())
                print(f"Backed up: {rel}")


def solution_33():
    class CSVValidator:
        def __init__(self, schema):
            self.schema = schema  # {col: {"type": int, "required": True, "min": 0, "max": 100}}

        def validate(self, filename):
            errors = []
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                for i, row in enumerate(reader, 2):
                    for col, rules in self.schema.items():
                        val = row.get(col, "").strip()
                        if rules.get("required") and not val:
                            errors.append(f"Row {i}: '{col}' is required")
                            continue
                        if not val and not rules.get("required"):
                            continue
                        try:
                            if rules.get("type") == int:
                                val = int(val)
                            elif rules.get("type") == float:
                                val = float(val)
                        except ValueError:
                            errors.append(f"Row {i}: '{col}' invalid type")
                            continue
                        if "min" in rules and val < rules["min"]:
                            errors.append(f"Row {i}: '{col}' below minimum {rules['min']}")
                        if "max" in rules and val > rules["max"]:
                            errors.append(f"Row {i}: '{col}' above maximum {rules['max']}")
            return errors


def solution_34():
    import os
    import json
    from pathlib import Path

    class Config:
        def __init__(self, path="config.json"):
            self.path = Path(path)
            self._data = {}
            if self.path.exists():
                with open(self.path) as f:
                    self._data = json.load(f)

        def get(self, key, default=None):
            env_val = os.environ.get(key.upper())
            if env_val is not None:
                return env_val
            keys = key.split(".")
            val = self._data
            for k in keys:
                if isinstance(val, dict):
                    val = val.get(k)
                else:
                    return default
            return val if val is not None else default


def solution_35():
    import re
    from collections import Counter, defaultdict
    from datetime import datetime

    class LogStreamProcessor:
        def __init__(self):
            self.level_counts = Counter()
            self.error_by_hour = defaultdict(list)
            self.top_errors = Counter()

        def process_file(self, filename):
            pattern = re.compile(
                r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(.*)"
            )
            with open(filename, "r") as f:
                for line in f:
                    match = pattern.match(line)
                    if not match:
                        continue
                    timestamp, level, message = match.groups()
                    self.level_counts[level] += 1
                    if level in ("ERROR", "CRITICAL"):
                        hour = timestamp[:13]
                        self.error_by_hour[hour].append(message)
                        words = message.split()
                        for w in words:
                            if w.isidentifier() and len(w) > 3:
                                self.top_errors[w] += 1

        def report(self):
            print("=== Log Summary ===")
            for level, count in self.level_counts.most_common():
                print(f"  {level}: {count}")
            print("\n=== Errors by Hour ===")
            for hour in sorted(self.error_by_hour):
                print(f"  {hour}: {len(self.error_by_hour[hour])} errors")
            print("\n=== Top Error Keywords ===")
            for word, count in self.top_errors.most_common(10):
                print(f"  {word}: {count}")
