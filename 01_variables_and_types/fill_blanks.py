#!/usr/bin/env python3
"""
Variables & Types — Fill in the Blanks

Instructions:
  Replace each _____ with the correct Python code.
  Run this file to check your answers.
  Solutions are at the bottom — no peeking!
"""

# =============================================================================
# Level 0 — Basic assignment
# =============================================================================

# 1. Assign your name to a variable
name = "user one"
print(name)

# 2. Assign your age
age = 26
print(age)

# 3. Create a greeting variable
greeting = "Hello, " + name
print(greeting)

# 4. Assign a float value
price = 77.79
print(price)

# 5. Assign a boolean
is_learning = True
print(is_learning)


# =============================================================================
# Level 1 — Types and multiple assignment
# =============================================================================

# 6. Check the type of 42
print(type(name))  # Should be <class 'int'>

# 7. Check the type of 3.14
print(type(price))  # Should be <class 'float'>

# 8. Check the type of True
print(type(is_learning))  # Should be <class 'bool'>

# 9. Multiple assignment: set a, b, c to 1, 2, 3
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# 10. Assign the same value to x, y, z
x = y = z = 69
print(x, y, z)

# 11. Check the type of None
print(type(None))  # <class 'NoneType'>


# =============================================================================
# Level 2 — Type conversion
# =============================================================================

# 12. Convert string "25" to int
age_str = "25"
age = int(age_str)
print(age)  # 25

# 13. Convert int to string
count = 42
count_str = str(count)
print(count_str)  # "42"

# 14. Convert string to float
price_str = "19.99"
price = float(price_str)
print(price)  # 19.99

# 15. Convert to bool — what's truthy?
print(bool(1))    # true
print(bool(0))    # false
print(bool(""))   # false
print(bool("x"))  # true

# 16. Convert user input (always a string) to int
user_input = "30"
user_age = int(user_input)
print(user_age + 5)  # 35


# =============================================================================
# Level 3 — None and comparisons
# =============================================================================

# 17. Set result to None
result = None
print(result)  # None

# 18. Check if result is None (use is, not ==)
if result is None:
    print("No result yet")

# 19. None is falsy — check its bool value
print(bool(None))  # false

# 20. Compare: None vs False
value = None
print(value is value)   # True (None is None)
print(value != value)   # False (None != False)


# =============================================================================
# Level 4 — Real-world patterns
# =============================================================================

# 21. Model configuration constants
MODEL_NAME = "gpt-4o"  # "gpt-4o"
MAX_TOKENS = 4096  # 4096
TEMPERATURE = 0.7  # 0.7
print(f"{MODEL_NAME}: max_tokens={MAX_TOKENS}, temp={TEMPERATURE}")
# gpt-4o: max_tokens=4096, temp=0.7

# 22. Token cost calculation
input_tokens = 1000
output_tokens = 500
input_rate = 0.03   # per 1k tokens
output_rate = 0.06  # per 1k tokens
cost = (input_tokens / 1000) * input_rate + (output_tokens / 1000) * output_rate
print(f"Cost: ${cost:.4f}")  # Cost: $0.0600

# 23. Confidence threshold
confidence = 0.95
threshold = 0.8
is_reliable = confidence >= threshold  # use > or >=
print(is_reliable)  # True

# 24. Type check before processing
value = "42"
if type(value) == str:
    print("It's a string!")
    num = int(value)
    print(num + 8)  # 50

# 25. Swap two variables
a = 5
b = 10
a, b = 10, 5
print(f"a={a}, b={b}")  # a=10, b=5

# 26. Named constants for API config
API_KEY = "sk-..."
API_TIMEOUT = "30 seconds"  # 30 seconds
print(f"Timeout: {API_TIMEOUT}s")


# =============================================================================
# Level 5 — Advanced patterns
# =============================================================================

# 27. Type hint a variable
name: str = "Alice"  # fill with the type
age: int = 25        # fill with the type
print(f"{name} is {age}")

# 28. Dataclass creation
from dataclasses import dataclass

@dataclass
class Config:
    model: str  # str
    temperature: float  # float
    max_tokens: int  # int
    stream: bool  # bool

cfg = Config("gpt-4", 0.7, 2048, False)
print(cfg.model)  # gpt-4

# 29. Multiple assignment unpacking
data = ["Alice", 25, 5.6]
name, age, height = data
print(f"{name} is {age}, height {height}")

# 30. Underscore for throwaway values
first, _, last = [1, 2, 3]
print(first, last)  # 1 3


# =============================================================================
# SOLUTIONS — Don't peek until you've tried!
# =============================================================================

# Level 0 solutions:
# 1. "YourName" or any string
# 2. 25 or any integer
# 3. name
# 4. 9.99 or any float
# 5. True or False

# Level 1 solutions:
# 6. 42
# 7. 3.14
# 8. True
# 9. a, b, c
# 10. 0 (or any value)
# 11. None

# Level 2 solutions:
# 12. int
# 13. str
# 14. float
# 15. True, False, False, True
# 16. user_input

# Level 3 solutions:
# 17. None
# 18. is
# 19. False
# 20. None, False

# Level 4 solutions:
# 21. "gpt-4o", 4096, 0.7
# 22. output_rate
# 23. >=
# 24. str
# 25. b, a
# 26. 30

# Level 5 solutions:
# 27. str, int
# 28. str, float, int, bool
# 29. data
# 30. _
