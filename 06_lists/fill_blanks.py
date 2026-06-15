"""
Fill-in-the-Blank: Python Lists
Fill in the blanks (_____) to make each statement correct.
Hints and solutions are provided below each exercise.
"""

# ============================================================
# SECTION 1: List Creation
# ============================================================

# 1.1 Create an empty list
empty = _____  # Hint: Use square brackets
# Solution: []

# 1.2 Create a list of integers 1 through 5
numbers = [1, _____, 3, 4, _____]  # Hint: Fill in the missing numbers
# Solution: [1, 2, 3, 4, 5]

# 1.3 Create a list using the list() constructor
chars = _____("hello")  # Hint: list() turns an iterable into a list
# Solution: list("hello")

# 1.4 Create a list from a range
nums = list(_____(5))  # Hint: range(5) gives 0,1,2,3,4
# Solution: list(range(5))

# ============================================================
# SECTION 2: Indexing
# ============================================================

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 2.1 Get the first element
first = fruits[_____]  # Hint: Index starts at 0
# Solution: 0

# 2.2 Get the last element using negative indexing
last = fruits[_____]  # Hint: -1 is the last element
# Solution: -1

# 2.3 Get the second element
second = fruits[_____]  # Hint: Index 1
# Solution: 1

# 2.4 Get the second-to-last element
second_last = fruits[_____]  # Hint: -2
# Solution: -2

# ============================================================
# SECTION 3: Slicing
# ============================================================

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3.1 Get elements from index 2 to 5 (exclusive)
slice1 = nums[_____]  # Hint: [start:stop]
# Solution: 2:5

# 3.2 Get first 4 elements
slice2 = nums[_____]  # Hint: [:stop]
# Solution: :4

# 3.3 Get elements from index 6 to end
slice3 = nums[_____]  # Hint: [start:]
# Solution: 6:

# 3.4 Get every other element
slice4 = nums[_____]  # Hint: [::step]
# Solution: ::2

# 3.5 Get reversed list
slice5 = nums[_____]  # Hint: [::-1]
# Solution: ::-1

# 3.6 Get last 3 elements
slice6 = nums[_____]  # Hint: Negative start
# Solution: -3:

# ============================================================
# SECTION 4: List Methods
# ============================================================

# 4.1 Add an item to the end
lst = [1, 2, 3]
lst._____(4)  # Hint: append
# Solution: append

# 4.2 Add all items from another list
lst = [1, 2, 3]
lst._____([4, 5, 6])  # Hint: extend
# Solution: extend

# 4.3 Insert at a specific position
lst = [1, 2, 4, 5]
lst._____(2, 3)  # Hint: insert(index, item)
# Solution: insert

# 4.4 Remove and return the last item
lst = [1, 2, 3]
last = lst._____()  # Hint: pop
# Solution: pop

# 4.5 Remove a specific item by value
lst = [1, 2, 3, 2]
lst._____(2)  # Hint: remove (removes first occurrence)
# Solution: remove

# 4.6 Find the index of an item
lst = [10, 20, 30, 40]
idx = lst._____(30)  # Hint: index
# Solution: index

# 4.7 Count occurrences
lst = [1, 2, 2, 3, 2, 4]
count = lst._____(2)  # Hint: count
# Solution: count

# 4.8 Sort in place
lst = [3, 1, 4, 1, 5, 9]
lst._____()  # Hint: sort
# Solution: sort

# 4.9 Reverse in place
lst = [1, 2, 3, 4, 5]
lst._____()  # Hint: reverse
# Solution: reverse

# ============================================================
# SECTION 5: List Comprehension
# ============================================================

# 5.1 Create squares of 0-9
squares = [x**2 _____ x in range(10)]  # Hint: for
# Solution: for

# 5.2 Create even numbers only
evens = [x for x in range(20) _____ x % 2 == 0]  # Hint: if
# Solution: if

# 5.3 Create list of (x, x*2) tuples
pairs = [(x, x*2) _____ x in range(5)]  # Hint: for
# Solution: for

# 5.4 Flatten a nested list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item _____ row _____ matrix _____ item _____ row]  # Rearrange
flat = [item for row in matrix for item in row]
# Hint: nested for loops, left to right
# Solution: for, in, for, in

# 5.5 Create list with condition on expression
labels = ["even" _____ x % 2 == 0 _____ "odd" for x in range(5)]  # Hint: ternary
# Solution: if, else

# ============================================================
# SECTION 6: Nested Lists
# ============================================================

# 6.1 Access element in nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = matrix[_____][_____]  # Get 5 from the matrix (Hint: row 1, col 1)
# Solution: 1, 1

# 6.2 Get first column of matrix
col = [row[_____] for row in matrix]  # Hint: index 0
# Solution: 0

# ============================================================
# SECTION 7: Operators and Functions
# ============================================================

# 7.1 Get length of list
length = _____([1, 2, 3, 4, 5])  # Hint: len()
# Solution: len

# 7.2 Check if item is in list
present = 3 _____ [1, 2, 3, 4, 5]  # Hint: in operator
# Solution: in

# 7.3 Check if item is not in list
absent = 10 _____ [1, 2, 3, 4, 5]  # Hint: not in
# Solution: not in

# 7.4 Concatenate lists
combined = [1, 2] _____ [3, 4]  # Hint: +
# Solution: +

# 7.5 Repeat list
repeated = [0] _____ 5  # Hint: *
# Solution: *

# ============================================================
# SUMMARY: Check your answers above.
# Each solution is on the line starting with # Solution:
# ============================================================

print("Fill-in-the-blank exercises completed. Check your answers!")
