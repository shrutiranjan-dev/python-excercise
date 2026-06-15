"""Module 05: Functions - Fill in the Blanks

Each question has a template with ____ placeholders.
Replace ____ with the correct Python code, then check your answers.
"""

import sys


QUESTIONS = [
    {
        "id": "Q1",
        "template": """
____ greet():
    return "Hello!"
result = greet()
""",
        "answer": "def",
        "expected": "Hello!",
        "hint": "Keyword to define a function",
    },
    {
        "id": "Q2",
        "template": """
def add(a, b):
    ____ a + b
result = add(3, 4)
""",
        "answer": "return",
        "expected": 7,
        "hint": "Keyword to send back a value",
    },
    {
        "id": "Q3",
        "template": """
def multiply(x, y):
    return x * y
result = multiply(4, ____)
""",
        "answer": "5",
        "expected": 20,
        "hint": "Second positional argument value",
    },
    {
        "id": "Q4",
        "template": """
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
result = greet("Bob")
""",
        "answer": "",
        "expected": "Hello, Bob!",
        "hint": "Default parameter value is 'Hello'",
    },
    {
        "id": "Q5",
        "template": """
def divide(a, b):
    return a / b
result = divide(____=10, ____=2)
""",
        "answer": "a b",
        "expected": 5.0,
        "hint": "Keyword arguments use parameter names (answer: 'a' and 'b')",
    },
    {
        "id": "Q6",
        "template": """
def sum_all(____):
    return sum(args)
result = sum_all(1, 2, 3, 4)
""",
        "answer": "*args",
        "expected": 10,
        "hint": "Variable positional arguments",
    },
    {
        "id": "Q7",
        "template": """
double = ____ x: x * 2
result = double(5)
""",
        "answer": "lambda",
        "expected": 10,
        "hint": "Lambda keyword for anonymous functions",
    },
    {
        "id": "Q8",
        "template": """
numbers = [1, 2, 3, 4, 5]
result = list(filter(____ x: x % 2 == 0, numbers))
""",
        "answer": "lambda",
        "expected": [2, 4],
        "hint": "Lambda for filter predicate",
    },
    {
        "id": "Q9",
        "template": """
def square(n):
    \"\"\"Return the ____ of n.\"\"\"
    return n ** 2
result = square.__doc__
""",
        "answer": "square",
        "expected": "Return the square of n.",
        "hint": "Docstring describes what the function does",
    },
    {
        "id": "Q10",
        "template": """
def no_return():
    pass
result = no_return()
""",
        "answer": "",
        "expected": None,
        "hint": "Functions without return return None",
    },
    {
        "id": "Q11",
        "template": """
x = 5
def my_func():
    return x
result = my_func()
""",
        "answer": "",
        "expected": 5,
        "hint": "Functions can access global variables (no blank)",
    },
    {
        "id": "Q12",
        "template": """
count = 0
def increment():
    ____ count
    count += 1
increment()
result = count
""",
        "answer": "global",
        "expected": 1,
        "hint": "Keyword to modify a global variable inside a function",
    },
    {
        "id": "Q13",
        "template": """
def outer():
    def inner():
        return "inner called"
    return ____()
result = outer()
""",
        "answer": "inner",
        "expected": "inner called",
        "hint": "Call the nested function",
    },
    {
        "id": "Q14",
        "template": """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n ____ 1)
result = factorial(5)
""",
        "answer": "-",
        "expected": 120,
        "hint": "Recursive call with decremented value",
    },
    {
        "id": "Q15",
        "template": """
def add(a: int, b: int) -> ____:
    return a + b
result = add(3, 5)
""",
        "answer": "int",
        "expected": 8,
        "hint": "Return type hint",
    },
    {
        "id": "Q16",
        "template": """
def add(a, b, c):
    return a + b + c
nums = [1, 2, 3]
result = add(*____)
""",
        "answer": "nums",
        "expected": 6,
        "hint": "Unpack the list into positional arguments",
    },
    {
        "id": "Q17",
        "template": """
def create_user(name, age):
    return f"{name} is {age} years old"
data = {"name": "Alice", "age": 30}
result = create_user(____data)
""",
        "answer": "**",
        "expected": "Alice is 30 years old",
        "hint": "Unpack dict into keyword arguments",
    },
    {
        "id": "Q18",
        "template": """
people = [("Alice", 30), ("Bob", 25)]
people.sort(key=____ p: p[1])
result = people
""",
        "answer": "lambda",
        "expected": [("Bob", 25), ("Alice", 30)],
        "hint": "Lambda for sorting by age (second element)",
    },
    {
        "id": "Q19",
        "template": """
def apply(func, value):
    return ____(value)
result = apply(lambda x: x ** 2, 5)
""",
        "answer": "func",
        "expected": 25,
        "hint": "Call the passed-in function",
    },
    {
        "id": "Q20",
        "template": """
def add_item(item, items=____):
    if items is None:
        items = []
    items.append(item)
    return items
result = add_item(1)
""",
        "answer": "None",
        "expected": [1],
        "hint": "Safe default for mutable objects is None",
    },
    {
        "id": "Q21",
        "template": """
def sum_to(n):
    if n <= 0:
        return 0
    return n + sum_to(n ____ 1)
result = sum_to(5)
""",
        "answer": "-",
        "expected": 15,
        "hint": "Recursive call with decremented value",
    },
    {
        "id": "Q22",
        "template": """
def show_info(____):
    pairs = []
    for k, v in kwargs.items():
        pairs.append(f"{k}: {v}")
    return pairs
result = show_info(name="Alice", age=30)
""",
        "answer": "**kwargs",
        "expected": ["name: Alice", "age: 30"],
        "hint": "Variable keyword arguments",
    },
    {
        "id": "Q23",
        "template": """
def min_max(numbers):
    return ____(numbers), ____(numbers)
lo, hi = min_max([3, 1, 4, 1, 5])
result = (lo, hi)
""",
        "answer": "min max",
        "expected": (1, 5),
        "hint": "Built-in functions for minimum and maximum",
    },
    {
        "id": "Q24",
        "template": """
def multiply(x, y):
    return x * y
result = multiply(y=3, x=4)
""",
        "answer": "",
        "expected": 12,
        "hint": "Keyword arguments can be in any order",
    },
    {
        "id": "Q25",
        "template": """
def make_counter():
    count = 0
    def counter():
        ____ count
        count += 1
        return count
    return counter
c = make_counter()
c()
result = c()
""",
        "answer": "nonlocal",
        "expected": 2,
        "hint": "Keyword to modify a variable in enclosing (non-global) scope",
    },
]


def run_question(q, student_answer):
    code = q["template"]
    if student_answer:
        blanks = student_answer.split()
        code = code.replace("____", blanks[0], 1)
        for b in blanks[1:]:
            code = code.replace("____", b, 1)
    ns = {}
    exec(code, ns)
    for name in ["result", "lo"]:
        if name in ns:
            return ns[name]
    return None


def check():
    passed = 0
    total = len(QUESTIONS)
    for q in QUESTIONS:
        try:
            result = run_question(q, q["answer"])
            if result == q["expected"]:
                passed += 1
            else:
                print(f'{q["id"]} FAILED: got {result!r}, expected {q["expected"]!r}')
        except Exception as e:
            print(f'{q["id"]} ERROR: {e}')
    print(f"\n{passed}/{total} passed")
    if passed == total:
        print("All correct!")


HINTS = "\n".join(f'{q["id"]}: {q["hint"]}' for q in QUESTIONS)
SOLUTIONS = "\n".join(f'{q["id"]}: {q["answer"]}' for q in QUESTIONS)


if __name__ == "__main__":
    if "--hints" in sys.argv:
        print(HINTS)
    elif "--solutions" in sys.argv:
        print(SOLUTIONS)
    else:
        check()
