"""
Modules — Exercises (Module 10)

Total: 35 exercises
  Easy: 10
  Medium: 10
  Hard: 10
  Expert: 5

Solutions are at the bottom of the file.
"""

# ============================================================
# EASY (10 exercises)
# ============================================================

# 1. Import the math module and print the value of pi.


# 2. Import sqrt from math and print sqrt of 144.


# 3. Import datetime as dt and print dt.datetime.now().


# 4. Use os.getcwd() to print the current working directory.


# 5. Use sys.version to print your Python version.


# 6. Generate a random integer between 1 and 10 (inclusive) and print it.


# 7. Parse the JSON string '{"key": "value"}' into a dict and print the dict.


# 8. Convert the dict {"name": "Python"} to a JSON string and print it.


# 9. Use pathlib.Path to create a Path object for "test.txt" and check if it exists.


# 10. Use collections.Counter to count characters in "abracadabra" and print.


# ============================================================
# MEDIUM (10 exercises)
# ============================================================

# 11. Write a function `list_files(directory)` that returns a list of filenames
#     in the given directory using os.listdir().

def list_files(directory):
    pass

# 12. Write a function `get_env_var(name)` that returns the value of an environment
#     variable or "NOT SET" if it doesn't exist.

def get_env_var(name):
    pass

# 13. Write a function `days_between(d1, d2)` that returns the number of days
#     between two date strings in "YYYY-MM-DD" format.

def days_between(d1, d2):
    pass

# 14. Write a function `roll_dice(n)` that simulates rolling n dice (1-6 each)
#     and returns the total using random.randint.

def roll_dice(n):
    pass

# 15. Write a function `load_json_file(filepath)` that loads and returns JSON
#     from a file. Return None if file not found.

def load_json_file(filepath):
    pass

# 16. Write a function `unique_words(filename)` that reads a text file and
#     returns a set of unique words.

def unique_words(filename):
    pass

# 17. Write a function `shuffle_list(items)` that returns a new shuffled list
#     without modifying the original, using random.sample.

def shuffle_list(items):
    pass

# 18. Write a function `file_extension(path)` that returns the file extension
#     using pathlib.

def file_extension(path):
    pass

# 19. Write a function `system_info()` that returns a dict with keys 'os',
#     'python_version', 'platform'.

def system_info():
    pass

# 20. Write a function `most_common_words(text, n)` that returns the n most
#     common words using collections.Counter.

def most_common_words(text, n):
    pass


# ============================================================
# HARD (10 exercises)
# ============================================================

# 21. Write a function `module_exists(module_name)` that checks if a module
#     can be imported without actually importing it (use importlib).

def module_exists(module_name):
    pass


# 22. Write a function `recursive_list_dir(path)` that recursively lists all
#     files in a directory tree using pathlib.

def recursive_list_dir(path):
    pass


# 23. Write a function `import_from_path(filepath)` that imports a Python file
#     given its absolute path (not just module name).

def import_from_path(filepath):
    pass


# 24. Write a function `timer(func, *args, **kwargs)` that measures and prints
#     the execution time of a function using time module.

def timer(func, *args, **kwargs):
    pass


# 25. Write a function `create_backup(filepath)` that copies a file with a
#     timestamp suffix using shutil and datetime.

def create_backup(filepath):
    pass


# 26. Write a function `env_table()` that prints all environment variables
#     in a formatted table (key | value).

def env_table():
    pass


# 27. Write a function `import_submodules(package_name)` that imports all
#     submodules of a package and returns them as a dict.

def import_submodules(package_name):
    pass


# 28. Write a function `random_password(length)` that generates a random
#     password with letters, digits, and special characters using string and random.

def random_password(length):
    pass


# 29. Write a function `relative_path(path1, path2)` that computes the relative
#     path from path1 to path2 using pathlib.

def relative_path(path1, path2):
    pass


# 30. Write a function `run_doctest(module_name)` that runs doctests for a
#     given module using doctest.

def run_doctest(module_name):
    pass


# ============================================================
# EXPERT (5 exercises)
# ============================================================

# 31. Write a function `lazy_import(module_name)` that imports a module only
#     when it's first accessed (lazy loading). Return a module proxy.

class LazyModule:
    pass

def lazy_import(module_name):
    pass


# 32. Write a function `find_duplicates(directory)` that finds all duplicate
#     files in a directory tree using hashlib and pathlib.

def find_duplicates(directory):
    pass


# 33. Write a function `package_tree(package_name)` that prints the dependency
#     tree of an installed package using importlib.metadata.

def package_tree(package_name):
    pass


# 34. Write a function `hot_reload(module_name)` that reloads a module and
#     all its submodules using importlib.reload.

def hot_reload(module_name):
    pass


# 35. Write a function `create_package_structure(structure_dict)` that creates
#     a package directory structure from a nested dict, creating __init__.py files.

def create_package_structure(structure_dict):
    pass


# ============================================================
# SOLUTIONS
# ============================================================

