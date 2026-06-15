# Modules in Python

## Import Mechanisms

```python
import math                    # Full module
from math import sqrt           # Specific function
from math import sqrt as s      # With alias
import math as m                # Module alias
from math import *              # All names (avoid)
```

## `__name__ == "__main__"`

Every Python module has a `__name__` variable. It is `"__main__"` when the file is run directly, and the module's name when imported.

```python
# mymodule.py
def main():
    print("Running directly")

if __name__ == "__main__":
    main()  # Only runs when executed directly
```

## Creating Modules

Any `.py` file is a module. A directory with `__init__.py` becomes a **package**.

```
mypackage/
    __init__.py   # Can be empty; runs on package import
    module1.py
    module2.py
```

## Module Search Path (`sys.path`)

Python searches for modules in:
1. The directory of the script being run
2. `PYTHONPATH` environment variable directories
3. Standard library directories
4. Site-packages (third-party packages)

```python
import sys
print(sys.path)  # List of search paths
```

## Virtual Environments and pip

```bash
python -m venv venv          # Create virtual environment
source venv/bin/activate     # Activate (Linux/Mac)
pip install requests         # Install package
pip freeze > requirements.txt  # Save dependencies
pip install -r requirements.txt  # Install from file
```

## Common Standard Library Modules

| Module | Common Uses |
|--------|-------------|
| `os` | File system ops, environment variables |
| `sys` | Interpreter settings, command-line args |
| `json` | Parse/generate JSON |
| `math` | Math constants and functions |
| `datetime` | Date and time handling |
| `random` | Random number generation |
| `collections` | Specialized data structures |
| `pathlib` | Object-oriented file paths |
| `re` | Regular expressions |
| `functools` | Higher-order functions |
| `itertools` | Iterator tools |

## `os` module essentials

```python
import os
os.getcwd()       # Current directory
os.listdir(".")   # List directory contents
os.environ        # Dict of environment variables
os.path.join(a,b) # Platform-safe path joining
os.path.exists(p) # Check if path exists
```

## `pathlib` (modern alternative)

```python
from pathlib import Path
p = Path("/home/user/file.txt")
p.name       # "file.txt"
p.stem       # "file"
p.suffix     # ".txt"
p.parent     # Path("/home/user")
p.exists()   # bool
p.read_text()  # Read file content
```

## JS Comparison

| Python | JavaScript |
|--------|-----------|
| `import math` | `const math = require('math')` |
| `from math import sqrt` | `const { sqrt } = require('math')` |
| `import math as m` | `const m = require('math')` |
| `def func(): ...` | `module.exports = func` or `export` |
| `pip install` | `npm install` |
| `requirements.txt` | `package.json` / `package-lock.json` |
| `__name__ == "__main__"` | `require.main === module` |
| `sys.path` | `module.paths` / `NODE_PATH` |

## AI Relevance

- **Importing ML/NLP libraries**: `import transformers`, `import openai`, `import langchain`, `from fastapi import FastAPI`
- **Modular AI projects**: Organize prompts, model wrappers, data processing into separate modules
- **Configuration**: Load model settings, API keys via JSON config files with `json` module
- **Data handling**: `numpy`, `pandas` for data processing; `json` for structured data
- **Logging**: `import logging` for tracking model runs and debugging prompts
- **Path management**: `pathlib` for dataset paths, checkpoint directories
