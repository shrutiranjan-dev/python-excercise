# Module 12: File Handling in Python

## Core Concepts

### The `open()` Function
Python's built-in `open()` function is the primary way to work with files.

```python
file = open("filename.txt", "r")
# work with file
file.close()
```

**Always close files** or use a context manager (see below).

### File Modes
| Mode | Description |
|------|-------------|
| `"r"` | Read (default). File must exist. |
| `"w"` | Write. Creates file or truncates existing. |
| `"a"` | Append. Creates file if not exists, writes at end. |
| `"r+"` | Read and write. File must exist. |
| `"w+"` | Read and write. Creates/truncates. |
| `"x"` | Exclusive creation. Fails if file exists. |
| `"b"` | Binary mode (add to another mode, e.g. `"rb"`). |

### Reading Methods
- `read(size)` — Read entire file or `size` bytes.
- `readline()` — Read one line.
- `readlines()` — Read all lines into a list.

### Writing Methods
- `write(string)` — Write a string.
- `writelines(list)` — Write a list of strings (no newlines added).

### Context Managers (`with` Statement)
Automatically closes files even if an error occurs.

```python
with open("file.txt", "r") as f:
    content = f.read()
# file is closed here
```

### File Paths
- **Absolute**: `/home/user/data/file.txt`
- **Relative**: `../data/file.txt`
- **pathlib** (recommended):
  ```python
  from pathlib import Path
  p = Path("data") / "file.txt"
  p.read_text()
  p.write_text("hello")
  ```

### Encoding
Always specify encoding for text files:
```python
with open("file.txt", "r", encoding="utf-8") as f:
    ...
```

### CSV Handling
```python
import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

With dictionaries:
```python
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

### JSON Handling
```python
import json

# String to dict
data = json.loads('{"name": "Alice"}')

# File to dict
with open("data.json") as f:
    data = json.load(f)

# Dict to string
s = json.dumps(data, indent=2)

# Dict to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

### Binary Files
```python
with open("image.jpg", "rb") as f:
    data = f.read()
```

### `os.path` Operations
```python
import os
os.path.exists("file.txt")   # True/False
os.path.isfile("file.txt")   # True/False
os.path.isdir("folder")      # True/False
os.path.join("dir", "file")  # "dir/file"
os.path.basename("a/b.txt")  # "b.txt"
os.path.dirname("a/b.txt")   # "a"
os.path.getsize("file.txt")  # bytes
```

## JavaScript Comparison

| JavaScript | Python |
|------------|--------|
| `fs.readFileSync('f', 'utf8')` | `open('f').read()` |
| `fs.writeFileSync('f', data)` | `with open('f','w') as f: f.write(data)` |
| `JSON.parse(str)` | `json.loads(str)` |
| `JSON.stringify(obj)` | `json.dumps(obj)` |
| `fs.appendFileSync('f', data)` | `with open('f','a') as f: f.write(data)` |
| CSV parsing (no built-in) | `csv.reader` / `csv.DictReader` |
| Promises/async | Context manager (`with`) |

## AI Relevance
- **Reading training data**: Load dataset files (JSON, CSV, TXT)
- **Saving model responses**: Log LLM outputs to files
- **Logging interactions**: Track prompts and responses with timestamps
- **Configuration files**: Load model settings from JSON/YAML
- **Dataset handling**: Process training data from files
- **Conversation history**: Persist chat history between sessions
