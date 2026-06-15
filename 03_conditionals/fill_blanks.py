"""Module 03: Conditionals - Fill in the Blanks

Each question has a template with ____ placeholders.
Replace ____ with the correct Python code, then check your answers.
"""

import sys


QUESTIONS = [
    {
        "id": "Q1",
        "template": """
x = 10
if x ____ 5:
    result = "Greater"
else:
    result = "Not greater"
""",
        "answer": ">",
        "expected": "Greater",
        "hint": "Comparison operator for greater than",
    },
    {
        "id": "Q2",
        "template": """
age = 15
if age >= 18:
    result = "Adult"
____:
    result = "Minor"
""",
        "answer": "else",
        "expected": "Minor",
        "hint": "Fallback branch keyword",
    },
    {
        "id": "Q3",
        "template": """
temp = 30
if temp > 35:
    condition = "Very hot"
____ temp > 25:
    condition = "Warm"
else:
    condition = "Cool"
""",
        "answer": "elif",
        "expected": "Warm",
        "hint": "Python's 'else if' keyword",
    },
    {
        "id": "Q4",
        "template": """
age = 20
result = "Adult" ____ age >= 18 ____ "Minor"
""",
        "answer": "if else",
        "expected": "Adult",
        "hint": "Ternary operator: x if cond else y (answer: 'if' and 'else' with space)",
    },
    {
        "id": "Q5",
        "template": """
name = ""
if ____ name:
    result = "Empty name"
else:
    result = "Name provided"
""",
        "answer": "not",
        "expected": "Empty name",
        "hint": "Empty string is falsy; negate it",
    },
    {
        "id": "Q6",
        "template": """
count = 0
if count:
    result = "Non-zero"
else:
    result = "____"
""",
        "answer": "Zero",
        "expected": "Zero",
        "hint": "0 is falsy in Python",
    },
    {
        "id": "Q7",
        "template": """
value = None
if value is ____:
    result = "No value"
else:
    result = "Has value"
""",
        "answer": "None",
        "expected": "No value",
        "hint": "The null singleton in Python",
    },
    {
        "id": "Q8",
        "template": """
x = 7
if x ____ 5 ____ x < 10:
    result = "Between 5 and 10"
else:
    result = "Outside range"
""",
        "answer": "> and",
        "expected": "Between 5 and 10",
        "hint": "Comparison + logical AND (answer: '>' and 'and' with space)",
    },
    {
        "id": "Q9",
        "template": """
day = "Saturday"
if day ____ "Saturday" ____ day == "Sunday":
    result = "Weekend!"
else:
    result = "Weekday"
""",
        "answer": "== or",
        "expected": "Weekend!",
        "hint": "Equality + logical OR (answer: '==' and 'or' with space)",
    },
    {
        "id": "Q10",
        "template": """
logged_in = False
if ____ logged_in:
    result = "Please log in"
else:
    result = "Welcome!"
""",
        "answer": "not",
        "expected": "Please log in",
        "hint": "Negation operator",
    },
    {
        "id": "Q11",
        "template": """
fruits = ["apple", "banana", "cherry"]
if "banana" ____ fruits:
    result = "Found banana"
else:
    result = "Not found"
""",
        "answer": "in",
        "expected": "Found banana",
        "hint": "Membership test operator",
    },
    {
        "id": "Q12",
        "template": """
code = 200
____ code:
    ____ 200:
        result = "OK"
    ____ 404:
        result = "Not Found"
    ____ _:
        result = "Other"
""",
        "answer": "match case case case",
        "expected": "OK",
        "hint": "Python 3.10+ pattern matching (answer: 'match case case case' with spaces)",
    },
    {
        "id": "Q13",
        "template": """
value = "hello"
match value:
    case "hi":
        result = "Greeting"
    case ____:
        result = "Something else"
""",
        "answer": "_",
        "expected": "Something else",
        "hint": "Wildcard/default pattern in match-case",
    },
    {
        "id": "Q14",
        "template": """
x = 15
if x > 10:
    if x ____ 20:
        result = "Between 11 and 20"
    else:
        result = "Above 20"
else:
    result = "10 or below"
""",
        "answer": "<",
        "expected": "Between 11 and 20",
        "hint": "Less-than operator for upper bound",
    },
    {
        "id": "Q15",
        "template": """
score = 75
if score >= 90:
    result = "A"
____ score >= 80:
    result = "B"
____ score >= 70:
    result = "C"
____ score >= 60:
    result = "D"
____:
    result = "F"
""",
        "answer": "elif elif elif else",
        "expected": "C",
        "hint": "Four keywords: elif, elif, elif, else (space-separated)",
    },
    {
        "id": "Q16",
        "template": """
a = 5
b = 10
result = a ____ a > b ____ b
""",
        "answer": "if else",
        "expected": 10,
        "hint": "Ternary operator to pick max (answer: 'if' and 'else')",
    },
    {
        "id": "Q17",
        "template": """
items = []
if ____ items:
    result = "Has items"
else:
    result = "Empty list"
""",
        "answer": "not",
        "expected": "Has items",
        "hint": "Empty list is falsy, 'not' makes it True",
    },
    {
        "id": "Q18",
        "template": """
x = 5
if 1 ____ x ____ 10:
    result = "In range"
else:
    result = "Out of range"
""",
        "answer": "< <",
        "expected": "In range",
        "hint": "Python chained comparison: a < b < c (answer: '<' and '<')",
    },
    {
        "id": "Q19",
        "template": """
name = "Alice"
if name ____ "Bob":
    result = "Hello Bob"
else:
    result = "You're not Bob"
""",
        "answer": "==",
        "expected": "You're not Bob",
        "hint": "Equality comparison operator",
    },
    {
        "id": "Q20",
        "template": """
num = 0
if num > 0:
    result = "Positive"
____ num < 0:
    result = "Negative"
____:
    result = "Zero"
""",
        "answer": "elif else",
        "expected": "Zero",
        "hint": "elif and else keywords",
    },
    {
        "id": "Q21",
        "template": """
color = "red"
if color ____ "blue":
    result = "Not blue"
else:
    result = "Is blue"
""",
        "answer": "!=",
        "expected": "Not blue",
        "hint": "Not-equal operator",
    },
    {
        "id": "Q22",
        "template": """
x = 5
if x > 3:
    result = "A"
____ x > 4:
    result = "B"
else:
    result = "C"
""",
        "answer": "elif",
        "expected": "A",
        "hint": "elif vs if: first matching branch runs",
    },
    {
        "id": "Q23",
        "template": """
age = 18
if age ____ 18:
    result = "Exactly 18"
else:
    result = "Not 18"
""",
        "answer": "==",
        "expected": "Exactly 18",
        "hint": "Equality operator",
    },
    {
        "id": "Q24",
        "template": """
nums = [1, 2, 3]
if (n := len(nums)) ____ 0:
    result = f"Has {n} items"
else:
    result = "Empty"
""",
        "answer": ">",
        "expected": "Has 3 items",
        "hint": "Walrus operator with greater-than",
    },
    {
        "id": "Q25",
        "template": """
temperature = -5
if temperature ____ 0:
    result = "Freezing"
else:
    result = "Above freezing"
""",
        "answer": "<",
        "expected": "Freezing",
        "hint": "Less-than comparison for below zero",
    },
]


def run_question(q, student_answer):
    code = q["template"]
    blanks = student_answer.split()
    code = code.replace("____", blanks[0], 1)
    for b in blanks[1:]:
        code = code.replace("____", b, 1)
    ns = {}
    exec(code, ns)
    return ns.get("result", ns.get("condition", ns.get("result")))


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
