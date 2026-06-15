# Strings in Python

## String Creation

Python strings can be created using single quotes, double quotes, or triple quotes:

```python
single = 'Hello'
double = "Hello"
triple_single = '''Multi-line
string'''
triple_double = """Also multi-line"""
```

## Immutability

Strings are **immutable** — once created, they cannot be changed. Any operation that modifies a string creates a **new** string.

```python
s = "hello"
# s[0] = "H"  # TypeError!
s = "H" + s[1:]  # Creates new string: "Hello"
```

## Indexing and Slicing

| Expression | Meaning |
|-----------|---------|
| `s[0]` | First character |
| `s[-1]` | Last character |
| `s[1:4]` | Characters 1,2,3 (end exclusive) |
| `s[:3]` | First 3 characters |
| `s[3:]` | From index 3 to end |
| `s[::-1]` | Reversed string |

## Common Methods

| Method | Description |
|--------|-------------|
| `s.upper()` | Uppercase |
| `s.lower()` | Lowercase |
| `s.strip()` | Remove leading/trailing whitespace |
| `s.split(delim)` | Split into list |
| `delim.join(list)` | Join list into string |
| `s.replace(old, new)` | Replace substring |
| `s.find(sub)` | First index of sub (-1 if not found) |
| `s.index(sub)` | First index of sub (ValueError if not found) |
| `s.startswith(prefix)` | Check prefix |
| `s.endswith(suffix)` | Check suffix |
| `s.count(sub)` | Count occurrences |
| `s.isalpha()` | All letters? |
| `s.isdigit()` | All digits? |
| `s.isspace()` | All whitespace? |

## f-Strings (Python 3.6+)

f-strings embed expressions inside string literals:

```python
name = "Alice"
age = 30
print(f"{name} is {age} years old")
print(f"{name.upper()}")  # Expression evaluation
print(f"{2 * 3}")         # Arithmetic
print(f"{value:.2f}")     # Format specifiers
print(f"{name!r}")        # repr() output
```

## Escape Sequences

| Sequence | Meaning |
|----------|---------|
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

## Raw Strings

Prefix `r` disables escape processing (useful for regex/file paths):

```python
path = r"C:\Users\name"
regex = r"\d+\.\d+"
```

## String Formatting Comparison

```python
# %-formatting (old)
"Name: %s, Age: %d" % (name, age)

# .format() (Python 2.6+)
"Name: {}, Age: {}".format(name, age)

# f-strings (best, 3.6+)
f"Name: {name}, Age: {age}"
```

**Prefer f-strings** — they are faster, more readable, and less error-prone.

## Concatenation vs join

Avoid `+` in loops (O(n²)):
```python
# Bad
result = ""
for s in items:
    result += s  # New string each time

# Good
result = "".join(items)  # O(n)
```

## JS Comparison

| Python | JavaScript |
|--------|-----------|
| `s.lower()` | `s.toLowerCase()` |
| `s.upper()` | `s.toUpperCase()` |
| `s.split(d)` | `s.split(d)` |
| `d.join(list)` | `list.join(d)` |
| `s.strip()` | `s.trim()` |
| `s.replace(a, b)` | `s.replace(a, b)` |
| `f"Hello {name}"` | `` `Hello ${name}` `` |
| `s[1:4]` | `s.slice(1, 4)` |
| `len(s)` | `s.length` |
| `s.startswith(x)` | `s.startsWith(x)` |

## AI Relevance

- **Prompt engineering**: f-strings construct dynamic prompts with user input, context, and instructions
- **Tokenization preprocessing**: `.lower()`, `.strip()`, `.split()` clean text before tokenization
- **RAG text cleaning**: Remove HTML, normalize whitespace via `replace()` and regex
- **Response parsing**: `split()`, `strip()`, and `find()` extract structured data from LLM output
- **Regex patterns**: Raw strings prevent escape-sequence conflicts in pattern definitions
