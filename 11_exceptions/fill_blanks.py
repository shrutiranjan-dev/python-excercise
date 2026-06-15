"""
Fill in the blanks — Exceptions (Module 11)

Instructions: Replace each ___ with a valid Python expression.
Hints and solutions are provided after each block.
"""

# ============================================================
# Section 1: try/except basics
# ============================================================

# 1. Basic try-except structure
___:
    result = 10 / 0
___ ZeroDivisionError:
    print("Cannot divide by zero!")

# 2. Catch exception with variable
try:
    int("abc")
___ ValueError ___ e:
    print(f"Error: {e}")

# 3. Catch multiple exception types
try:
    [1, 2, 3][10]
except (___, ___):
    print("Index or type error")

# ============================================================
# Section 2: else and finally
# ============================================================

# 4. else runs when ___ exception occurs.
#    Hint: no

# 5. finally ___ runs.
#    Hint: always

# 6. try/except/else/finally structure
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
___:  # Runs on success
    print(f"Result: {result}")
___:  # Always runs
    print("Done")

# ============================================================
# Section 3: Raising exceptions
# ============================================================

# 7. Raise a ValueError
___ ValueError("Invalid input")

# 8. Re-raise current exception
try:
    risky()
except:
    ___  # Hint: raise

# 9. Raise with a condition
x = -5
if x < 0:
    ___ ValueError("x must be non-negative")

# ============================================================
# Section 4: Custom exceptions
# ============================================================

# 10. Define a custom exception
class MyError(___):
    pass

# 11. Custom exception with constructor
class APIError(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
        ___().__init__(f"Error {code}: {msg}")  # Hint: super

# 12. Raise custom exception
___ MyError("Something went wrong")

# ============================================================
# Section 5: Exception chaining
# ============================================================

# 13. Chain exceptions with 'from'
try:
    int("abc")
except ValueError as e:
    ___ RuntimeError("Conversion failed") ___ e

# ============================================================
# Section 6: assert
# ============================================================

# 14. Basic assert
x = 5
___ x > 0, "x must be positive"

# 15. Assert raises ___Error if condition is False.
#    Hint: Assertion

# ============================================================
# Section 7: Context managers
# ============================================================

# 16. Using with for file handling
___ open("file.txt", "r") ___ f:
    content = f.read()

# 17. Custom context manager methods
class MyResource:
    def ___:  # Enter method
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleanup")

# ============================================================
# Section 8: Common exceptions
# ============================================================

# 18. Accessing a missing dictionary key raises ___
d = {}
# d["missing"]  # raises ___

# 19. Accessing an invalid list index raises ___
lst = [1, 2, 3]
# lst[10]  # raises ___

# 20. Dividing by zero raises ___
# 1 / 0  # raises ___

# 21. Calling undefined attribute raises ___
# "hello".nonexistent()  # raises ___

# ============================================================
# SOLUTIONS (uncomment to check)
# ============================================================

"""
1:  try, except
2:  except, as
3:  IndexError, TypeError
4:  no
5:  always
6:  else, finally
7:  raise
8:  raise
9:  raise
10: Exception
11: super
12: raise
13: raise, from
14: assert
15: Assertion
16: with, as
17: __enter__(self)
18: KeyError
19: IndexError
20: ZeroDivisionError
21: AttributeError
"""
