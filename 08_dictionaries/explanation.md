# Python Dictionaries

## Creating Dicts

Dictionaries store **key-value pairs**. Keys must be hashable (immutable).

```python
empty = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
grades = dict(Alice=85, Bob=92, Charlie=78)
pairs = dict([("a", 1), ("b", 2), ("c", 3)])
mixed_keys = {1: "int", "str": "string", (1, 2): "tuple"}
```

## Accessing Values

```python
d = {"name": "Alice", "age": 30}

# Bracket notation (raises KeyError if missing)
d["name"]       # "Alice"

# .get() method (returns None or default if missing)
d.get("age")            # 30
d.get("city")           # None
d.get("city", "N/A")    # "N/A"

# .setdefault() - get value or set default if missing
d.setdefault("country", "USA")  # "USA", and d["country"] = "USA"
```

## Modifying

```python
d = {"a": 1, "b": 2}

# Update existing key
d["a"] = 10

# Add new key
d["c"] = 3

# Update multiple keys
d.update({"d": 4, "e": 5})
d.update(f=6, g=7)       # keyword args
```

## Dict Methods

| Method            | Description                                    |
|-------------------|------------------------------------------------|
| `keys()`          | View of all keys                               |
| `values()`        | View of all values                             |
| `items()`         | View of (key, value) pairs                     |
| `update(dict)`    | Merge another dict into this one               |
| `pop(key)`        | Remove key and return value (KeyError if missing) |
| `popitem()`       | Remove and return last inserted (key, value)   |
| `clear()`         | Remove all items                               |
| `copy()`          | Shallow copy                                   |
| `setdefault(k,v)` | Return d[k] if exists, else set d[k]=v and return v |
| `fromkeys(seq,v)` | Create dict from keys with default value       |
| `get(k, default)` | Return d[k] or default if missing              |

```python
d = {"x": 10, "y": 20, "z": 30}
list(d.keys())      # ['x', 'y', 'z']
list(d.values())    # [10, 20, 30]
list(d.items())     # [('x', 10), ('y', 20), ('z', 30)]

d.pop("y")          # 20, d = {"x": 10, "z": 30}
d.popitem()         # ('z', 30) (Python 3.7+: LIFO)
d.clear()           # {}

new_dict = dict.fromkeys(["a", "b", "c"], 0)  # {"a": 0, "b": 0, "c": 0}
```

## Dict Comprehension

```python
# Basic
squares = {x: x**2 for x in range(10)}

# With condition
even_squares = {x: x**2 for x in range(20) if x % 2 == 0}

# From two lists
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = {k: v for k, v in zip(keys, vals)}

# Transform values
upper = {k: k.upper() for k in ["hello", "world"]}

# Swap keys and values
original = {"a": 1, "b": 2}
swapped = {v: k for k, v in original.items()}

# Nested comprehension
matrix = {(i, j): i * j for i in range(3) for j in range(3)}

# With if-else
labels = {x: ("even" if x % 2 == 0 else "odd") for x in range(10)}
```

## Nested Dicts

```python
students = {
    "Alice": {"age": 25, "grade": "A", "subjects": ["Math", "Physics"]},
    "Bob": {"age": 23, "grade": "B", "subjects": ["Chemistry", "Biology"]},
}

students["Alice"]["age"]        # 25
students["Bob"]["subjects"][0]  # "Chemistry"
```

## defaultdict

From `collections` module — provides default values for missing keys.

```python
from collections import defaultdict

# Default value from a factory
word_count = defaultdict(int)       # default: 0
grouped = defaultdict(list)        # default: []
cache = defaultdict(lambda: None)  # default: None

# No KeyError!
word_count["hello"] += 1            # word_count = {"hello": 1}

# Grouping
data = [("fruit", "apple"), ("fruit", "banana"), ("animal", "cat")]
groups = defaultdict(list)
for category, item in data:
    groups[category].append(item)
# groups = {"fruit": ["apple", "banana"], "animal": ["cat"]}
```

## Merging Dicts (Python 3.9+)

```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

# | operator (3.9+)
merged = a | b       # {"x": 1, "y": 3, "z": 4}

# |= update operator
a |= b               # a = {"x": 1, "y": 3, "z": 4}
```

Older Python ways:
```python
{**a, **b}                          # merge with unpacking
a.copy().update(b)                  # copy + update
dict(a, **b)                        # works for string keys
```

## JS Comparison

| Python                    | JavaScript                  |
|---------------------------|-----------------------------|
| `{}`                      | `{}` (object literal)       |
| `d["key"]`                | `obj["key"]` or `obj.key`   |
| `d.get("key", default)`   | `obj?.key ?? default`       |
| `d.keys()`                | `Object.keys(obj)`          |
| `d.values()`              | `Object.values(obj)`        |
| `d.items()`               | `Object.entries(obj)`       |
| `k in d`                  | `k in obj`                  |
| `d.update(other)`         | `Object.assign(obj, other)` |
| `d.pop("key")`            | `delete obj.key` (different)|
| `dict()`                  | `new Map()`                 |
| `{k:v for k,v in ...}`    | `Object.fromEntries(...)` or `reduce` |
| `defaultdict`             | Proxy with get handler      |
| `a \| b` (3.9+)           | `{...a, ...b}`              |
| `len(d)`                  | `Object.keys(obj).length`   |
| `del d["key"]`            | `delete obj.key`            |

**Dict vs Map in JS**: Python dict is more like JS `Map` (accepts any hashable keys, maintains insertion order). JS objects only accept string/Symbol keys.

## AI Relevance

- **JSON-like data**: API responses from LLM providers are JSON objects (dicts)
- **Model configurations**: Hyperparameters stored as nested dicts
- **RAG document metadata**: Dicts storing source, date, relevance scores
- **Embedding storage**: Dict mapping doc IDs to embedding vectors
- **Agent state management**: Dicts tracking conversation state, tool calls, memory
- **Token mapping**: Dicts mapping tokens to IDs and vice versa
- **Caching**: LRU caches, memoization using dicts
- **Config files**: YAML/JSON configs loaded as dicts
- **Counters**: Word frequency, n-gram counts using `defaultdict(int)`
