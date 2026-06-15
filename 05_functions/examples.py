"""Module 05: Functions - Examples"""

# ---------------------------------------------------------------
# Level 0: Basic function
# ---------------------------------------------------------------
def greet():
    print("Hello, World!")

greet()


# ---------------------------------------------------------------
# Level 1: Parameters and return values
# ---------------------------------------------------------------
def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

print(add(3, 7))
print(is_even(10))


# ---------------------------------------------------------------
# Level 2: Default and keyword arguments
# ---------------------------------------------------------------
def create_profile(name, age, city="Unknown", occupation="Unemployed"):
    return {
        "name": name,
        "age": age,
        "city": city,
        "occupation": occupation,
    }

profile = create_profile("Alice", 30, city="NYC")
print(profile)

def log_message(*messages, level="INFO"):
    for msg in messages:
        print(f"[{level}] {msg}")

log_message("Server started", "Loading config", level="DEBUG")


# ---------------------------------------------------------------
# Level 3: Prompt template function with variable injection
# ---------------------------------------------------------------
def render_prompt(template: str, **kwargs) -> str:
    """Simple template renderer for prompts.
    Replaces {{variable}} placeholders with provided kwargs.
    """
    result = template
    for key, value in kwargs.items():
        placeholder = "{{" + key + "}}"
        result = result.replace(placeholder, str(value))
    return result

prompt_template = """
You are a {role} assistant.
User question: {{question}}
Context: {{context}}
Please provide a {{style}} answer.
"""

prompt = render_prompt(
    prompt_template,
    role="coding expert",
    question="What is recursion?",
    context="Python programming",
    style="concise",
)
print(prompt)


# ---------------------------------------------------------------
# Level 4: Recursive Fibonacci with memoization
# ---------------------------------------------------------------
def make_fibonacci():
    cache = {0: 0, 1: 1}

    def fib(n: int) -> int:
        if n in cache:
            return cache[n]
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib

fib = make_fibonacci()
print(f"fib(10) = {fib(10)}")
print(f"fib(50) = {fib(50)}")


# ---------------------------------------------------------------
# Level 5: Rate-limited API wrapper with retry logic
# ---------------------------------------------------------------
import time
import random

class RateLimitExceeded(Exception):
    pass

class APIClient:
    def __init__(self, max_retries=3, rate_limit_per_sec=2):
        self.max_retries = max_retries
        self.min_interval = 1.0 / rate_limit_per_sec
        self.last_call = 0.0

    def _wait_if_needed(self):
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)

    def call(self, endpoint: str, payload: dict = None) -> dict:
        for attempt in range(1, self.max_retries + 1):
            try:
                self._wait_if_needed()
                self.last_call = time.time()

                response = self._make_request(endpoint, payload)
                return response

            except RateLimitExceeded:
                wait = 2 ** attempt
                print(f"Rate limited. Retrying in {wait}s... (attempt {attempt})")
                time.sleep(wait)
            except Exception as e:
                if attempt == self.max_retries:
                    raise
                print(f"Error: {e}. Retrying... (attempt {attempt})")
                time.sleep(1)

        raise Exception("Max retries exceeded")

    def _make_request(self, endpoint, payload):
        if random.random() < 0.3:
            raise RateLimitExceeded("Too many requests")
        return {"status": "ok", "data": {"endpoint": endpoint, "payload": payload}}

client = APIClient(max_retries=3, rate_limit_per_sec=2)
for _ in range(3):
    result = client.call("/api/generate", {"prompt": "Hello"})
    print(f"Response: {result}")
