# Module 04: Loops

## What Are Loops?
Loops let you repeat code multiple times. Python has two main loop types: `for` and `while`.

---

## 1. `for` Loop

### Over a `range()`
```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)
```
- `range(stop)` — 0 to stop-1
- `range(start, stop)` — start to stop-1
- `range(start, stop, step)` — with custom step

### Over a List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Over a String
```python
for char in "hello":
    print(char)  # h, e, l, l, o
```

### Over a Dictionary
```python
person = {"name": "Alice", "age": 30}
for key in person:           # keys
    print(key, person[key])
for key, val in person.items():  # key-value pairs
    print(key, val)
```

### JavaScript Comparison
| JavaScript | Python |
|---|---|
| `for (let i=0; i<n; i++)` | `for i in range(n):` |
| `for (let x of arr)` | `for x in arr:` |
| `for (let key in obj)` | `for key in dict:` |
| `arr.forEach(fn)` | No direct equivalent |

---

## 2. `while` Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

Runs **while** the condition is `True`. Be careful of infinite loops!

---

## 3. `break`, `continue`, `pass`

```python
for i in range(10):
    if i == 3:
        continue    # skip this iteration
    if i == 7:
        break       # exit loop entirely
    print(i)
```
- `pass` — does nothing (placeholder)

---

## 4. `enumerate()`
Get both index and value:
```python
for i, fruit in enumerate(["a", "b", "c"]):
    print(i, fruit)  # 0 a, 1 b, 2 c
```

---

## 5. `zip()`
Iterate over multiple sequences in parallel:
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(name, score)
```

---

## 6. Nested Loops

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

## 7. `else` Clause on Loops

The `else` block runs **only if** the loop completed without hitting `break`:
```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x} * {n//x}")
            break
    else:
        print(f"{n} is prime")
```

---

## 8. List Comprehensions (Introduction)

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

---

## AI Relevance

- **Batch processing**: Process inference requests in batches
- **Token processing loops**: Iterate over token sequences
- **Pagination**: Loop through paginated API responses
- **Dataset iteration**: Loop through training data epochs

```python
responses = []
for batch in get_batches(dataset, batch_size=32):
    outputs = model(batch)
    responses.extend(outputs)
```
