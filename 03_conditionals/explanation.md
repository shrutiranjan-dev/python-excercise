# Module 03: Conditionals

## What Are Conditionals?
Conditionals let your code make decisions. Based on whether a condition is `True` or `False`, different blocks of code run.

---

## 1. `if`, `elif`, `else`

```python
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

- `if` — first check
- `elif` — "else if" (can have many)
- `else` — fallback (optional)

### JavaScript Comparison
| JavaScript | Python |
|---|---|
| `else if` | `elif` |
| `if (x) { }` | `if x:` |
| `&&`, `\|\|`, `!` | `and`, `or`, `not` |

---

## 2. Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

---

## 3. Truthiness & Falsiness

Values that are **falsy** in Python:
- `False`, `None`, `0`, `0.0`, `""` (empty string)
- Empty collections: `[]`, `()`, `{}`, `set()`

Everything else is **truthy**.

```python
name = ""
if not name:
    print("Name is empty")  # runs because "" is falsy
```

### JavaScript Comparison
| JS Falsy | Python Falsy |
|---|---|
| `false` | `False` |
| `null` / `undefined` | `None` |
| `0`, `0n` | `0`, `0.0` |
| `""` | `""` |
| `NaN` | (no equivalent) |

---

## 4. Ternary (Conditional Expression)

```python
status = "adult" if age >= 18 else "minor"
```

---

## 5. Nested Conditionals

```python
if authenticated:
    if is_admin:
        print("Welcome admin!")
    else:
        print("Welcome user!")
else:
    print("Please log in.")
```

---

## 6. match-case (Python 3.10+)

```python
status_code = 404
match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown")
```

The `_` wildcard matches anything (like `default`).

### JavaScript Comparison
| JavaScript | Python |
|---|---|
| `switch(x) { case 1: ... break; }` | `match x: case 1: ...` |
| `default:` | `case _:` |
| `break` (fallthrough) | No fallthrough (automatic break) |

---

## AI Relevance

- **Model response routing**: Route to different models based on confidence thresholds
- **Error handling chains**: Retry logic with conditional fallbacks
- **Confidence thresholds**: Only accept LLM responses above a certainty score
- **RAG fallback logic**: If vector search returns low scores, fall back to keyword search
- **Content moderation**: Multi-stage filtering with escalating rules

```python
confidence = 0.85
if confidence >= 0.95:
    model = "gpt-4"
elif confidence >= 0.80:
    model = "claude-3"
else:
    model = "fallback-llama"
```
