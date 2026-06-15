"""Module 05: Functions - Exercises"""

import sys


# ===================== EASY (10) =====================

def e01_square(n: int) -> int:
    """Return n squared."""
    pass


def e02_full_name(first: str, last: str) -> str:
    """Return "first last"."""
    pass


def e03_is_adult(age: int) -> bool:
    """Return True if age >= 18."""
    pass


def e04_max_of_two(a: int, b: int) -> int:
    """Return the larger of a and b using ternary."""
    pass


def e05_count_letter(text: str, letter: str) -> int:
    """Return how many times letter appears in text."""
    pass


def e06_celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit: F = C * 9/5 + 32."""
    pass


def e07_string_length(s: str) -> int:
    """Return len(s) without using len()."""
    pass


def e08_first_last(items: list) -> tuple:
    """Return (first, last) element of items."""
    pass


def e09_sum_list(numbers: list) -> int:
    """Return sum of all numbers without using sum()."""
    pass


def e10_greet_user(name: str = "Guest") -> str:
    """Return "Welcome, {name}!". Default name is "Guest"."""
    pass


# ===================== MEDIUM (10) =====================

def m01_factorial(n: int) -> int:
    """Return n! (n factorial) using recursion."""
    pass


def m02_is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (same forwards and backwards)."""
    pass


def m03_count_vowels(text: str) -> int:
    """Return count of vowels (a, e, i, o, u) case-insensitive."""
    pass


def m04_flatten(nested: list) -> list:
    """Flatten a list of lists into a single list.
    E.g., [[1,2],[3,4]] -> [1,2,3,4]
    """
    pass


def m05_power(base: int, exp: int) -> int:
    """Return base^exp using recursion (not ** or pow())."""
    pass


def m06_merge_dicts(d1: dict, d2: dict) -> dict:
    """Merge two dicts. If keys conflict, use d2's value. Use **kwargs-style merge."""
    pass


def m07_filter_even(numbers: list) -> list:
    """Return a list of even numbers using filter() and lambda."""
    pass


def m08_sort_by_second(items: list) -> list:
    """Sort list of tuples by the second element using sorted() and lambda.
    E.g., [(1,3), (2,1)] -> [(2,1), (1,3)]
    """
    pass


def m09_once(func):
    """Return a wrapper that only allows func to be called once.
    Subsequent calls return None.
    """
    pass


def m10_timer(func):
    """Return a wrapper that prints how long func took in seconds."""
    pass


# ===================== HARD (10) =====================

def h01_deep_flatten(nested: list) -> list:
    """Flatten arbitrarily nested lists.
    E.g., [1, [2, [3, 4]], 5] -> [1, 2, 3, 4, 5]
    """
    pass


def h02_memoize(func):
    """Return a memoized version of func that caches results."""
    pass


def h03_curry(func):
    """Transform a function of N arguments into a curried function.
    E.g., add(1, 2, 3) -> curried_add(1)(2)(3)
    """
    pass


def h04_pipe(*funcs):
    """Return a function that composes all functions left-to-right.
    pipe(f, g)(x) = g(f(x))
    """
    pass


