"""
Fill in the blanks — Modules (Module 10)

Instructions: Replace each ___ with a valid Python expression.
Hints and solutions are provided after each block.
"""

# ============================================================
# Section 1: import statements
# ============================================================

# 1. Import the entire math module
___ math

# 2. Import only sqrt from math
___ math import sqrt

# 3. Import datetime with an alias
import datetime ___ dt

# 4. Import all names from math (not recommended)
from math import ___

# ============================================================
# Section 2: __name__ guard
# ============================================================

# 5. The __name__ variable equals ___ when a script is run directly.
#    Hint: "__main__"

# 6. Write the condition to check if script is run directly:
if ___ == "___":
    print("Running directly")

# ============================================================
# Section 3: stdlib modules
# ============================================================

# 7. Get current working directory
import os
os.___()  # Hint: getcwd

# 8. List files in current directory
os.___(".")  # Hint: listdir

# 9. Join paths safely
os.path.___("folder", "file.txt")  # Hint: join

# 10. Parse JSON string
import json
data = json.___('{"name": "Alice"}')  # Hint: loads

# 11. Convert dict to JSON string
json.___({"name": "Alice"})  # Hint: dumps

# 12. Get current date and time
from datetime import ___
now = ___.now()  # Hint: datetime

# 13. Get today's date
from datetime import ___
today = ___.today()  # Hint: date

# 14. Generate random float between 0 and 1
import random
random.___()  # Hint: random

# 15. Pick random element from list
random.___([1, 2, 3])  # Hint: choice

# 16. Create a counter
from collections import ___
counts = ___("hello")  # Hint: Counter -> Counter("hello")

# ============================================================
# Section 4: sys module
# ============================================================

# 17. Get Python version
import sys
sys.___  # Hint: version

# 18. Get command line arguments
sys.___  # Hint: argv

# 19. Exit the program
sys.___(0)  # Hint: exit

# 20. Module search paths
sys.___  # Hint: path

# ============================================================
# Section 5: pathlib
# ============================================================

# 21. Create a Path object
from pathlib import ___
p = ___("/home/user/file.txt")  # Hint: Path

# 22. Get filename from path
p.___  # -> "file.txt"  (Hint: name)

# 23. Get file extension
p.___  # -> ".txt"  (Hint: suffix)

# 24. Check if path exists
p.___()  # Hint: exists

# ============================================================
# SOLUTIONS (uncomment to check)
# ============================================================

"""
1:  import
2:  from
3:  as
4:  *
5:  __main__
6:  __name__, __main__
7:  getcwd()
8:  listdir()
9:  join()
10: loads()
11: dumps()
12: datetime, datetime
13: date, date
14: random()
15: choice()
16: Counter, Counter
17: version
18: argv
19: exit()
20: path
21: Path, Path
22: name
23: suffix
24: exists()
"""
