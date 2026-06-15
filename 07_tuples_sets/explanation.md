# Python Tuples and Sets

## Tuples

### Creation
Tuples are ordered, **immutable** sequences. Created with parentheses `()`.

```python
empty = ()
single = (1,)          # trailing comma required!
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14)
nested = ((1, 2), (3, 4))
```

Tuple packing (parentheses optional):
```python
point = 3, 4         # (3, 4) - tuple packing
```

### Immutability
Once created, tuples cannot be modified — no append, remove, or item assignment.

```python
t = (1, 2, 3)
# t[0] = 10  # TypeError!
```

Tuples are **hashable** (if all elements are hashable), making them usable as dict keys and set elements.

### Packing / Unpacking

```python
# Packing
coords = 10, 20, 30

# Unpacking
x, y, z = coords       # x=10, y=20, z=30

# Extended unpacking
first, *rest = (1, 2, 3, 4)     # first=1, rest=[2,3,4]
first, *middle, last = (1,2,3,4) # first=1, middle=[2,3], last=4

# Swapping
a, b = b, a
```

### When to Use Tuples
- **Fixed data**: Coordinates, RGB values, configuration constants
- **Multiple return values**: Functions return tuples by default
- **Dict keys**: Only immutable types can be dict keys
- **Set elements**: Only hashable types can be in sets
- **Named tuples**: `collections.namedtuple` for self-documenting code
- **Performance**: Slightly faster than lists due to immutability

### Tuple Methods
```python
t = (1, 2, 3, 2, 4, 2)
t.index(3)     # 2
t.count(2)     # 3
len(t)         # 6
```

## Sets

### Creation
Sets are **unordered**, **mutable** collections of **unique** elements.

```python
empty = set()                # NOT {} (that's a dict)
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14}
from_list = set([1, 2, 2, 3])  # {1, 2, 3}
```

### Uniqueness
Sets automatically eliminate duplicates.

```python
{1, 2, 2, 3, 3, 3}  # {1, 2, 3}
```

### Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b        # Union:     {1, 2, 3, 4, 5, 6}
a & b        # Intersection: {3, 4}
a - b        # Difference:   {1, 2}
a ^ b        # Symmetric difference: {1, 2, 5, 6}
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
```

### Subset / Superset

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
a.issubset(b)       # True
b.issuperset(a)     # True
a.isdisjoint({4})   # True (no common elements)
```

### Set Methods

| Method              | Description                           |
|---------------------|---------------------------------------|
| `add(x)`            | Add element x                         |
| `remove(x)`         | Remove x (KeyError if missing)        |
| `discard(x)`        | Remove x if present (no error)        |
| `pop()`             | Remove and return arbitrary element   |
| `clear()`           | Remove all elements                   |
| `copy()`            | Shallow copy                          |
| `update(s)`         | Union update (add all from s)         |
| `intersection_update(s)` | Keep only elements also in s     |
| `difference_update(s)`   | Remove elements found in s       |
| `symmetric_difference_update(s)` | Keep elements in either but not both |

```python
s = {1, 2, 3}
s.add(4)           # {1, 2, 3, 4}
s.remove(2)        # {1, 3, 4}
s.discard(10)      # no error
s.update({5, 6})   # {1, 3, 4, 5, 6}
```

### Frozensets
Immutable version of sets. Hashable, usable as dict keys.

```python
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError!
```

### Hashable Requirements
To be in a set or used as dict key, an object must be hashable:
- Immutable types are hashable: `int`, `float`, `str`, `tuple`, `frozenset`
- Mutable types are NOT hashable: `list`, `set`, `dict`
- A tuple is hashable **only if all its elements are hashable**

## JS Comparison

| Python                | JavaScript                    |
|-----------------------|-------------------------------|
| `(1, 2, 3)`           | No direct equivalent (frozen arr) |
| `a, b = (1, 2)`       | `[a, b] = [1, 2]` (destructuring) |
| `{1, 2, 3}`           | `new Set([1, 2, 3])`          |
| `s.add(x)`            | `s.add(x)`                    |
| `s.delete(x)`         | `s.delete(x)`                 |
| `len(s)`              | `s.size`                      |
| `a \| b`              | `new Set([...a, ...b])`       |
| `a & b`               | `new Set([...a].filter(x => b.has(x)))` |
| `a - b`               | `new Set([...a].filter(x => !b.has(x)))` |
| `x in s`              | `s.has(x)`                    |
| `frozenset(...)`      | No direct equivalent          |

## AI Relevance

### Tuples
- **Fixed model configurations**: Model parameters stored as immutable tuples
- **Return values**: Functions returning (tokens, probabilities) pairs
- **Coordinates**: Embedding-space coordinates as (x, y, z) tuples
- **Hashable keys**: Using tuples as dictionary keys for cached results

### Sets
- **Unique token vocabulary**: `set(tokenizer.get_vocab())`
- **Deduplication**: Removing duplicate documents in RAG results
- **Set operations for filtering**: Finding documents that match multiple criteria
- **Stop words**: Stored as sets for O(1) lookup
- **Ground truth vs predictions**: Set operations for evaluation metrics (precision, recall)
- **Vocabulary overlap**: Comparing model vocabularies using set operations
