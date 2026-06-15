#!/usr/bin/env python3
"""
Operators — Fill in the Blanks

Instructions:
  Replace each _____ with the correct Python code.
  Run this file to check your answers.
  Solutions are at the bottom — no peeking!
"""

# =============================================================================
# Level 0 — Basic arithmetic
# =============================================================================

# 1. Add 10 and 5
print(10 _____ 5)  # 15

# 2. Subtract 8 from 20
print(20 _____ 8)  # 12

# 3. Multiply 6 by 7
print(6 _____ 7)  # 42

# 4. Divide 15 by 4 (true division)
print(15 _____ 4)  # 3.75

# 5. Floor divide 15 by 4
print(15 _____ 4)  # 3

# 6. Get remainder of 17 divided by 5
print(17 _____ 5)  # 2

# 7. Calculate 2 to the power of 10
print(2 _____ 10)  # 1024


# =============================================================================
# Level 1 — Comparison and logic
# =============================================================================

# 8. Check if 10 is greater than 5
print(10 _____ 5)  # True

# 9. Check if 3 is equal to "3"
print(3 _____ "3")  # False (no type coercion)

# 10. Check if 7 is not equal to 8
print(7 _____ 8)  # True

# 11. Check if 5 is between 1 and 10 (use chaining)
print(1 _____ 5 _____ 10)  # True

# 12. Use AND logic
print(True _____ False)  # False

# 13. Use OR logic
print(False _____ False)  # False

# 14. Use NOT logic
print(_____ True)  # False

# 15. Ternary: assign "yes" if 5 > 3 else "no"
result = "yes" _____ 5 > 3 _____ "no"
print(result)  # yes


# =============================================================================
# Level 2 — Assignment operators
# =============================================================================

# 16. Use +=
x = 10
x _____ 5
print(x)  # 15

# 17. Use *=
y = 3
y _____ 4
print(y)  # 12

# 18. Use //=
z = 17
z _____ 5
print(z)  # 3

# 19. Use %=
w = 20
w _____ 7
print(w)  # 6

# 20. Use **=
v = 2
v _____ 10
print(v)  # 1024


# =============================================================================
# Level 3 — Identity and membership
# =============================================================================

# 21. Check identity with is
a = [1, 2]
b = [1, 2]
c = a
print(a _____ c)  # True (same object)
print(a _____ b)  # False (different objects)

# 22. Check membership with in
colors = ["red", "green", "blue"]
print("red" _____ colors)   # True
print("yellow" _____ colors)  # False

# 23. Check NOT membership
print("yellow" _____ colors)  # True (yellow is NOT in colors)

# 24. Check substring with in
text = "Hello, World!"
print("World" _____ text)  # True
print("world" _____ text)  # False (case-sensitive)

# 25. Use is with None
value = None
print(value _____ None)  # True


# =============================================================================
# Level 4 — Real-world patterns
# =============================================================================

# 26. Confidence threshold check
confidence = 0.92
threshold = 0.8
is_reliable = confidence _____ threshold
print(is_reliable)  # True

# 27. Token budget check
used_tokens = 1500
max_allowed = 2048
within_budget = used_tokens _____ max_allowed
print(within_budget)  # True

# 28. Temperature range check (0.0 to 2.0)
temperature = 1.5
in_range = 0.0 _____ temperature _____ 2.0
print(in_range)  # True

# 29. Model routing with OR
model = "gpt-4"
is_supported = model _____ "gpt-4" _____ model _____ "claude-3"
print(is_supported)  # True

# 30. Rate limiting with modulo
request_count = 61
rate_limit = 60
is_limited = (request_count _____ rate_limit) == 0
print(is_limited)  # False (61 % 60 = 1, not 0)


# =============================================================================
# Level 5 — Complex expressions
# =============================================================================

# 31. Precedence: what is 5 + 3 * 2 ** 2?
result = 5 + 3 * 2 ** 2
print(result)  # _____ (think about order of operations)

# 32. Batch size check with AND and modulo
batch_size = 32
data_len = 128
valid = data_len % batch_size _____ 0 _____ data_len > 0
print(valid)  # True

# 33. Chained comparison with logical
score = 75
grade = "A" if score _____ 90 _____ "B" if score _____ 80 _____ "C" if score _____ 70 _____ "F"
print(grade)  # C

# 34. Cost calculation (tokens / 1000) * rate
input_tokens = 1500
rate = 0.03
cost = (input_tokens _____ 1000) _____ rate
print(f"${cost:.4f}")  # $0.0450

# 35. Power with modulus — last digit of 7^1000
last_digit = 7 ** 1000 _____ 10
print(f"Last digit: {last_digit}")


# =============================================================================
# SOLUTIONS
# =============================================================================

# Level 0:
# 1. +
# 2. -
# 3. *
# 4. /
# 5. //
# 6. %
# 7. **

# Level 1:
# 8. >
# 9. == (not ===, Python doesn't have it)
# 10. !=
# 11. <, <
# 12. and
# 13. or
# 14. not
# 15. if, else

# Level 2:
# 16. +=
# 17. *=
# 18. //=
# 19. %=
# 20. **=

# Level 3:
# 21. is, is not
# 22. in, not in
# 23. not in
# 24. in, not in
# 25. is

# Level 4:
# 26. >=
# 27. <=
# 28. <=, <= (or < and < if exclusive)
# 29. ==, or, ==
# 30. %

# Level 5:
# 31. 17 (5 + 3 * 4 → 5 + 12)
# 32. ==, and
# 33. >=, if, >=, else, >=, else (or simplified)
#    Actually: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
# 34. /, *
# 35. %
