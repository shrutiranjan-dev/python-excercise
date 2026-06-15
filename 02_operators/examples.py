#!/usr/bin/env python3
"""
Operators — Examples
Level 0 → Level 5: From basics to production patterns.
"""

# =============================================================================
# Level 0 — Simple arithmetic
# =============================================================================

print(10 + 5)   # 15
print(10 - 5)   # 5
print(10 * 5)   # 50
print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3
print(10 % 3)   # 1
print(10 ** 3)  # 1000


# =============================================================================
# Level 1 — All operator types
# =============================================================================

# Arithmetic
a, b = 20, 7
print(f"{a} + {b} = {a + b}")    # 27
print(f"{a} - {b} = {a - b}")    # 13
print(f"{a} * {b} = {a * b}")    # 140
print(f"{a} / {b} = {a / b:.4f}") # 2.8571
print(f"{a} // {b} = {a // b}")   # 2
print(f"{a} % {b} = {a % b}")     # 6
print(f"{a} ** 2 = {a ** 2}")     # 400

# Comparison
print(f"5 == 5: {5 == 5}")      # True
print(f"5 != 5: {5 != 5}")      # False
print(f"5 < 10: {5 < 10}")      # True
print(f"5 > 10: {5 > 10}")      # False
print(f"5 <= 5: {5 <= 5}")      # True
print(f"5 >= 6: {5 >= 6}")      # False
print(f"1 < 5 < 10: {1 < 5 < 10}")  # True (chaining)

# Logical
print(f"True and True: {True and True}")    # True
print(f"True and False: {True and False}")  # False
print(f"True or False: {True or False}")    # True
print(f"not True: {not True}")              # False

# Identity
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(f"x is z: {x is z}")      # True (same object)
print(f"x is y: {x is y}")      # False (different objects)
print(f"x == y: {x == y}")      # True (same value)

# Membership
fruits = ["apple", "banana", "cherry"]
print(f"'apple' in fruits: {'apple' in fruits}")  # True
print(f"'grape' in fruits: {'grape' in fruits}")  # False
print(f"'grape' not in fruits: {'grape' not in fruits}")  # True

# Ternary
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")  # adult


# =============================================================================
# Level 2 — User input calculator
# =============================================================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}" if num2 != 0 else "Cannot divide by zero")


# =============================================================================
# Level 3 — Real world: Score threshold checker
# =============================================================================

MODEL_CONFIDENCE = 0.87
THRESHOLD = 0.8
FALLBACK_THRESHOLD = 0.6

high_confidence = MODEL_CONFIDENCE >= THRESHOLD
medium_confidence = FALLBACK_THRESHOLD <= MODEL_CONFIDENCE < THRESHOLD
low_confidence = MODEL_CONFIDENCE < FALLBACK_THRESHOLD

print(f"High confidence: {high_confidence}")    # True
print(f"Medium confidence: {medium_confidence}") # False
print(f"Low confidence: {low_confidence}")       # False

# Route based on confidence
if MODEL_CONFIDENCE >= THRESHOLD:
    print("Route to GPT-4")
elif MODEL_CONFIDENCE >= FALLBACK_THRESHOLD:
    print("Route to GPT-3.5")
else:
    print("Ask for human review")


# =============================================================================
# Level 4 — Mini challenge: Compound interest calculator
# =============================================================================

principal = 1000.0
rate = 0.05
time = 3
n = 12  # compounded monthly

amount = principal * (1 + rate / n) ** (n * time)
print(f"After {time} years: ${amount:.2f}")
# After 3 years: $1161.47


# =============================================================================
# Level 5 — Production: Percentage calculator with validation
# =============================================================================

def calculate_percentage(value: float, total: float) -> str:
    if total <= 0:
        return "Error: total must be positive"
    if value < 0:
        return "Error: value must be non-negative"
    if value > total:
        return "Error: value cannot exceed total"

    percentage = (value / total) * 100
    return f"{value:.2f} / {total:.2f} = {percentage:.1f}%"

print(calculate_percentage(45, 200))
# 45.00 / 200.00 = 22.5%

print(calculate_percentage(50, 0))
# Error: total must be positive

print(calculate_percentage(-5, 100))
# Error: value must be non-negative
