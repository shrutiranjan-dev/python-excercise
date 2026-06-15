"""
Module 11: Exceptions
Level 0: Basic try-except
Level 1: Multiple except blocks and else/finally
Level 2: Raising and catching custom exceptions
Level 3: Real world: LLM API call with retry and rate limit handling
Level 4: Mini challenge: Robust calculator with error handling
Level 5: Production: Context manager for API resource management
"""

# ============================================================
# Level 0: Basic try-except
# ============================================================

print("=== Level 0: Basic try-except ===")

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ValueError
try:
    number = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# IndexError
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError:
    print("Index out of range!")

# TypeError
try:
    result = "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# KeyError
try:
    d = {"name": "Alice"}
    print(d["age"])
except KeyError as e:
    print(f"KeyError: missing key {e}")

# FileNotFoundError
try:
    with open("nonexistent.txt") as f:
        pass
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# ============================================================
# Level 1: Multiple except blocks and else/finally
# ============================================================

print("\n=== Level 1: Multiple except blocks and else/finally ===")


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    else:
        print(f"Division successful: {result}")
        return result
    finally:
        print("Division operation complete")


safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("10", 2)

# Grouping exceptions
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}")

# ============================================================
# Level 2: Raising and catching custom exceptions
# ============================================================

print("\n=== Level 2: Custom exceptions ===")


class ValidationError(Exception):
    """Raised when input validation fails."""
    pass


class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Insufficient funds: balance ${balance}, "
            f"needs ${amount}"
        )


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValidationError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValidationError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount


account = BankAccount("Alice", 100)

try:
    account.deposit(-50)
except ValidationError as e:
    print(f"Validation error: {e}")

try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(f"Insufficient funds: {e}")

try:
    account.deposit(50)
    account.withdraw(30)
    print(f"Balance: ${account.balance}")
except (ValidationError, InsufficientFundsError) as e:
    print(f"Error: {e}")

# ============================================================
# Level 3: Real world: LLM API call with retry and rate limit
# ============================================================

print("\n=== Level 3: LLM API call with retry and rate limit ===")

import time
import random


class RateLimitError(Exception):
    def __init__(self, retry_after=60):
        self.retry_after = retry_after
        super().__init__(f"Rate limited. Retry after {retry_after}s")


class APIKeyError(Exception):
    pass


class LLMClient:
    """Simulated LLM client with rate limiting."""

    def __init__(self, api_key=None):
        if not api_key:
            raise APIKeyError("API key is required")
        self.api_key = api_key
        self._call_count = 0

    def generate(self, prompt):
        self._call_count += 1
        # Simulate rate limit after 3 calls
        if self._call_count > 3:
            raise RateLimitError(retry_after=2)
        # Simulate random transient errors
        if random.random() < 0.2:
            raise ConnectionError("Connection reset by peer")
        return f"Response to: {prompt[:50]}..."


def call_with_retry(client, prompt, max_retries=3, base_delay=1):
    """Call LLM with exponential backoff retry logic."""
    last_exception = None

    for attempt in range(1, max_retries + 1):
        try:
            return client.generate(prompt)
        except RateLimitError as e:
            print(f"  Rate limited (attempt {attempt}). Waiting {e.retry_after}s...")
            time.sleep(e.retry_after)
        except ConnectionError as e:
            delay = base_delay * (2 ** (attempt - 1))
            print(f"  Connection error: {e}. Retrying in {delay}s...")
            time.sleep(delay)
        except APIKeyError:
            raise  # No retry for auth errors
        except Exception as e:
            print(f"  Unexpected error: {e}")
            last_exception = e
            if attempt == max_retries:
                raise

    raise RuntimeError(f"Max retries ({max_retries}) exceeded")


try:
    client = LLMClient(api_key="sk-test123")
    print("LLM Client created")

    for i in range(5):
        print(f"\nCall {i + 1}:")
        response = call_with_retry(client, f"Tell me a fact about number {i}")
        print(f"  Response: {response}")
        time.sleep(0.5)

except APIKeyError as e:
    print(f"Auth error: {e}")
except RuntimeError as e:
    print(f"Failed after retries: {e}")

# ============================================================
# Level 4: Mini challenge: Robust calculator with error handling
# ============================================================

print("\n=== Level 4: Robust calculator with error handling ===")


class CalculatorError(Exception):
    pass