def h05_camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case.
    E.g., "helloWorld" -> "hello_world"
    """
    pass


def h06_validate_email(email: str) -> bool:
    """Return True if email has exactly one @, a domain with a dot,
    and valid characters.
    """
    pass


def h07_partial(func, *fixed_args, **fixed_kwargs):
    """Implement functools.partial manually.
    Return a new function with some arguments pre-filled.
    """
    pass


def h08_throttle(func, interval: float):
    """Return a wrapper that only calls func at most once per `interval` seconds."""
    pass


def h09_retry(max_attempts: int = 3, delay: float = 1.0):
    """Return a decorator that retries the function up to max_attempts times
    if it raises an exception, waiting `delay` seconds between retries.
    """
    pass


def h10_function_composition(*funcs):
    """Return the composition of all functions (right-to-left).
    compose(f, g)(x) = f(g(x))
    """
    pass


# ===================== EXPERT (5) =====================

def x01_lru_cache(maxsize: int = 128):
    """Implement an LRU cache decorator.
    When cache exceeds maxsize, evict the least recently used item.
    """
    pass


def x02_async_rate_limiter(max_calls: int, period: float):
    """Return a decorator that limits a function to max_calls per period seconds.
    Can be applied to both sync and async functions.
    """
    pass


def x03_dependency_injection(container: dict):
    """Return a decorator that injects dependencies from container into
    function parameters based on type hints or parameter names.
    """
    pass


def x04_pattern_matching_dispatch():
    """Implement a simple multi-method dispatcher using match-case.
    dispatch("int", "int")(add) -> handles (int, int)
    dispatch("str", "str")(concat) -> handles (str, str)
    """
    pass


def x05_monadic_bind(value, func):
    """Implement a simple Maybe monad bind.
    If value is None, return None.
    Otherwise, return func(value).
    """
    pass


# ===================== TEST RUNNER =====================

def test():
    tests = {
        "e01_square": [(5, 25), (0, 0), (-3, 9)],
        "e02_full_name": [("John", "Doe", "John Doe")],
        "e03_is_adult": [(18, True), (17, False), (21, True)],
        "e04_max_of_two": [(3, 7, 7), (10, 2, 10)],
        "e05_count_letter": [("hello", "l", 2), ("world", "z", 0)],
        "e06_celsius_to_fahrenheit": [(0, 32.0), (100, 212.0)],
        "e07_string_length": [("hello", 5), ("", 0)],
        "e08_first_last": [([1, 2, 3], (1, 3)), (["a"], ("a", "a"))],
        "e09_sum_list": [([1, 2, 3, 4, 5], 15), ([], 0)],
        "e10_greet_user": [("Alice", "Welcome, Alice!"), (None, "Welcome, Guest!")],
        "m01_factorial": [(5, 120), (0, 1), (1, 1)],
        "m02_is_palindrome": [("racecar", True), ("hello", False), ("", True)],
        "m03_count_vowels": [("hello", 2), ("AEIOU", 5), ("xyz", 0)],
        "m04_flatten": [([[1, 2], [3, 4]], [1, 2, 3, 4]), ([], [])],
        "m05_power": [(2, 3, 8), (5, 0, 1), (3, 2, 9)],
        "m06_merge_dicts": [({"a": 1}, {"b": 2}, {"a": 1, "b": 2}), ({"a": 1}, {"a": 2}, {"a": 2})],
        "m07_filter_even": [([1, 2, 3, 4, 5, 6], [2, 4, 6])],
        "m08_sort_by_second": [([(1, 3), (2, 1), (3, 2)], [(2, 1), (3, 2), (1, 3)])],
    }

    passed = 0
    total = 0
    func_map = {k: v for k, v in globals().items() if k.startswith(("e0", "m0", "h0", "x0"))}

    for name, cases in tests.items():
        func = func_map.get(name)
        if func is None:
            continue
        for case in cases:
            total += 1
            if name == "e10_greet_user" and case[0] is None:
                *args, expected = case
                args = ()
            else:
                *args, expected = case
            try:
                result = func(*args)
                if result == expected:
                    passed += 1
                else:
                    print(f"{name}({', '.join(repr(a) for a in args)}) = {result!r}, expected {expected!r}")
            except Exception as e:
                print(f"{name} ERROR: {e}")

    print(f"\n=== {passed}/{total} passed ===")
    if passed == total:
        print("All exercises complete!")
    return passed == total


# ===================== SOLUTIONS =====================

def e01_square_solution(n):
    return n * n


def e02_full_name_solution(first, last):
    return f"{first} {last}"


def e03_is_adult_solution(age):
    return age >= 18


def e04_max_of_two_solution(a, b):
    return a if a > b else b


def e05_count_letter_solution(text, letter):
    count = 0
    for ch in text:
        if ch == letter:
            count += 1
    return count


def e06_celsius_to_fahrenheit_solution(c):
    return c * 9 / 5 + 32


def e07_string_length_solution(s):
    count = 0
    for _ in s:
        count += 1
    return count


def e08_first_last_solution(items):
    return items[0], items[-1]


def e09_sum_list_solution(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def e10_greet_user_solution(name="Guest"):
    return f"Welcome, {name}!"


def m01_factorial_solution(n):
    if n <= 1:
        return 1
    return n * m01_factorial_solution(n - 1)


def m02_is_palindrome_solution(s):
    return s == s[::-1]


def m03_count_vowels_solution(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


def m04_flatten_solution(nested):
    result = []
    for sublist in nested:
        for item in sublist:
            result.append(item)
    return result


def m05_power_solution(base, exp):
    if exp == 0:
        return 1
    return base * m05_power_solution(base, exp - 1)


def m06_merge_dicts_solution(d1, d2):
    return {**d1, **d2}


def m07_filter_even_solution(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def m08_sort_by_second_solution(items):
    return sorted(items, key=lambda x: x[1])


def m09_once_solution(func):
    called = False
    def wrapper(*args, **kwargs):
        nonlocal called
        if called:
            return None
        called = True
        return func(*args, **kwargs)
    return wrapper


def m10_timer_solution(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


def h01_deep_flatten_solution(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(h01_deep_flatten_solution(item))
        else:
            result.append(item)
    return result


def h02_memoize_solution(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


def h03_curry_solution(func):
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more: curried(*args, *more)
    return curried


def h04_pipe_solution(*funcs):
    def wrapper(x):
        result = x
        for f in funcs:
            result = f(result)
        return result
    return wrapper


def h05_camel_to_snake_solution(name):
    result = ""
    for ch in name:
        if ch.isupper():
            if result:
                result += "_"
            result += ch.lower()
        else:
            result += ch
    return result


def h06_validate_email_solution(email):
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True


def h07_partial_solution(func, *fixed_args, **fixed_kwargs):
    def wrapper(*args, **kwargs):
        all_kwargs = {**fixed_kwargs, **kwargs}
        return func(*fixed_args, *args, **all_kwargs)
    return wrapper


def h08_throttle_solution(func, interval):
    import time
    last_called = 0.0
    def wrapper(*args, **kwargs):
        nonlocal last_called
        now = time.time()
        if now - last_called < interval:
            return None
        last_called = now
        return func(*args, **kwargs)
    return wrapper


def h09_retry_solution(max_attempts=3, delay=1.0):
    import time
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator


def h10_function_composition_solution(*funcs):
    from functools import reduce
    def compose_two(f, g):
        return lambda x: f(g(x))
    return reduce(compose_two, funcs, lambda x: x)


def x01_lru_cache_solution(maxsize=128):
    from collections import OrderedDict
    def decorator(func):
        cache = OrderedDict()
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result
        return wrapper
    return decorator


def x02_async_rate_limiter_solution(max_calls, period):
    import time
    import asyncio
    calls = []
    def decorator(func):
        import inspect
        is_async = inspect.iscoroutinefunction(func)
        if is_async:
            async def async_wrapper(*args, **kwargs):
                now = time.time()
                calls[:] = [t for t in calls if now - t < period]
                if len(calls) >= max_calls:
                    wait = calls[0] + period - now
                    await asyncio.sleep(wait)
                calls.append(time.time())
                return await func(*args, **kwargs)
            return async_wrapper
        else:
            def sync_wrapper(*args, **kwargs):
                now = time.time()
                calls[:] = [t for t in calls if now - t < period]
                if len(calls) >= max_calls:
                    wait = calls[0] + period - now
                    time.sleep(wait)
                calls.append(time.time())
                return func(*args, **kwargs)
            return sync_wrapper
    return decorator


def x03_dependency_injection_solution(container):
    import inspect
    def decorator(func):
        sig = inspect.signature(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind_partial(*args, **kwargs)
            for name, param in sig.parameters.items():
                if name not in bound.arguments and name in container:
                    kwargs[name] = container[name]
            return func(*args, **kwargs)
        return wrapper
    return decorator


def x04_pattern_matching_dispatch_solution():
    registry = {}
    def dispatch(type1, type2):
        def register(func):
            registry[(type1, type2)] = func
            return func
        return register

    def call(arg1, arg2):
        key = (type(arg1).__name__, type(arg2).__name__)
        if key in registry:
            return registry[key](arg1, arg2)
        raise TypeError(f"No handler for {key}")
    return dispatch, call


def x05_monadic_bind_solution(value, func):
    if value is None:
        return None
    return func(value)


if __name__ == "__main__":
    if "--solutions" in sys.argv:
        print("Solutions are defined in this file with _solution suffix.")
    else:
        test()
