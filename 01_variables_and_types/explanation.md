# Module 01: Variables & Types

## Introduction

Variables are **named containers** that store data in memory. Every programming language needs them — they're how we track state, pass data around, and build complex systems.

In Python, variables are:
- **Created by assignment** — no declaration keyword needed
- **Dynamically typed** — the type is inferred from the value
- **Strongly typed** — Python won't silently coerce types (no `"2" + 2` nonsense)
- **References to objects** — everything is an object, variables are just labels

### Why they exist

Without variables, you'd have to hardcode every value. Variables let us write **general, reusable code** that works with different inputs.

### Where they're used

Everywhere. Configuration values, user input, intermediate computations, loop counters, function arguments, return values — literally every line of code.

---

## JavaScript Comparison

| Concept | JavaScript | Python |
|---|---|---|
| Variable declaration | `let`, `const`, `var` | Just assign: `name = "Alice"` |
| Null / None | `null`, `undefined` (two!) | `None` (one canonical null) |
| Integer type | `Number` (float64 for everything) | `int` (arbitrary precision) |
| Number types | `Number` (float64) | `int`, `float`, `complex` |
| String type | `String` | `str` |
| Boolean type | `Boolean` | `bool` |
| Check type | `typeof x` | `type(x)` |
| Dynamic typing | Yes | Yes |
| Strong typing | No (weak) | Yes (strong) |
| Truthiness | Falsy: `0`, `""`, `null`, `undefined`, `NaN`, `false` | Falsy: `0`, `""`, `None`, `False`, empty collections |
| Type coercion | `"5" - 3` → `2` (coerces) | `"5" - 3` → TypeError |
| `switch` / `match` | `switch` statement | `match` statement (3.10+) |

### Key insight

If you're coming from TypeScript, you might feel like Python is less strict. It is. But Python's philosophy is different: **"We're all consenting adults here."** Instead of the compiler catching type errors, Python relies on:
- Clear naming conventions
- Type hints (optional, but use them!)
- Testing
- Good discipline

---

## Concepts

### Variable Assignment

```python
# No let, const, or var — just the name
name = "Alice"       # str
age = 25             # int
height = 5.6         # float
is_active = True     # bool
nothing = None       # NoneType
```

A variable is created the first time you assign to it. If you use a variable before assignment, Python raises `NameError`.

### Naming Conventions

Python uses `snake_case` for variables and functions:

```python
# ✅ Pythonic
model_name = "gpt-4"
max_tokens = 2048

# ❌ Not Pythonic (looks like JavaScript)
modelName = "gpt-4"
maxTokens = 2048
```

| Style | When to Use | Example |
|---|---|---|
| `snake_case` | Variables, functions, modules | `model_name`, `get_response()` |
| `UPPER_CASE` | Constants | `MAX_TOKENS = 4096` |
| `PascalCase` | Classes | `class ModelConfig:` |
| `_single_leading` | Internal / private | `_internal_value` |
| `__double_leading` | Name mangling (rare) | `__private_attr` |

### Dynamic Typing

The same variable can hold different types at different times:

```python
value = 42           # int
value = "hello"      # str — same variable, new type
value = [1, 2, 3]    # list — no problem
```

This is powerful but dangerous. Type hints help manage the chaos.

### The `type()` Function

```python
print(type(42))          # <class 'int'>
print(type("hello"))     # <class 'str'>
print(type(3.14))        # <class 'float'>
print(type(True))        # <class 'bool'>
print(type(None))        # <class 'NoneType'>
```

Use `type()` liberally when debugging. It's the `console.log` of Python type debugging.

### `None` Type

`None` is Python's null. It's a singleton — there's only one `None` in existence.

```python
result = None           # No value yet
result = compute_something()
```

- `None` is falsy: `bool(None)` → `False`
- Check with `is` (not `==`): `if result is None:`
- Different from `False`, `0`, `""`, `[]`

### Basic Types

| Type | Example | Notes |
|---|---|---|
| `int` | `42`, `-10`, `1_000_000` | Arbitrary precision (no overflow) |
| `float` | `3.14`, `1e5`, `0.5` | 64-bit IEEE 754 |
| `str` | `"hello"`, `'world'` | Immutable, Unicode |
| `bool` | `True`, `False` | Subclass of `int` (`True == 1`, `False == 0`) |
| `NoneType` | `None` | Singleton null |

