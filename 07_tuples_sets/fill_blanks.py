"""
Fill-in-the-Blank: Python Tuples and Sets
Fill in the blanks (_____) to make each statement correct.
Hints and solutions are provided below each exercise.
"""

# ============================================================
# SECTION 1: Tuple Creation
# ============================================================

# 1.1 Create an empty tuple
empty = _____  # Hint: Use parentheses
# Solution: ()

# 1.2 Create a single-element tuple (must include trailing comma)
single = (5,)  # The comma is essential!
# Hint: Without the comma, (5) is just an int in parentheses
# Solution: (5,)

# 1.3 Create a tuple of three integers
numbers = (1, _____, 3)  # Hint: Fill in the missing number
# Solution: 2

# 1.4 Tuple packing (no parentheses)
packed = 10, _____, 30  # Hint: Fill in 20
# Solution: 20

# ============================================================
# SECTION 2: Tuple Indexing and Slicing
# ============================================================

t = (10, 20, 30, 40, 50)

# 2.1 Get first element
first = t[_____]  # Hint: Index 0
# Solution: 0

# 2.2 Get last element
last = t[_____]  # Hint: -1
# Solution: -1

# 2.3 Slice to get (20, 30, 40)
middle = t[_____]  # Hint: [1:4]
# Solution: 1:4

# 2.4 Get reversed tuple
reversed_t = t[_____]  # Hint: [::-1]
# Solution: ::-1

# ============================================================
# SECTION 3: Tuple Unpacking
# ============================================================

# 3.1 Basic unpacking
point = (3, 4)
x, y = _____  # Hint: Assign to multiple variables
# Solution: point

# 3.2 Swapping variables
a, b = 1, 2
a, b = _____, _____  # Hint: Swap using tuple unpacking
# Solution: b, a

# 3.3 Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
# first = _____  # Hint: 1
# rest = _____   # Hint: [2, 3, 4, 5]
# Solution: first=1, rest=[2,3,4,5]

# ============================================================
# SECTION 4: Tuple Methods and Properties
# ============================================================

t = (1, 2, 3, 2, 4, 2)

# 4.1 Count occurrences of 2
count = t._____(2)  # Hint: count()
# Solution: count

# 4.2 Find index of first 3
idx = t._____(3)  # Hint: index()
# Solution: index

# 4.3 Get length
length = _____(t)  # Hint: len()
# Solution: len

# 4.4 Check immutability
# t[0] = 10  # This would raise a _____  # Hint: TypeError
# Solution: TypeError

# ============================================================
# SECTION 5: Set Creation
# ============================================================

# 5.1 Create an empty set
empty = _____()  # Hint: Not {} (that's a dict!)
# Solution: set

# 5.2 Create a set of numbers
numbers = {1, 2, _____, 4, 5}  # Hint: Fill missing number
# Solution: 3

# 5.3 Create a set from a list (removes duplicates)
unique = _____([1, 2, 2, 3, 3, 3])  # Hint: set()
# Solution: set

# ============================================================
# SECTION 6: Set Operations
# ============================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 6.1 Union
union = a _____ b  # Hint: |
# Solution: |

# 6.2 Intersection
intersection = a _____ b  # Hint: &
# Solution: &

# 6.3 Difference
diff = a _____ b  # Hint: -
# Solution: -

# 6.4 Symmetric difference
sym_diff = a _____ b  # Hint: ^
# Solution: ^

# 6.5 Check if a is subset of b
result = a._____(b)  # Hint: issubset()
# Solution: issubset

# 6.6 Check if sets are disjoint
result = a._____({5, 6})  # Hint: isdisjoint()
# Solution: isdisjoint

# ============================================================
# SECTION 7: Set Methods
# ============================================================

s = {1, 2, 3}

# 7.1 Add element
s._____(4)  # Hint: add()
# Solution: add

# 7.2 Remove element (raises error if missing)
s._____(2)  # Hint: remove()
# Solution: remove

# 7.3 Remove element (no error if missing)
s._____(10)  # Hint: discard()
# Solution: discard

# 7.4 Remove and return arbitrary element
popped = s._____()  # Hint: pop()
# Solution: pop

# 7.5 Remove all elements
s._____()  # Hint: clear()
# Solution: clear

# 7.6 Update with elements from another set
s = {1, 2}
s._____({3, 4})  # Hint: update()
# Solution: update

# ============================================================
# SECTION 8: Set Comprehension
# ============================================================

# 8.1 Create set of squares
squares = {x**2 _____ x in range(10)}  # Hint: for
# Solution: for

# 8.2 Create set of even squares
even_squares = {x**2 for x in range(10) _____ x % 2 == 0}  # Hint: if
# Solution: if

# ============================================================
# SECTION 9: Frozensets
# ============================================================

# 9.1 Create a frozenset
fs = _____([1, 2, 3])  # Hint: frozenset()
# Solution: frozenset

# 9.2 Frozensets are hashable and can be used as dict keys
d = {fs: "value"}  # Using frozenset as key
# This works because frozensets are _____  # Hint: hashable
# Solution: hashable

# ============================================================
# SUMMARY: Check your answers above.
# ============================================================

print("Fill-in-the-blank exercises completed. Check your answers!")