"""
=== EASY ===

# 1
import math
print(math.pi)

# 2
from math import sqrt
print(sqrt(144))

# 3
import datetime as dt
print(dt.datetime.now())

# 4
import os
print(os.getcwd())

# 5
import sys
print(sys.version)

# 6
import random
print(random.randint(1, 10))

# 7
import json
d = json.loads('{"key": "value"}')
print(d)

# 8
import json
s = json.dumps({"name": "Python"})
print(s)

# 9
from pathlib import Path
p = Path("test.txt")
print(p.exists())

# 10
from collections import Counter
print(Counter("abracadabra"))

=== MEDIUM ===

# 11
def list_files(directory):
    import os
    return os.listdir(directory)

# 12
def get_env_var(name):
    import os
    return os.environ.get(name, "NOT SET")

# 13
def days_between(d1, d2):
    from datetime import datetime
    a = datetime.strptime(d1, "%Y-%m-%d")
    b = datetime.strptime(d2, "%Y-%m-%d")
    return abs((b - a).days)

# 14
def roll_dice(n):
    import random
    return sum(random.randint(1, 6) for _ in range(n))

# 15
def load_json_file(filepath):
    import json
    import os
    if not os.path.exists(filepath):
        return None
    with open(filepath) as f:
        return json.load(f)

# 16
def unique_words(filename):
    with open(filename) as f:
        return set(f.read().split())

# 17
def shuffle_list(items):
    import random
    return random.sample(items, len(items))

# 18
def file_extension(path):
    from pathlib import Path
    return Path(path).suffix

# 19
def system_info():
    import os, sys
    return {"os": os.name, "python_version": sys.version, "platform": sys.platform}

# 20
def most_common_words(text, n):
    from collections import Counter
    return Counter(text.lower().split()).most_common(n)

=== HARD ===

# 21
def module_exists(module_name):
    import importlib
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False

# 22
def recursive_list_dir(path):
    from pathlib import Path
    return [str(p) for p in Path(path).rglob("*") if p.is_file()]

# 23
def import_from_path(filepath):
    import importlib
    import sys
    spec = importlib.util.spec_from_file_location("module", filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules["module"] = module
    spec.loader.exec_module(module)
    return module

# 24
def timer(func, *args, **kwargs):
    import time
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start
    print(f"{func.__name__} took {elapsed:.4f}s")
    return result

# 25
def create_backup(filepath):
    import shutil
    from datetime import datetime
    from pathlib import Path
    p = Path(filepath)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = p.parent / f"{p.stem}_{timestamp}{p.suffix}"
    shutil.copy2(filepath, backup)
    return str(backup)

# 26
def env_table():
    import os
    for key, value in os.environ.items():
        print(f"{key:30s} | {value}")

# 27
def import_submodules(package_name):
    import pkgutil
    import importlib
    result = {}
    package = importlib.import_module(package_name)
    for importer, modname, ispkg in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        result[modname] = importlib.import_module(modname)
    return result

# 28
def random_password(length):
    import random
    import string
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

# 29
def relative_path(path1, path2):
    from pathlib import Path
    return Path(path1).relative_to(Path(path2))

# 30
def run_doctest(module_name):
    import doctest
    import importlib
    module = importlib.import_module(module_name)
    doctest.testmod(module)

=== EXPERT ===

# 31
class LazyModule:
    def __init__(self, name):
        self._name = name
        self._module = None
    def _load(self):
        if self._module is None:
            import importlib
            self._module = importlib.import_module(self._name)
    def __getattr__(self, name):
        self._load()
        return getattr(self._module, name)

def lazy_import(module_name):
    return LazyModule(module_name)

# 32
def find_duplicates(directory):
    from pathlib import Path
    import hashlib
    hashes = {}
    for file in Path(directory).rglob("*"):
        if file.is_file():
            h = hashlib.md5(file.read_bytes()).hexdigest()
            hashes.setdefault(h, []).append(file)
    return {h: files for h, files in hashes.items() if len(files) > 1}

# 33
def package_tree(package_name):
    import importlib.metadata
    dist = importlib.metadata.distribution(package_name)
    if not dist:
        print(f"Package {package_name} not found")
        return
    requires = dist.requires or []
    for req in requires:
        print(f"  {req}")

# 34
def hot_reload(module_name):
    import importlib
    import sys
    for name in list(sys.modules.keys()):
        if name.startswith(module_name + ".") or name == module_name:
            importlib.reload(sys.modules[name])

# 35
def create_package_structure(structure_dict):
    from pathlib import Path
    def _create(current_path, structure):
        for name, content in structure.items():
            item_path = Path(current_path) / name
            if content is None:
                item_path.mkdir(parents=True, exist_ok=True)
                (item_path / "__init__.py").write_text("")
            elif isinstance(content, dict):
                item_path.mkdir(parents=True, exist_ok=True)
                (item_path / "__init__.py").write_text("")
                _create(item_path, content)
            else:
                item_path.parent.mkdir(parents=True, exist_ok=True)
                item_path.write_text(content)
    _create(".", structure_dict)
"""
