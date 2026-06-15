"""
Python Dictionaries - Examples
Level 0-5: From basics to production-ready code.
Run: python examples.py
"""

print("=" * 60)
print("LEVEL 0: Basic Dict Creation")
print("=" * 60)

# Creating dictionaries
empty = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
grades = dict(Alice=85, Bob=92, Charlie=78)
pairs = dict([("a", 1), ("b", 2), ("c", 3)])
mixed = {1: "int", "str": "string", (1, 2): "tuple"}

print(f"Empty dict: {empty}")
print(f"Person: {person}")
print(f"Grades: {grades}")
print(f"Pairs: {pairs}")
print(f"Mixed keys: {mixed}")

# Accessing
print(f"\nperson['name']: {person['name']}")
print(f"person.get('age'): {person.get('age')}")
print(f"person.get('country', 'N/A'): {person.get('country', 'N/A')}")

# in operator
print(f"\n'name' in person: {'name' in person}")
print(f"'country' in person: {'country' in person}")

print("\n" + "=" * 60)
print("LEVEL 1: Dict Methods (keys, values, items, get)")
print("=" * 60)

d = {"name": "Alice", "age": 30, "city": "New York", "job": "Engineer"}
print(f"Dict: {d}")

# keys, values, items
print(f"\n.keys(): {d.keys()}")
print(f".values(): {d.values()}")
print(f".items(): {d.items()}")

# Convert to lists
print(f"\nlist(keys): {list(d.keys())}")
print(f"list(values): {list(d.values())}")
print(f"list(items): {list(d.items())}")

# Modifying
d["age"] = 31
print(f"\nAfter d['age'] = 31: {d}")

d["country"] = "Canada"
print(f"After d['country'] = 'Canada': {d}")

d.update({"job": "Senior Engineer", "salary": 100000})
print(f"After update: {d}")

# Removing
salary = d.pop("salary")
print(f"\nPopped 'salary': {salary}, dict: {d}")

last = d.popitem()
print(f"Popped item: {last}, dict: {d}")

# setdefault
result = d.setdefault("phone", "N/A")
print(f"\nsetdefault('phone', 'N/A'): {result}, dict: {d}")

# fromkeys
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(f"\nfromkeys: {default_dict}")

# copy
d_copy = d.copy()
print(f"Copy: {d_copy}")

print("\n" + "=" * 60)
print("LEVEL 2: Dict Comprehension")
print("=" * 60)

