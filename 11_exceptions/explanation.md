# Exceptions in Python

## Try/Except/Else/Finally

```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Value error: {e}")
except (TypeError, KeyError) as e:
    print(f"Type or key error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print(f"Success: {result}")  # Runs if no exception
finally:
    cleanup()  # Always runs
```

## Common Exception Types

| Exception | Cause |
|-----------|-------|
| `ValueError` | Invalid argument value |
| `TypeError` | Wrong type for operation |
| `KeyError` | Missing dict key |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File does not exist |
| `ZeroDivisionError` | Division by zero |
| `AttributeError` | Missing attribute/method |
| `ImportError` | Module not found |
| `StopIteration` | Iterator exhausted |

## Raising Exceptions

```python
raise ValueError("Invalid input")
raise  # Re-raise current exception

# With custom message
if value < 0:
    raise ValueError(f"Value must be non-negative, got {value}")
```

## Custom Exceptions

```python
class ValidationError(Exception):
    pass

class APIError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")
```

## Exception Chaining

```python
try:
    process(data)
except OSError as e:
    raise RuntimeError("Failed to process") from e
```

## `assert` Statement

```python
assert condition, "Message if False"

# Equivalent to:
if not condition:
    raise AssertionError("Message if False")
```

Use asserts for debugging/development, not for production validation (they can be disabled with `-O` flag).

## Context Managers (`with`)

```python
with open("file.txt", "r") as f:
    content = f.read()
# File automatically closed here

# Custom context manager
class ManagedResource:
    def __enter__(self):
        print("Acquiring resource")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        return False  # Don't suppress exceptions
```

## Best Practices

1. **Be specific**: Catch specific exceptions, not bare `except:`
2. **Fail fast**: Validate inputs early with clear error messages
3. **Don't swallow**: Avoid empty `except` blocks that hide bugs
4. **Clean up**: Use `finally` or context managers for resources
5. **Log errors**: Use `logging` module instead of print for errors
6. **Re-raise appropriately**: Convert low-level to domain-specific exceptions

## JS Comparison

| Python | JavaScript |
|--------|-----------|
| `try/except` | `try/catch` |
| `raise` | `throw` |
| `except ValueError as e:` | `catch (e)` (no typing) |
| `else` (success block) | No direct equivalent |
| `finally` | `finally` |
| `class MyError(Exception)` | `class MyError extends Error` |
| `raise ... from e` | Error chaining with `.cause` |
| `with open() as f:` | No direct equivalent |
| `assert condition` | `console.assert()` |

## AI Relevance

- **API error handling**: Handle `openai.APIError`, `openai.RateLimitError` in LLM calls
- **Retry logic**: Exponential backoff on rate limits with `try/except` + `time.sleep`
- **Graceful fallbacks**: In RAG pipelines, catch retrieval failures and serve cached results
- **Input validation**: `ValueError` / custom exceptions in FastAPI request validation
- **Context managers**: Manage GPU memory, file handles, API sessions with `with` statements
- **Logging**: Structured error logging for production AI systems
