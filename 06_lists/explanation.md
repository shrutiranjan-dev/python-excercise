# Python Lists

## Creating Lists

Lists are ordered, mutable sequences. Created with square brackets `[]`.

```python
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]
```

Can also use `list()` constructor:
```python
list("abc")     # ['a', 'b', 'c']
list(range(5))  # [0, 1, 2, 3, 4]
```

## Indexing (Positive / Negative)

| Positive | 0 | 1 | 2 | 3 | 4 |
|----------|---|---|---|---|---|
| Value    | a | b | c | d | e |
| Negative  |-5 |-4 |-3 |-2 |-1 |

```python
nums = [10, 20, 30, 40, 50]
nums[0]    # 10
nums[-1]   # 50
nums[-3]   # 30
```

## Slicing

Syntax: `list[start:stop:step]`

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[2:5]     # [2, 3, 4]
nums[:4]      # [0, 1, 2, 3]
nums[4:]      # [4, 5, 6, 7, 8, 9]
nums[::2]     # [0, 2, 4, 6, 8]
nums[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
nums[-3:]     # [7, 8, 9]
nums[:-3]     # [0, 1, 2, 3, 4, 5, 6]
```

## Common Methods

| Method      | Description                                      |
|-------------|--------------------------------------------------|
| `append(x)` | Adds x to end                                    |
| `extend(it)`| Adds all items from iterable                     |
| `insert(i,x)`| Inserts x at index i                            |
| `remove(x)` | Removes first occurrence of x                    |
| `pop(i)`    | Removes & returns item at i (default last)       |
| `clear()`   | Removes all items                                |
| `index(x)`  | Returns index of first occurrence                |
| `count(x)`  | Counts occurrences of x                          |
| `sort()`    | Sorts in place                                   |
| `reverse()` | Reverses in place                                |
| `copy()`    | Returns shallow copy                             |

```python
lst = [1, 2, 3]
lst.append(4)           # [1, 2, 3, 4]
lst.extend([5, 6])      # [1, 2, 3, 4, 5, 6]
lst.insert(0, 0)        # [0, 1, 2, 3, 4, 5, 6]
lst.remove(3)           # [0, 1, 2, 4, 5, 6]
popped = lst.pop()      # popped=6, lst=[0,1,2,4,5]
idx = lst.index(4)      # 3
cnt = lst.count(2)      # 1
lst.sort(reverse=True)  # [5, 4, 2, 1, 0]
lst.reverse()           # [0, 1, 2, 4, 5]
new = lst.copy()        # shallow copy
lst.clear()             # []
```

## List Comprehension

Full coverage — the most Pythonic way to create lists.

**Basic syntax:** `[expression for item in iterable if condition]`

```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested loop
pairs = [(x, y) for x in range(3) for y in range(3)]

# With if-else expression
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]

# Flatten nested list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]  # [1,2,3,4,5,6]

# With function call
words = ["hello", "world", "python"]
lengths = [len(w) for w in words]

# Nested list comprehension (matrix transpose)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(3)]
```

## Nested Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[1][2]  # 6
```

## List as Stack / Queue

**Stack** (LIFO) — use `append()` / `pop()`:
```python
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # 2
```

**Queue** (FIFO) — use `collections.deque` for efficiency:
```python
from collections import deque
queue = deque(["a", "b", "c"])
queue.append("d")
queue.popleft()  # 'a'
```

## len() and 'in' Operator

```python
len([1, 2, 3])       # 3
3 in [1, 2, 3]       # True
10 not in [1, 2, 3]  # True
```

## JS Comparison

| Python              | JavaScript             |
|---------------------|------------------------|
| `[]`                | `[]` or `Array()`      |
| `lst.append(x)`     | `arr.push(x)`          |
| `lst.pop()`         | `arr.pop()`            |
| `lst.pop(i)`        | `arr.splice(i, 1)`     |
| `lst.insert(i, x)`  | `arr.splice(i, 0, x)`  |
| `lst.extend(it)`    | `arr.push(...it)`      |
| `lst.remove(x)`     | `splice(indexOf(x),1)` |
| `lst.sort()`        | `arr.sort()`           |
| `lst.copy()`        | `[...arr]` or `slice()`|
| `[x**2 for x in lst]` | `lst.map(x => x**2)` |
| `[x for x in lst if x>0]` | `lst.filter(x => x>0)` |
| `lst[i:j]`          | `arr.slice(i, j)`      |
| `lst[::-1]`         | `[...arr].reverse()`   |
| `len(lst)`          | `arr.length`           |
| `x in lst`          | `arr.includes(x)`      |

## AI Relevance

- **Storing sequence data**: Tokens, embeddings, feature vectors as lists
- **Batch processing**: Lists of items for parallel API calls
- **Conversation history**: Maintaining chat message history as list of dicts
- **Dataset management**: Training/validation/test splits as list indices
- **Sliding windows**: Context windows for LLM processing using slicing
- **Gradients & weights**: Stored as lists (or arrays) in ML models
