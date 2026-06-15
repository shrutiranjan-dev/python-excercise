"""
Exceptions — Exercises (Module 11)

Total: 35 exercises
  Easy: 10
  Medium: 10
  Hard: 10
  Expert: 5

Solutions are at the bottom of the file.
"""

# ============================================================
# EASY (10 exercises)
# ============================================================

# 1. Write a try/except block that catches ZeroDivisionError when dividing 5 by 0.


# 2. Catch a ValueError when converting "hello" to an integer and print "Invalid int".


# 3. Catch both IndexError and KeyError in one except block when accessing
#    list[10] and dict["missing"].


# 4. Write a function `safe_get(lst, index, default=None)` that returns the list
#    element or default if index is out of range.

def safe_get(lst, index, default=None):
    pass

# 5. Write a try/except/else block that divides 10 by 2 and prints result in else.


# 6. Write a try/except/finally block that prints "Cleanup" in finally.


# 7. Write a function `safe_int(value)` that returns the integer value or 0
#    if conversion fails.

def safe_int(value):
    pass

# 8. Write a function `divide(a, b)` that returns None if division by zero occurs.

def divide(a, b):
    pass

# 9. Write a function `file_exists(filename)` that returns True if the file
#    can be opened, False otherwise (catch FileNotFoundError).

def file_exists(filename):
    pass

# 10. Use assert to check that a number is positive, with message "Must be positive".


# ============================================================
# MEDIUM (10 exercises)
# ============================================================

# 11. Write a function `validate_age(age)` that raises ValueError if age < 0 or age > 150.

def validate_age(age):
    pass

# 12. Write a function `get_env_or_fail(key)` that returns os.environ[key] or
#     raises a custom EnvVariableMissing exception.

class EnvVariableMissing(Exception):
    pass

def get_env_or_fail(key):
    pass

# 13. Write a function `divide_with_assert(a, b)` that uses assert to ensure
#     b is not zero before dividing.

def divide_with_assert(a, b):
    pass

# 14. Write a context manager `FileManager` that opens a file and ensures it closes.

class FileManager:
    def __init__(self, filename, mode="r"):
        pass
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# 15. Write a function `parse_json_safe(s)` that returns the parsed dict or
#     an empty dict if JSON is invalid.

def parse_json_safe(s):
    pass

# 16. Write a function `safe_divide_list(values, divisor)` that divides each
#     element by divisor, skipping elements that cause errors.

def safe_divide_list(values, divisor):
    pass

# 17. Write a function `retry(func, max_attempts=3)` that retries a function
#     if it raises an exception, up to max_attempts times.

def retry(func, max_attempts=3):
    pass

# 18. Write a function `validate_dict(d, required_keys)` that raises KeyError
#     with a message listing which keys are missing.

def validate_dict(d, required_keys):
    pass

# 19. Write a function `safe_write(filename, content)` that writes content to
#     a file and catches any IOError, returning True on success, False on failure.

def safe_write(filename, content):
    pass

# 20. Write a nested try/except that catches outer (TypeError) and inner (ValueError):

def nested_exceptions():
    pass


# ============================================================
# HARD (10 exercises)
# ============================================================

# 21. Write a function `exponential_backoff(attempt, base=1)` that returns the
#     sleep time (base * 2^attempt) with jitter (+- random 0.5).

def exponential_backoff(attempt, base=1):
    pass


# 22. Write a function `circuit_breaker(func, threshold=3, cooldown=10)` that
#     stops calling func after threshold failures until cooldown expires.

def circuit_breaker(func, threshold=3, cooldown=10):
    pass


# 23. Write a class `Transaction` that acts as a context manager. On __exit__,
#     if an exception occurred, print "Rollback"; otherwise print "Commit".

class Transaction:
    pass


# 24. Write a function `convert_type(value, target_type)` that tries to convert
#     value to target_type. On failure, chain-raise a ConversionError.

class ConversionError(Exception):
    pass

def convert_type(value, target_type):
    pass


# 25. Write a function `ignore_errors(func, *exceptions)` that calls func and
#     ignores specified exceptions, returning None on error.

def ignore_errors(func, *exceptions):
    pass


# 26. Write a function `ensure_directory(path)` that creates a directory if
#     it doesn't exist, catching FileExistsError if it already exists.

def ensure_directory(path):
    pass


# 27. Write a function `parse_config(text)` that parses "key=value" lines.
#     Skip blank lines and lines with errors. Return a dict.

def parse_config(text):
    pass


# 28. Write a function `strict_slice(lst, start, end)` that raises IndexError
#     with a descriptive message if indices are out of bounds.

def strict_slice(lst, start, end):
    pass


# 29. Write a function `fallback_chain(funcs, *args, **kwargs)` that tries each
#     function in order, returning the first successful result.

def fallback_chain(funcs, *args, **kwargs):
    pass


# 30. Write a function `validate_and_process(data, validators)` that applies
#     each validator function (raises ValueError on failure) and processes data.

def validate_and_process(data, validators):
    pass


# ============================================================
# EXPERT (5 exercises)
# ============================================================

# 31. Write a decorator `log_exceptions(logger_func=print)` that logs any
#     exception raised by the decorated function and re-raises it.

def log_exceptions(logger_func=print):
    pass


# 32. Write a context manager `timeout(seconds)` that raises TimeoutError if
#     the block takes longer than `seconds` (use signal module or threading).

def timeout(seconds):
    pass


# 33. Write a function `exception_tree(exception_class, depth=0)` that prints
#     the inheritance tree for a given exception class.

def exception_tree(exception_class, depth=0):
    pass


