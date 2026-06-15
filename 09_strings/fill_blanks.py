"""
Fill in the blanks — Strings (Module 09)

Instructions: Replace each ___ with a valid Python expression.
Hints and solutions are provided after each block.
"""

# ============================================================
# Section 1: String creation and immutability
# ============================================================

# 1. Create a string with double quotes
s1 = ___  # Hint: "hello"

# 2. Strings are immutable — this will raise a TypeError
s = "hello"
# s[0] = "H"  # What error? ___

# 3. Triple-quote strings can span ___ lines.
s3 = """line1
line2"""

# ============================================================
# Section 2: Indexing and slicing
# ============================================================

s = "Python"

# 4. Get first character
first = s[___]  # Hint: 0

# 5. Get last character
last = s[___]   # Hint: -1

# 6. Get substring "yth"
sub = s[___:___]  # Hint: 1:4

# 7. Get every other character
step = s[___:___:___]  # Hint: 0:6:2 -> "Pto"

# 8. Reverse the string
rev = s[___]  # Hint: ::-1

# ============================================================
# Section 3: String methods
# ============================================================

# 9. Convert to uppercase
"hello".___()  # -> "HELLO"

# 10. Remove whitespace
"  hi  ".___()  # -> "hi"

# 11. Split by comma
"a,b,c".___(",")  # -> ["a", "b", "c"]

# 12. Join with hyphen
"-".___(["a", "b", "c"])  # -> "a-b-c"

# 13. Replace substring
"I like cats".___("cats", "dogs")  # -> "I like dogs"

# 14. Find index (returns -1 if not found)
"hello".___("x")  # -> -1

# 15. Count occurrences
"banana".___("a")  # -> 3

# 16. Check if starts with prefix
"Python".___("Py")  # -> True

# 17. Check if all alphabetic
"abc123".___()  # -> False

# 18. Check if all digits
"123".___()  # -> True

# ============================================================
# Section 4: f-strings and formatting
# ============================================================

name = "Alice"
age = 30

# 19. f-string interpolation
result = f"___ is ___ years old"  # -> "Alice is 30 years old"

# 20. Format as percentage
score = 0.8567
f"{score:__}"  # -> "85.67%"

# 21. Format float with 2 decimal places
pi = 3.14159
f"{pi:__}"  # -> "3.14"

# 22. Right-align in 10 characters
f"{"hi":__}"  # -> "        hi"

# ============================================================
# Section 5: Escape sequences and raw strings
# ============================================================

# 23. Newline character
print("line1__line2")  # prints on two lines

# 24. Raw string ignores escape sequences
path = __("C:\\Users\\name")  # Hint: r prefix makes '\\' unnecessary

# 25. Tab character
print("col1__col2")  # Hint: \t

# ============================================================
# SOLUTIONS (uncomment to check)
# ============================================================

"""
1:  "hello"
2:  TypeError
3:  multiple
4:  0
5:  -1
6:  1, 4
7:  0, 6, 2
8:  ::-1
9:  upper()
10: strip()
11: split()
12: join()
13: replace()
14: find()
15: count()
16: startswith()
17: isalpha()
18: isdigit()
19: {name}, {age}
20: .2%
21: .2f
22: >10
23: \n
24: r"C:\Users\name"
25: \t
"""
