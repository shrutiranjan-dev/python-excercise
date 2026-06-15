"""
Module 12: File Handling - Fill in the Blanks
Fill in the _____ with the correct code. Answers at the bottom.
"""

# ============================================================
# Question 1
# ============================================================
# Open a file for reading
with _____("data.txt", "r") as f:
    content = f.read()

# ============================================================
# Question 2
# ============================================================
# Write to a file (creates or truncates)
with open("out.txt", _____) as f:
    f.write("Hello")

# ============================================================
# Question 3
# ============================================================
# Append to an existing file
with open("log.txt", _____) as f:
    f.write("New entry\n")

# ============================================================
# Question 4
# ============================================================
# Read entire file content
with open("file.txt") as f:
    content = f._____()

# ============================================================
# Question 5
# ============================================================
# Read one line
with open("file.txt") as f:
    line = f._____()

# ============================================================
# Question 6
# ============================================================
# Read all lines into a list
with open("file.txt") as f:
    lines = f._____()

# ============================================================
# Question 7
# ============================================================
# Write multiple lines at once
with open("file.txt", "w") as f:
    f._____(["line1\n", "line2\n"])

# ============================================================
# Question 8
# ============================================================
# Parse JSON string to dict
import json
data = json._____('{"key": "value"}')

# ============================================================
# Question 9
# ============================================================
# Read JSON from file
with open("data.json") as f:
    data = json._____(f)

# ============================================================
# Question 10
# ============================================================
# Write dict to file as JSON
with open("data.json", "w") as f:
    json._____(data, f, indent=2)

# ============================================================
# Question 11
# ============================================================
# Convert dict to JSON string
s = json._____(data, indent=2)

# ============================================================
# Question 12
# ============================================================
# Read CSV file as dictionaries
import csv
with open("data.csv") as f:
    reader = csv._____(f)
    for row in reader:
        print(row["name"])

# ============================================================
# Question 13
# ============================================================
# Write CSV with header
with open("out.csv", "w", newline="") as f:
    writer = csv._____(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer._____({"name": "Alice", "age": "30"})

# ============================================================
# Question 14
# ============================================================
# Using pathlib
from pathlib import Path
p = _____("data") / "subdir" / "file.txt"

# ============================================================
# Question 15
# ============================================================
# Check if file exists
import os
if os.path._____("file.txt"):
    print("Exists")

# ============================================================
# Question 16
# ============================================================
# Get file size in bytes
size = os.path._____("file.txt")

# ============================================================
# Question 17
# ============================================================
# Context manager (with statement) is also called a _____ manager.

# ============================================================
# Question 18
# ============================================================
# Specify encoding when opening a file
with open("file.txt", "r", _____="utf-8") as f:
    content = f.read()

# ============================================================
# Question 19
# ============================================================
# Binary read mode
with open("image.jpg", _____) as f:
    data = f.read()

# ============================================================
# Question 20
# ============================================================
# Join path components
path = os.path._____("folder", "subfolder", "file.txt")

# ============================================================
# Question 21
# ============================================================
# Get the filename from a path
name = os.path._____("/home/user/file.txt")  # Returns "file.txt"

# ============================================================
# Question 22
# ============================================================
# Get the directory from a path
d = os.path._____("/home/user/file.txt")  # Returns "/home/user"

# ============================================================
# Question 23
# ============================================================
# Check if a path is a directory
if os.path._____("mydir"):
    print("It's a directory")

# ============================================================
# Question 24
# ============================================================
# Read all text from a file using pathlib
content = Path("file.txt")._____()

# ============================================================
# Question 25
# ============================================================
# Write text to a file using pathlib
Path("file.txt")._____("Hello, World!")

# ============================================================
# Question 26
# ============================================================
# The exclusive creation mode (fails if file exists)
with open("new.txt", _____) as f:
    f.write("data")

# ============================================================
# Question 27
# ============================================================
# Read and write mode (file must exist)
with open("file.txt", _____) as f:
    content = f.read()
    f.write("more")

# ============================================================
# Question 28
# ============================================================
# Handle JSON decode error
try:
    json.loads("bad data")
except json.JSON_____Error as e:
    print(f"Invalid JSON: {e}")

# ============================================================
# ANSWERS
# ============================================================
"""
1. open
2. "w"
3. "a"
4. read
5. readline
6. readlines
7. writelines
8. loads
9. load
10. dump
11. dumps
12. DictReader
13. DictWriter, writerow
14. Path
15. exists
16. getsize
17. context
18. encoding
19. "rb"
20. join
21. basename
22. dirname
23. isdir
24. read_text
25. write_text
26. "x"
27. "r+"
28. Decode
"""