# 34. Write a function `safe_import(module_name, fallback=None)` that tries to
#     import a module and returns the fallback if ImportError occurs.

def safe_import(module_name, fallback=None):
    pass


# 35. Write a function `suppress_and_log(*exceptions, logger=None)` that returns
#     a context manager that suppresses specified exceptions and logs them.

@contextlib.contextmanager
def suppress_and_log(*exceptions, logger=None):
    pass


# ============================================================
# SOLUTIONS
# ============================================================

"""
=== EASY ===

# 1
try:
    5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2
try:
    int("hello")
except ValueError:
    print("Invalid int")

# 3
try:
    x = [1, 2, 3][10]
    y = {"a": 1}["missing"]
except (IndexError, KeyError):
    print("Index or key error")

# 4
def safe_get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default

# 5
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print(f"Result: {result}")

# 6
try:
    print("Trying")
finally:
    print("Cleanup")

# 7
def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0

# 8
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# 9
def file_exists(filename):
    try:
        with open(filename):
            return True
    except FileNotFoundError:
        return False

# 10
x = 5
assert x > 0, "Must be positive"

=== MEDIUM ===

# 11
def validate_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"Invalid age: {age}")

# 12
class EnvVariableMissing(Exception):
    pass

def get_env_or_fail(key):
    import os
    try:
        return os.environ[key]
    except KeyError:
        raise EnvVariableMissing(f"Missing env var: {key}")

# 13
def divide_with_assert(a, b):
    assert b != 0, "Division by zero"
    return a / b

# 14
class FileManager:
    def __init__(self, filename, mode="r"):
        self.file = open(filename, mode)
    def __enter__(self):
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False

# 15
def parse_json_safe(s):
    import json
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return {}

# 16
def safe_divide_list(values, divisor):
    result = []
    for v in values:
        try:
            result.append(v / divisor)
        except (TypeError, ZeroDivisionError):
            result.append(None)
    return result

# 17
def retry(func, max_attempts=3):
    last_exception = None
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            last_exception = e
    raise last_exception

# 18
def validate_dict(d, required_keys):
    missing = [k for k in required_keys if k not in d]
    if missing:
        raise KeyError(f"Missing keys: {missing}")

# 19
def safe_write(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        return True
    except IOError:
        return False

# 20
def nested_exceptions():
    try:
        try:
            int("abc")
        except ValueError:
            print("Inner caught ValueError")
            raise TypeError("Wrapped") from None
    except TypeError as e:
        print(f"Outer caught: {e}")

=== HARD ===

# 21
def exponential_backoff(attempt, base=1):
    import random
    return base * (2 ** attempt) + random.uniform(-0.5, 0.5)

# 22
def circuit_breaker(func, threshold=3, cooldown=10):
    failures = 0
    last_failure_time = 0

    def wrapper(*args, **kwargs):
        nonlocal failures, last_failure_time
        import time
        if failures >= threshold:
            if time.time() - last_failure_time < cooldown:
                raise RuntimeError("Circuit breaker open")
            failures = 0
        try:
            result = func(*args, **kwargs)
            failures = 0
            return result
        except Exception as e:
            failures += 1
            last_failure_time = time.time()
            raise
    return wrapper

# 23
class Transaction:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Rollback")
        else:
            print("Commit")
        return False

# 24
class ConversionError(Exception):
    pass

def convert_type(value, target_type):
    try:
        return target_type(value)
    except (ValueError, TypeError) as e:
        raise ConversionError(
            f"Cannot convert {value!r} to {target_type.__name__}"
        ) from e

# 25
def ignore_errors(func, *exceptions):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exceptions:
            return None
    return wrapper

# 26
def ensure_directory(path):
    import os
    try:
        os.makedirs(path, exist_ok=True)
    except FileExistsError:
        pass

# 27
def parse_config(text):
    result = {}
    for line in text.strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            key, value = line.split("=", 1)
            result[key.strip()] = value.strip()
        except ValueError:
            continue
    return result

# 28
def strict_slice(lst, start, end):
    if start < 0 or end > len(lst):
        raise IndexError(
            f"Slice [{start}:{end}] out of bounds for list of length {len(lst)}"
        )
    return lst[start:end]

# 29
def fallback_chain(funcs, *args, **kwargs):
    for i, func in enumerate(funcs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if i == len(funcs) - 1:
                raise
    return None

# 30
def validate_and_process(data, validators):
    for validator in validators:
        try:
            validator(data)
        except ValueError as e:
            raise ValueError(f"Validation failed: {e}")
    return data

=== EXPERT ===

# 31
def log_exceptions(logger_func=print):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger_func(f"Exception in {func.__name__}: {e}")
                raise
        return wrapper
    return decorator

# 32
def timeout(seconds):
    import signal

    class TimeoutError(Exception):
        pass

    def handler(signum, frame):
        raise TimeoutError(f"Timed out after {seconds}s")

    @contextlib.contextmanager
    def timeout_context():
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(seconds)
        try:
            yield
        finally:
            signal.alarm(0)

    return timeout_context()

# 33
def exception_tree(exception_class, depth=0):
    indent = "  " * depth
    print(f"{indent}{exception_class.__name__}")
    for subclass in exception_class.__subclasses__():
        exception_tree(subclass, depth + 1)

# 34
def safe_import(module_name, fallback=None):
    try:
        import importlib
        return importlib.import_module(module_name)
    except ImportError:
        return fallback

# 35
import contextlib

@contextlib.contextmanager
def suppress_and_log(*exceptions, logger=None):
    try:
        yield
    except exceptions as e:
        if logger:
            logger(f"Suppressed: {e}")
"""
