#!/usr/bin/env python3
"""
Variables & Types — Examples
Level 0 → Level 5: From basics to production patterns.
"""

# =============================================================================
# Level 0 — Simple variable
# =============================================================================

name = "Alice"
print(name)  # Alice


# =============================================================================
# Level 1 — Multiple variables and types
# =============================================================================

name = "Alice"
age = 25
height = 5.6
is_student = True
print(f"{name}, {age}, {height}, {is_student}")  # Alice, 25, 5.6, True


# =============================================================================
# Level 2 — User input with type conversion
# =============================================================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old")


# =============================================================================
# Level 3 — Real world: Model configuration
# =============================================================================

MODEL_NAME = "gpt-4"
MAX_TOKENS = 2048
TEMPERATURE = 0.7
TOP_P = 0.9
print(f"Config: model={MODEL_NAME}, max_tokens={MAX_TOKENS}, temperature={TEMPERATURE}")
# Config: model=gpt-4, max_tokens=2048, temperature=0.7


# =============================================================================
# Level 4 — Mini challenge: Token cost calculator
# =============================================================================

model_name = "gpt-4"
input_tokens = 500
output_tokens = 200
input_cost_per_1k = 0.03
output_cost_per_1k = 0.06
total_cost = (input_tokens / 1000) * input_cost_per_1k + (output_tokens / 1000) * output_cost_per_1k
print(f"Total cost for {model_name}: ${total_cost:.4f}")
# Total cost for gpt-4: $0.0270


# =============================================================================
# Level 5 — Production style: Config dataclass
# =============================================================================

from dataclasses import dataclass


@dataclass
class ModelConfig:
    model_name: str
    max_tokens: int
    temperature: float
    top_p: float


config = ModelConfig("gpt-4", 2048, 0.7, 0.9)
print(f"Model: {config.model_name}, Max Tokens: {config.max_tokens}")
# Model: gpt-4, Max Tokens: 2048


# =============================================================================
# Bonus: Type checking examples
# =============================================================================

print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("hello"))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type(None))         # <class 'NoneType'>

# Multiple assignment
a = b = c = 0
print(a, b, c)            # 0 0 0

name, age, height = "Bob", 30, 6.0
print(name, age, height)  # Bob 30 6.0

# Swapping
x, y = 10, 20
x, y = y, x
print(x, y)               # 20 10

# None vs False
result = None
print(result is None)     # True
print(result == False)    # False — different type

# Type conversion
print(int("42"))          # 42
print(float("3.14"))      # 3.14
print(str(100))           # "100"
print(bool(1))            # True
print(bool(0))            # False
print(bool(""))           # False
print(bool("text"))       # True