# Basic
squares = {x: x**2 for x in range(10)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(20) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From two lists
keys = ["a", "b", "c", "d"]
vals = [1, 2, 3, 4]
zipped = {k: v for k, v in zip(keys, vals)}
print(f"Zipped: {zipped}")

# Transform values
upper = {k: k.upper() for k in ["hello", "world", "python"]}
print(f"Upper: {upper}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# Nested comprehension
matrix = {(i, j): i * j for i in range(3) for j in range(3)}
print(f"Matrix: {matrix}")

# If-else in expression
labels = {x: ("even" if x % 2 == 0 else "odd") for x in range(10)}
print(f"Labels: {labels}")

# Filter keys
filtered = {k: v for k, v in original.items() if v > 1}
print(f"Filtered (value > 1): {filtered}")

print("\n" + "=" * 60)
print("LEVEL 3: API Response Parsing for LLM")
print("=" * 60)

import json

class LLMResponseParser:
    """Parse and validate LLM API responses."""

    @staticmethod
    def parse_chat_response(response_dict):
        """Parse a chat completion response."""
        if "error" in response_dict:
            raise ValueError(f"API Error: {response_dict['error']}")

        choices = response_dict.get("choices", [])
        if not choices:
            raise ValueError("No choices in response")

        choice = choices[0]
        message = choice.get("message", {})
        content = message.get("content", "")

        result = {
            "content": content,
            "role": message.get("role", "assistant"),
            "finish_reason": choice.get("finish_reason", "unknown"),
            "model": response_dict.get("model", "unknown"),
            "usage": response_dict.get("usage", {}),
        }
        return result

    @staticmethod
    def extract_tool_calls(response_dict):
        """Extract function/tool calls from response."""
        choices = response_dict.get("choices", [])
        if not choices:
            return []
        message = choices[0].get("message", {})
        return message.get("tool_calls", [])

    @staticmethod
    def parse_streaming_chunk(chunk_dict):
        """Parse a single streaming chunk."""
        choices = chunk_dict.get("choices", [])
        if not choices:
            return {}
        delta = choices[0].get("delta", {})
        finish = choices[0].get("finish_reason")
        result = {"content": delta.get("content", ""), "finished": finish is not None}
        if finish:
            result["finish_reason"] = finish
        return result

    @staticmethod
    def build_request(messages, model="gpt-4", temperature=0.7, max_tokens=1000):
        """Build a request dict from messages."""
        return {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

    @staticmethod
    def merge_streaming_chunks(chunks):
        """Merge streaming chunks into full response."""
        full_content = ""
        for chunk in chunks:
            full_content += chunk.get("content", "")
        return full_content


response = {
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677858242,
    "model": "gpt-4",
    "choices": [{
        "index": 0,
        "message": {
            "role": "assistant",
            "content": "Python lists are ordered, mutable sequences."
        },
        "finish_reason": "stop"
    }],
    "usage": {
        "prompt_tokens": 50,
        "completion_tokens": 10,
        "total_tokens": 60
    }
}

parsed = LLMResponseParser.parse_chat_response(response)
for key, value in parsed.items():
    if isinstance(value, dict):
        print(f"{key}: {json.dumps(value, indent=2)}")
    else:
        print(f"{key}: {value}")

request = LLMResponseParser.build_request(
    [{"role": "user", "content": "Explain lists"}]
)
print(f"\nBuilt request: {json.dumps(request, indent=2)}")

print("\n" + "=" * 60)
print("LEVEL 4: Nested Config Merge")
print("=" * 60)

class ConfigManager:
    """Deep merge nested config dictionaries."""

    @staticmethod
    def deep_merge(base, override):
        """Deep merge two dicts. override takes precedence."""
        result = base.copy()
        for key, value in override.items():
            if (key in result and isinstance(result[key], dict)
                    and isinstance(value, dict)):
                result[key] = ConfigManager.deep_merge(result[key], value)
            else:
                result[key] = value
        return result

    @staticmethod
    def flatten(nested_dict, parent_key="", sep="."):
        """Flatten nested dict into dot-separated keys."""
        items = []
        for key, value in nested_dict.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.extend(ConfigManager.flatten(value, new_key, sep=sep).items())
            else:
                items.append((new_key, value))
        return dict(items)

    @staticmethod
    def unflatten(flat_dict, sep="."):
        """Unflatten dot-separated keys into nested dict."""
        result = {}
        for key, value in flat_dict.items():
            parts = key.split(sep)
            current = result
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]
            current[parts[-1]] = value
        return result

    @staticmethod
    def diff(a, b, path=""):
        """Find differences between two configs."""
        diffs = []
        all_keys = set(a.keys()) | set(b.keys())
        for key in sorted(all_keys):
            new_path = f"{path}.{key}" if path else key
            if key not in a:
                diffs.append(("added", new_path, b[key]))
            elif key not in b:
                diffs.append(("removed", new_path, a[key]))
            elif isinstance(a[key], dict) and isinstance(b[key], dict):
                diffs.extend(ConfigManager.diff(a[key], b[key], new_path))
            elif a[key] != b[key]:
                diffs.append(("changed", new_path, a[key], b[key]))
        return diffs


default_config = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 1000,
    "stream": False,
    "retry": {
        "max_retries": 3,
        "backoff_factor": 1.5,
    }
}

user_config = {
    "model": "gpt-4",
    "temperature": 0.5,
    "retry": {
        "max_retries": 5,
    },
    "timeout": 30,
}

merged = ConfigManager.deep_merge(default_config, user_config)
print("Default config:", default_config)
print("User config:", user_config)
print("Merged config:", merged)

flat = ConfigManager.flatten(merged)
print(f"\nFlattened: {flat}")

unflattened = ConfigManager.unflatten(flat)
print(f"Unflattened: {unflattened}")

diffs = ConfigManager.diff(default_config, user_config)
print(f"\nDifferences:")
for diff_item in diffs:
    print(f"  {diff_item}")

print("\n" + "=" * 60)
print("LEVEL 5: LRU Cache Implementation")
print("=" * 60)

from collections import OrderedDict

class LRUCache:
    """Least Recently Used (LRU) Cache implementation."""

    def __init__(self, capacity=128):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.hits = 0
        self.misses = 0

    def get(self, key):
        """Get value for key. Returns None if not found."""
        if key not in self.cache:
            self.misses += 1
            return None
        self.hits += 1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """Insert or update key-value pair."""
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def delete(self, key):
        """Remove key from cache."""
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        """Clear all cached items."""
        self.cache.clear()
        self.hits = 0
        self.misses = 0

    def get_stats(self):
        """Return cache statistics."""
        total = self.hits + self.misses
        hit_rate = self.hits / total if total > 0 else 0
        return {
            "size": len(self.cache),
            "capacity": self.capacity,
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": round(hit_rate, 4),
        }

    def __contains__(self, key):
        return key in self.cache

    def __len__(self):
        return len(self.cache)

    def __repr__(self):
        return f"LRUCache(capacity={self.capacity}, size={len(self.cache)})"


class TokenCache(LRUCache):
    """Specialized LRU cache for token lookups."""

    def __init__(self, capacity=1024):
        super().__init__(capacity)

    def batch_get(self, keys):
        """Get multiple keys at once."""
        return {key: self.get(key) for key in keys}

    def batch_put(self, items):
        """Insert multiple key-value pairs."""
        for key, value in items:
            self.put(key, value)

    def get_or_compute(self, key, compute_fn):
        """Get from cache or compute and store."""
        result = self.get(key)
        if result is None:
            result = compute_fn(key)
            self.put(key, result)
        return result


cache = LRUCache(capacity=3)

cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print(f"Cache after puts: {dict(cache.cache)}")

print(f"get('a'): {cache.get('a')}")
print(f"Cache after get('a'): {dict(cache.cache)}")

cache.put("d", 4)
print(f"After put('d',4): {dict(cache.cache)}")
print(f"get('b'): {cache.get('b')}")

print(f"\nStats: {cache.get_stats()}")

# TokenCache example
token_cache = TokenCache(capacity=5)

def expensive_tokenize(text):
    return f"<tokens_for_{text}>"

for text in ["hello", "world", "hello", "python", "cache", "hello", "world"]:
    result = token_cache.get_or_compute(text, expensive_tokenize)
    print(f"  '{text}' -> {result}")

print(f"\nToken cache stats: {token_cache.get_stats()}")

print("\nAll examples completed successfully!")
