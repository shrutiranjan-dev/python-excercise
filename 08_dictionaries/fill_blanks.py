"""
Fill-in-the-Blank: Python Dictionaries
Fill in the blanks (_____) to make each statement correct.
Hints and solutions are provided below each exercise.
"""

# ============================================================
# SECTION 1: Dictionary Creation
# ============================================================

# 1.1 Create an empty dict
empty = _____  # Hint: Use curly braces
# Solution: {}

# 1.2 Create a dict with key-value pairs
person = {"name": "Alice", "age": _____}  # Hint: Fill in age 30
# Solution: 30

# 1.3 Create dict using dict() constructor
grades = _____(Alice=85, Bob=92)  # Hint: dict()
# Solution: dict

# 1.4 Create dict from list of pairs
pairs = _____([("a", 1), ("b", 2)])  # Hint: dict()
# Solution: dict

# ============================================================
# SECTION 2: Accessing Values
# ============================================================

d = {"name": "Alice", "age": 30, "city": "New York"}

# 2.1 Access using bracket notation
name = d[_____]  # Hint: key "name"
# Solution: "name"

# 2.2 Access using get() method (safe access)
age = d._____("age")  # Hint: get
# Solution: get

# 2.3 Access with default using get()
country = d._____("country", "USA")  # Hint: get with default
# Solution: get

# 2.4 Check if key exists
has_name = "name" _____ d  # Hint: in
# Solution: in

# ============================================================
# SECTION 3: Modifying Dictionaries
# ============================================================

d = {"a": 1, "b": 2}

# 3.1 Update existing key
d["a"] = _____  # Set to 10
# Solution: 10

# 3.2 Add new key
d[_____] = 3  # Add key "c" with value 3
# Solution: "c"

# 3.3 Update multiple keys at once
d._____({"d": 4, "e": 5})  # Hint: update
# Solution: update

# 3.4 Remove a key and return its value
removed = d._____("d")  # Hint: pop
# Solution: pop

# 3.5 Remove and return last inserted item
last = d._____()  # Hint: popitem
# Solution: popitem

# 3.6 Remove all items
d._____()  # Hint: clear
# Solution: clear

# ============================================================
# SECTION 4: Dictionary Views and Methods
# ============================================================

d = {"x": 10, "y": 20, "z": 30}

# 4.1 Get all keys
keys = d._____()  # Hint: keys
# Solution: keys

# 4.2 Get all values
values = d._____()  # Hint: values
# Solution: values

# 4.3 Get all key-value pairs
items = d._____()  # Hint: items
# Solution: items

# 4.4 Create a copy
copy = d._____()  # Hint: copy
# Solution: copy

# 4.5 Get or set default
result = d._____("w", 0)  # Hint: setdefault
# Solution: setdefault

# ============================================================
# SECTION 5: Dict Comprehension
# ============================================================

# 5.1 Create squares dict
squares = {x: x**2 _____ x in range(5)}  # Hint: for
# Solution: for

# 5.2 Create even squares only
even = {x: x**2 for x in range(10) _____ x % 2 == 0}  # Hint: if
# Solution: if

# 5.3 Create from two lists using zip
names = ["Alice", "Bob"]
scores = [85, 92]
d = {name: score _____ name, score _____ zip(names, scores)}
# Hint: for, in
# Solution: for, in

# 5.4 Swap keys and values
original = {"a": 1, "b": 2}
swapped = {value: _____ for key, value in original.items()}  # Hint: key
# Solution: key

# 5.5 With if-else in expression
labels = {x: "even" _____ x % 2 == 0 _____ "odd" for x in range(5)}
# Hint: if, else
# Solution: if, else

# ============================================================
# SECTION 6: Nested Dicts
# ============================================================

# 6.1 Access nested value
students = {
    "Alice": {"age": 25, "grade": "A"},
    "Bob": {"age": 23, "grade": "B"},
}
alice_grade = students[_____][_____]  # Hint: "Alice", "grade"
# Solution: "Alice", "grade"

# 6.2 Add nested value
students["Charlie"] = {"age": 24, _____: "A"}  # Hint: key "grade" with value "A"
# Solution: "grade"

# ============================================================
# SECTION 7: defaultdict
# ============================================================

from collections import defaultdict

# 7.1 Create defaultdict with int default
counter = _____(int)  # Hint: defaultdict
# Solution: defaultdict

# 7.2 Counting with defaultdict
words = ["a", "b", "a", "c", "b", "a"]
for word in words:
    counter[word] += _____  # Hint: increment by 1
# Solution: 1

# 7.3 Create defaultdict with list default
groups = _____(list)  # Hint: defaultdict
# Solution: defaultdict

# 7.4 Grouping with defaultdict
data = [("fruit", "apple"), ("fruit", "banana"), ("animal", "cat")]
for category, item in data:
    groups[category]._____(item)  # Hint: append
# Solution: append

# ============================================================
# SECTION 8: Merging (Python 3.9+)
# ============================================================

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

# 8.1 Merge using | operator (Python 3.9+)
merged = a _____ b  # Hint: |
# Solution: |

# 8.2 Merge using ** unpacking
merged = {_____a, _____b}  # Hint: **
# Solution: **a, **b

# ============================================================
# SUMMARY: Check your answers above.
# ============================================================

print("Fill-in-the-blank exercises completed. Check your answers!")
