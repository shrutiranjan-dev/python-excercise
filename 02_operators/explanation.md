# Module 02: Operators

## Introduction

Operators are **symbols that perform operations** on values and variables. They're how we compute things — adding numbers, comparing values, checking conditions, and combining logic.

In Python, operators work slightly differently than in JavaScript. Python doesn't have `===` (because `==` already checks both value and type — well, almost), and it uses `and`/`or`/`not` instead of `&&`/`||`/`!`.

### Why they exist

Without operators, programs couldn't calculate, compare, or make decisions. They're the building blocks of all computation.

### Where they're used

Everywhere - scoring model outputs, threshold comparisons, checking membership in RAG contexts, cost calculations, rate limiting, confidence checks.

---

## JavaScript Comparison

| Operator | JavaScript | Python |
|---|---|---|
| Addition | `+` | `+` |
| Subtraction | `-` | `-` |
| Multiplication | `*` | `*` |
| Division | `/` (float) | `/` (float) |
| Integer division | `Math.floor(a / b)` | `//` |
| Modulus | `%` | `%` |
| Exponentiation | `**` | `**` |
| Equal (value) | `==` (loose) | `==` (value, no coercion) |
| Equal (value + type) | `===` | `==` (Python is already strict) |
| Not equal | `!==` | `!=` |
| Less / greater | `<` `>` `<=` `>=` | `<` `>` `<=` `>=` |
| Logical AND | `&&` | `and` |
| Logical OR | `||` | `or` |
| Logical NOT | `!` | `not` |
| Identity | — | `is`, `is not` |
| Membership | — | `in`, `not in` |
| Ternary | `x ? a : b` | `a if x else b` |

### Key difference: `==` vs `is`

```python
# JS: == checks value after coercion, === checks value AND type
# Python: == checks value (no coercion), is checks identity (same object)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True  — same value
print(a is b)  # False — different objects in memory

# But for small integers and strings, Python caches:
x = 256
y = 256
print(x is y)  # True (small integers are cached)

# Always use "is" for None:
result = None
print(result is None)  # ✅ correct
print(result == None)  # ⚠️ works but not idiomatic
```

---

## Concepts

### Arithmetic Operators

```python
a = 10
b = 3

print(a + b)   # 13  — addition
print(a - b)   # 7   — subtraction
print(a * b)   # 30  — multiplication
print(a / b)   # 3.333... — true division (always float)
print(a // b)  # 3   — floor division (integer result)
print(a % b)   # 1   — modulus (remainder)
print(a ** b)  # 1000 — exponentiation (10^3)
```

### Comparison Operators

```python
print(5 == 5)   # True
print(5 != 5)   # False
print(5 < 10)   # True
print(5 > 10)   # False
print(5 <= 5)   # True
print(5 >= 6)   # False

# Chaining (unique to Python)
print(1 < 5 < 10)       # True — same as 1 < 5 and 5 < 10
print(10 > 5 > 1)       # True
print(1 < 5 > 10)       # False — 5 is not > 10
```

### Logical Operators

```python
# and — both must be True
print(True and True)    # True
print(True and False)   # False

# or — at least one must be True
print(True or False)    # True
print(False or False)   # False

# not — negates
print(not True)         # False
print(not False)        # True

# Short-circuit evaluation
# Python stops evaluating as soon as the result is determined
def might_fail():
    print("might_fail() called")
    return False

def might_also_fail():
    print("might_also_fail() called")
    return True

result = might_fail() and might_also_fail()
# Only "might_fail() called" is printed — might_also_fail is never called
```

### Assignment Operators

```python
x = 10       # basic assignment
x += 5       # x = x + 5  → 15
x -= 3       # x = x - 3  → 12
x *= 2       # x = x * 2  → 24
x /= 4       # x = x / 4  → 6.0
x //= 2      # x = x // 2 → 3.0 (still float because of previous division)
x %= 2       # x = x % 2  → 1.0
x **= 3      # x = x ** 3 → 1.0

# Start fresh for clarity
y = 10
y //= 3      # y = 10 // 3 → 3
print(y)     # 3
y %= 2       # y = 3 % 2 → 1
print(y)     # 1
```

### Identity Operators (`is`, `is not`)

Check if two variables refer to the **same object in memory**.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)     # True  — same object
print(a is b)     # False — different objects
print(a is not b) # True  — they are different

# Always use with None:
response = None
if response is None:
    print("No response yet")
```

### Membership Operators (`in`, `not in`)

Check if a value exists in a collection.

```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

# Also works with strings
text = "hello world"
print("hello" in text)       # True
print("xyz" in text)         # False

# AI relevance: checking if a token is in vocabulary
vocab = {"the", "cat", "sat"}
print("dog" in vocab)        # False
```

### Operator Precedence

From highest to lowest precedence:

| Level | Operators | Associativity |
|---|---|---|
| 1 (highest) | `**` | Right-to-left |
| 2 | `+x`, `-x`, `~x` (unary) | — |
| 3 | `*`, `/`, `//`, `%` | Left-to-right |
| 4 | `+`, `-` (binary) | Left-to-right |
| 5 | `<<`, `>>` | — |
| 6 | `&` | — |
| 7 | `^` | — |
| 8 | `|` | — |
| 9 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `in` | — |
| 10 | `not` | — |
| 11 | `and` | — |
| 12 | `or` | — |

```python
# Precedence example
result = 5 + 3 * 2 ** 2  # 5 + 3 * 4 → 5 + 12 → 17
print(result)  # 17

# Use parentheses to be explicit
result = 5 + (3 * (2 ** 2))  # same, but clearer
```

---

## AI Engineering Relevance

| AI Concept | Operator | Example |
|---|---|---|
| Confidence threshold | `>=` | `confidence >= 0.8` |
| Token budget check | `<=` | `total_tokens <= max_tokens` |
| RAG membership | `in` | `query in document_chunk` |
| Temperature range | `and` | `0.0 <= temp <= 2.0` |
| Cost calculation | `*`, `/` | `(tokens / 1000) * rate` |
| Rate limiting | `%` | `request_count % 60` |
| Batch size divisibility | `%` | `len(data) % batch_size == 0` |
| Model routing | `or` | `model == "gpt-4" or model == "claude-3"` |
| Text preprocessing | `not in` | `char not in stop_chars` |
| Chunk size | `//` | `context_window // 2` |

### Real example: Model routing with operators

```python
confidence = 0.95
max_tokens = 2048
input_length = 500

# Check all conditions before calling expensive model
if confidence >= 0.8 and input_length <= max_tokens:
    print("Calling GPT-4 for high-confidence response")
else:
    print("Falling back to cheaper model")

# Check if model is in supported list
supported_models = ["gpt-4", "claude-3", "llama-3"]
model_name = "gpt-3.5"
if model_name not in supported_models:
    print(f"Warning: {model_name} not in supported list")
```