class DivisionByZeroError(CalculatorError):
    pass


class InvalidOperatorError(CalculatorError):
    pass


class Calculator:
    """A calculator with robust error handling."""

    def __init__(self):
        self.history = []

    def operate(self, a, op, b):
        """Perform a calculation with error handling."""
        try:
            result = self._execute(a, op, b)
        except CalculatorError:
            raise
        except Exception as e:
            raise CalculatorError(f"Unexpected error: {e}") from e
        else:
            entry = f"{a} {op} {b} = {result}"
            self.history.append(entry)
            return result

    def _execute(self, a, op, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise CalculatorError("Operands must be numbers")

        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                raise DivisionByZeroError("Cannot divide by zero")
            return a / b
        elif op == "//":
            if b == 0:
                raise DivisionByZeroError("Cannot divide by zero")
            return a // b
        elif op == "%":
            if b == 0:
                raise DivisionByZeroError("Cannot divide by zero")
            return a % b
        elif op == "**":
            return a ** b
        else:
            raise InvalidOperatorError(f"Unknown operator: {op}")

    def show_history(self):
        if not self.history:
            print("No calculations yet")
        for entry in self.history:
            print(f"  {entry}")


calc = Calculator()

test_cases = [
    (10, "+", 5),
    (10, "/", 0),
    ("abc", "+", 5),
    (10, "^", 5),
    (10, "/", 3),
    (15, "%", 4),
    (2, "**", 10),
]

for a, op, b in test_cases:
    try:
        result = calc.operate(a, op, b)
        print(f"  {a} {op} {b} = {result}")
    except DivisionByZeroError as e:
        print(f"  Division error: {e}")
    except InvalidOperatorError as e:
        print(f"  Operator error: {e}")
    except CalculatorError as e:
        print(f"  Calculator error: {e}")

print("\nHistory:")
calc.show_history()

# ============================================================
# Level 5: Production: Context manager for API resource management
# ============================================================

print("\n=== Level 5: Context manager for API resource management ===")

import contextlib


class APISession:
    """Simulated API session with resource management."""

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self._connected = False
        self._requests = 0

    def connect(self):
        if self._connected:
            return
        print(f"  Connecting to {self.base_url}...")
        # Simulate connection
        self._connected = True
        print(f"  Connected")

    def request(self, endpoint, data=None):
        if not self._connected:
            raise RuntimeError("Session not connected. Use 'with' block.")
        self._requests += 1
        if self._requests > 3:
            raise ConnectionError("Session expired, too many requests")
        return {"status": "ok", "endpoint": endpoint, "data": data}

    def close(self):
        if not self._connected:
            return
        print(f"  Closing session. Total requests: {self._requests}")
        self._connected = False


class ManagedAPISession:
    """Context manager for API session lifecycle."""

    def __init__(self, base_url, api_key):
        self.session = APISession(base_url, api_key)

    def __enter__(self):
        self.session.connect()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        if exc_type is not None:
            print(f"  Exception occurred: {exc_type.__name__}: {exc_val}")
        return False  # Don't suppress exceptions


# Successful usage
print("\nSuccessful API session:")
try:
    with ManagedAPISession("https://api.example.com", "sk-abc123") as api:
        r1 = api.request("/chat", {"prompt": "Hello"})
        print(f"  Response 1: {r1}")
        r2 = api.request("/chat", {"prompt": "Tell me a joke"})
        print(f"  Response 2: {r2}")
except (ConnectionError, RuntimeError) as e:
    print(f"  Error: {e}")

# Using contextlib.closing for simpler cases
print("\nUsing contextlib.closing:")


class SimpleResource:
    def __init__(self, name):
        self.name = name
        print(f"  Acquired {name}")
    def process(self):
        return f"  Processing {self.name}"
    def close(self):
        print(f"  Closed {self.name}")


with contextlib.closing(SimpleResource("db-connection")) as res:
    print(res.process())

# Nested context managers
print("\nNested context managers:")
try:
    with ManagedAPISession("https://api.openai.com", "sk-key") as api:
        r = api.request("/models")
        print(f"  Models: {r}")
        with open("/tmp/api_response.json", "w") as f:
            import json
            json.dump(r, f)
        print("  Response saved")
except (ConnectionError, RuntimeError, OSError) as e:
    print(f"  Error: {e}")
