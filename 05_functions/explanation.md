# Module 05: Functions

## What Are Functions?
Functions are reusable blocks of code that take inputs, perform actions, and return outputs.

---

## 1. Defining and Calling Functions

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!
```

### JavaScript Comparison
| JavaScript | Python |
|---|---|
| `function foo() {}` | `def foo():` |
| `const foo = () => {}` | `foo = lambda: None` |
| No colon after def | Colon required |
| Curly braces `{}` | Indentation |

---

## 2. Parameters vs Arguments

- **Parameters**: variables listed in the function definition
- **Arguments**: values passed when calling the function

---

## 3. Parameter Types

### Positional
```python
def add(a, b):
    return a + b
add(3, 5)  # a=3, b=5
```

### Keyword
```python
add(b=5, a=3)  # order doesn't matter
```

### Default
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
greet("Bob")              # Hello, Bob!
greet("Bob", "Hi")        # Hi, Bob!
```

### Variable-Length: `*args`
```python
def sum_all(*args):
    return sum(args)
sum_all(1, 2, 3)  # 6
```
`args` is a tuple of all positional arguments.

### Variable-Length: `**kwargs`
```python
def print_info(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")
print_info(name="Alice", age=30)
```
`kwargs` is a dict of all keyword arguments.

### JavaScript Comparison
| JavaScript | Python |
|---|---|
| `...args` (rest params) | `*args` |
| `{...obj}` (spread) | `**dict` |
| Default params `x=5` | Default params `x=5` |

---

## 4. Lambda Functions

```python
square = lambda x: x ** 2
square(5)  # 25

numbers = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

### JavaScript Comparison
- JS arrow `(x) => x * x` ≈ Python `lambda x: x * x`
- Python lambdas are limited to single expressions

---

## 5. Docstrings

```python
def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b
```

Access with `help(multiply)` or `multiply.__doc__`.

---

## 6. Scope (LEGB Rule)

Python looks up variables in this order:
1. **L**ocal — inside the current function
2. **E**nclosing — outer functions (nested)
3. **G**lobal — module level
4. **B**uilt-in — Python's built-in names

```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
outer()  # local
```

---

## 7. Recursion

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

Always need a **base case** to avoid infinite recursion.

---

## 8. Type Hints (Python 3.5+)

```python
def add(a: int, b: int) -> int:
    return a + b
```

Type hints are optional and not enforced at runtime, but help with IDE support and readability.

---

## AI Relevance

- **Reusable prompt functions**: Template functions with variable injection
- **API call wrappers**: Functions that wrap API calls with auth, retries, logging
- **Embedding generation functions**: Reusable embedding pipeline
- **Callback patterns**: Pass functions as arguments to agent orchestrators

```python
def generate_embedding(text: str, model: str = "text-embedding-3-small") -> list:
    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding
```