### Type Conversion

Explicit conversion is required — no implicit coercion:

```python
# String to int
age = int("25")

# Int to string
message = "Age: " + str(25)

# String to float
price = float("19.99")

# Anything to bool
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("hello")  # True
bool([])       # False
bool([1, 2])   # True
```

### Multiple Assignment

```python
# Same value to multiple variables
a = b = c = 0

# Tuple unpacking
name, age, height = "Alice", 25, 5.6

# Swapping (no temp variable needed!)
a, b = b, a
```

---

## Type System: Dynamic but Strong

Python is **dynamically typed** (types are checked at runtime) but **strongly typed** (types are not implicitly coerced).

```python
# Dynamic: variable can change type
x = 42
x = "hello"  # OK

# Strong: no implicit coercion
"hello" + 42       # TypeError
"hello" + str(42)  # "hello42" — explicit conversion required
```

Compare with JavaScript:
```javascript
// JS: weakly typed — implicit coercion everywhere
"5" - 3     // 2 (string coerced to number)
"5" + 3     // "53" (number coerced to string)
```

Python's strong typing means fewer surprises but more explicit conversions. This is generally better for production systems.

---

## Common Mistakes

### Mistake 1: Using camelCase

```python
# ❌ JavaScript habit
modelName = "gpt-4"

# ✅ Pythonic
model_name = "gpt-4"
```

### Mistake 2: Forgetting `type()` for debugging

```python
# When something unexpected happens:
value = some_function()
print(type(value))  # Always check the type first!
```

### Mistake 3: Confusing `None` with `False`

```python
result = None

# ❌ Wrong comparison
if result == False:
    print("no result")  # This won't run — None != False

# ✅ Correct
if result is None:
    print("no result")
```

### Mistake 4: Using undeclared variables

```python
# ❌ This will raise NameError
print(undefined_variable)

# ✅ Always assign before use
undefined_variable = None
print(undefined_variable)
```

### Mistake 5: Assuming float precision

```python
0.1 + 0.2 == 0.3  # False! Floating point precision
```

---

## Best Practices

### 1. Use `snake_case`

```python
# ✅
user_name = "Alice"
token_count = 1500

# ❌
userName = "Alice"
tokenCount = 1500
```

### 2. Use meaningful names

```python
# ❌
x = "gpt-4"
y = 2048

# ✅
model_name = "gpt-4"
max_tokens = 2048
```

### 3. Use type hints (introduced early)

```python
name: str = "Alice"
age: int = 25
scores: list[float] = [0.9, 0.85, 0.95]
```

### 4. Constants in `ALL_CAPS`

```python
MAX_RETRIES = 3
API_TIMEOUT = 30
DEFAULT_MODEL = "gpt-4"
```

### 5. Avoid single-letter names (except loops)

```python
# ❌ Avoid
m = "gpt-4"
t = 2048

# ✅ Except in loops
for i in range(10):
    print(i)
for j, k in zip(list_a, list_b):
    print(j, k)
```

---

## AI Engineering Relevance

Everything in AI engineering starts with variables and types:

| AI Concept | Python Type | Example |
|---|---|---|
| Model name | `str` | `model_name = "gpt-4"` |
| Token count | `int` | `input_tokens = 500` |
| Temperature | `float` | `temperature = 0.7` |
| Probability score | `float` | `confidence = 0.95` |
| Enable/disable flag | `bool` | `use_streaming = True` |
| API response (pending) | `None` | `response = None` |
| Max tokens limit | `int` (constant) | `MAX_TOKENS = 4096` |
| Model config | `dataclass` | `ModelConfig(...)` |

### Real example: LLM API call config

```python
from dataclasses import dataclass

@dataclass
class LLMConfig:
    model: str = "gpt-4"
    temperature: float = 0.7
    max_tokens: int = 2048
    top_p: float = 0.9
    stream: bool = False

config = LLMConfig()
print(f"Using {config.model} with temperature {config.temperature}")
```

This is exactly how production AI systems configure their model calls. You'll see this pattern in LangChain, LlamaIndex, and OpenAI SDK.
