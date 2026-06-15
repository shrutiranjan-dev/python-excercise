"""Module 04: Loops - Fill in the Blanks

Each question has a template with ____ placeholders.
Replace ____ with the correct Python code, then check your answers.
"""

import sys


QUESTIONS = [
    {
        "id": "Q1",
        "template": """
result = []
for i in ____(5):
    result.append(i)
""",
        "answer": "range",
        "expected": [0, 1, 2, 3, 4],
        "hint": "Function that generates a sequence of numbers",
    },
    {
        "id": "Q2",
        "template": """
result = []
for i in range(0, 10, ____):
    result.append(i)
""",
        "answer": "2",
        "expected": [0, 2, 4, 6, 8],
        "hint": "Step value to get even numbers",
    },
    {
        "id": "Q3",
        "template": """
items = ["a", "b", "c"]
result = ""
for item ____ items:
    result += item
""",
        "answer": "in",
        "expected": "abc",
        "hint": "Keyword for iterating over a sequence",
    },
    {
        "id": "Q4",
        "template": """
text = "ABC"
result = ""
for ch ____ text:
    result += ch.lower()
""",
        "answer": "in",
        "expected": "abc",
        "hint": "Iterating over a string",
    },
    {
        "id": "Q5",
        "template": """
d = {"x": 1, "y": 2}
keys = []
for k ____ d:
    keys.append(k)
""",
        "answer": "in",
        "expected": ["x", "y"],
        "hint": "Iterating over a dict gives keys by default",
    },
    {
        "id": "Q6",
        "template": """
d = {"a": 1, "b": 2}
pairs = []
for k, v ____ d.items():
    pairs.append((k, v))
""",
        "answer": "in",
        "expected": [("a", 1), ("b", 2)],
        "hint": "Unpacking dict items",
    },
    {
        "id": "Q7",
        "template": """
count = 0
result = []
____ count < 3:
    result.append(count)
    count += 1
""",
        "answer": "while",
        "expected": [0, 1, 2],
        "hint": "Loop that runs while condition is True",
    },
    {
        "id": "Q8",
        "template": """
result = []
for i in range(10):
    if i == 5:
        ____
    result.append(i)
""",
        "answer": "break",
        "expected": [0, 1, 2, 3, 4],
        "hint": "Exit the loop immediately",
    },
    {
        "id": "Q9",
        "template": """
result = []
for i in range(5):
    if i == 2:
        ____
    result.append(i)
""",
        "answer": "continue",
        "expected": [0, 1, 3, 4],
        "hint": "Skip to the next iteration",
    },
    {
        "id": "Q10",
        "template": """
fruits = ["apple", "banana"]
result = []
for i, fruit in ____(fruits):
    result.append(f"{i}:{fruit}")
""",
        "answer": "enumerate",
        "expected": ["0:apple", "1:banana"],
        "hint": "Function that gives index and value",
    },
    {
        "id": "Q11",
        "template": """
names = ["Alice", "Bob"]
ages = [25, 30]
pairs = []
for name, age in ____(names, ages):
    pairs.append((name, age))
""",
        "answer": "zip",
        "expected": [("Alice", 25), ("Bob", 30)],
        "hint": "Function to combine iterables in parallel",
    },
    {
        "id": "Q12",
        "template": """
result = []
for i in range(2):
    for j in range(2):
        result.append((i, j))
""",
        "answer": "",
        "expected": [(0, 0), (0, 1), (1, 0), (1, 1)],
        "hint": "Nested loops produce all combinations",
    },
    {
        "id": "Q13",
        "template": """
result = []
for i in range(3):
    result.append(i)
____:
    result.append("done")
""",
        "answer": "else",
        "expected": [0, 1, 2, "done"],
        "hint": "Runs when loop completes without break",
    },
    {
        "id": "Q14",
        "template": """
result = []
for i in range(5):
    if i == 3:
        break
    result.append(i)
else:
    result.append("done")
""",
        "answer": "",
        "expected": [0, 1, 2],
        "hint": "else does NOT run when break happens",
    },
    {
        "id": "Q15",
        "template": """
result = [x____2 for x in range(5)]
""",
        "answer": "**",
        "expected": [0, 1, 4, 9, 16],
        "hint": "Exponentiation operator",
    },
    {
        "id": "Q16",
        "template": """
result = [x for x in range(10) ____ x % 2 == 0]
""",
        "answer": "if",
        "expected": [0, 2, 4, 6, 8],
        "hint": "Keyword to add filter in list comprehension",
    },
    {
        "id": "Q17",
        "template": """
total = 0
for n in [1, 2, 3, 4, 5]:
    total ____ n
""",
        "answer": "+=",
        "expected": 15,
        "hint": "Addition assignment operator",
    },
    {
        "id": "Q18",
        "template": """
result = []
n = 0
____ True:
    if n >= 3:
        ____
    result.append(n)
    n += 1
""",
        "answer": "while break",
        "expected": [0, 1, 2],
        "hint": "Infinite loop with exit condition (answer: 'while' and 'break')",
    },
    {
        "id": "Q19",
        "template": """
result = []
for i in range(5, 0, ____):
    result.append(i)
""",
        "answer": "-1",
        "expected": [5, 4, 3, 2, 1],
        "hint": "Negative step for reverse iteration",
    },
    {
        "id": "Q20",
        "template": """
result = []
for i in range(3):
    if i == 1:
        ____
    result.append(i)
""",
        "answer": "pass",
        "expected": [0, 1, 2],
        "hint": "No-op placeholder statement",
    },
    {
        "id": "Q21",
        "template": """
result = []
n = 0
while n < 3:
    result.append(n)
    n += 1
____:
    result.append("done")
""",
        "answer": "else",
        "expected": [0, 1, 2, "done"],
        "hint": "while loop also supports else clause",
    },
    {
        "id": "Q22",
        "template": """
total = 0
matrix = [[1, 2], [3, 4]]
for row ____ matrix:
    for val ____ row:
        total += val
""",
        "answer": "in in",
        "expected": 10,
        "hint": "Two 'in' keywords for nested iteration",
    },
    {
        "id": "Q23",
        "template": """
result = list(range(10, 0, ____))
""",
        "answer": "-1",
        "expected": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "hint": "Step for counting down from 10 to 1",
    },
    {
        "id": "Q24",
        "template": """
count = 0
for _ in "hello":
    count ____ 1
""",
        "answer": "+=",
        "expected": 5,
        "hint": "Increment counter",
    },
    {
        "id": "Q25",
        "template": """
result = [i * 2 for i in range(1, 6)]
""",
        "answer": "",
        "expected": [2, 4, 6, 8, 10],
        "hint": "No blank needed - just confirm comprehension",
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
    for name in ["result", "total", "pairs", "keys", "count"]:
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
