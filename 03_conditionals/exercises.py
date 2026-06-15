"""Module 03: Conditionals - Exercises"""

# Instructions: Implement each function below.
# Run `pytest exercises.py` or `python exercises.py` to test.
# Solutions are at the bottom of the file.

import sys


# ===================== EASY (10) =====================

def e01_is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    pass


def e02_is_positive(n: int) -> str:
    """Return "Positive", "Negative", or "Zero"."""
    pass


def e03_max_of_two(a: int, b: int) -> int:
    """Return the larger of a and b."""
    pass


def e04_absolute(n: int) -> int:
    """Return the absolute value of n (without using abs())."""
    pass


def e05_is_vowel(char: str) -> bool:
    """Return True if char is a vowel (a, e, i, o, u). Case-insensitive."""
    pass


def e06_can_vote(age: int) -> bool:
    """Return True if age >= 18."""
    pass


def e07_is_leap_year(year: int) -> bool:
    """Return True if year is a leap year.
    Leap years: divisible by 4, but not by 100 unless also by 400.
    """
    pass


def e08_smallest_of_three(a: int, b: int, c: int) -> int:
    """Return the smallest of three numbers."""
    pass


def e09_ends_with_s(word: str) -> bool:
    """Return True if word ends with 's' (case-sensitive)."""
    pass


def e10_is_long_string(s: str) -> bool:
    """Return True if len(s) > 10."""
    pass


# ===================== MEDIUM (10) =====================

def m01_number_to_word(n: int) -> str:
    """Convert 1-5 to words: 1->"One", 2->"Two", etc. Use match-case.
    Return "Unknown" for other numbers.
    """
    pass


def m02_temperature_category(celsius: float) -> str:
    """Return:
    "Freezing" if < 0,
    "Cold" if 0-15,
    "Warm" if 15-30,
    "Hot" if > 30.
    """
    pass


def m03_bmi_category(weight_kg: float, height_m: float) -> str:
    """BMI = weight / height^2.
    Return "Underweight" (<18.5), "Normal" (18.5-25), "Overweight" (25-30),
    "Obese" (>=30).
    """
    pass


def m04_days_in_month(month: int, year: int) -> int:
    """Return number of days in the given month (1-12).
    Consider leap years for February.
    """
    pass


def m05_triangle_type(a: int, b: int, c: int) -> str:
    """Return "Equilateral", "Isosceles", "Scalene", or "Invalid"."""
    pass


def m06_rock_paper_scissors(p1: str, p2: str) -> str:
    """Return "Player 1 wins", "Player 2 wins", or "Draw"."""
    pass


def m07_quadrant(x: int, y: int) -> str:
    """Return which quadrant (1-4) or "Origin" or "On axis"."""
    pass


def m08_grade_comment(grade: str) -> str:
    """Use match-case: A->"Excellent", B->"Good", C->"Average",
    D->"Below Average", F->"Fail", _->"Invalid grade"
    """
    pass


def m09_discount(price: float, is_member: bool) -> float:
    """Members get 20% off. Non-members get 10% if price > 100, else 0%."""
    pass


def m10_is_weekend(day: str) -> bool:
    """Return True if day is "Saturday" or "Sunday" (case-insensitive)."""
    pass


# ===================== HARD (10) =====================

def h01_fizzbuzz(n: int) -> str:
    """Return "Fizz" if divisible by 3, "Buzz" if by 5,
    "FizzBuzz" if by both, else str(n).
    """
    pass


def h02_valid_triangle_angles(a: int, b: int, c: int) -> bool:
    """Return True if three angles can form a valid triangle (sum = 180, all > 0)."""
    pass


def h03_tax_calculator(income: float) -> float:
    """Progressive tax:
    0-10000: 0%
    10001-50000: 15%
    50001-100000: 25%
    >100000: 35%
    """
    pass


def h04_phone_keypad(char: str) -> int:
    """Return the phone keypad digit (2-9) for a letter.
    2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz.
    Return -1 for non-letter.
    """
    pass


def h05_login_system(username: str, password: str) -> str:
    """Valid users: {"admin": "admin123", "user": "pass123"}.
    Return "Success", "Invalid username", or "Wrong password".
    Note: do NOT hardcode credentials in real code!
    """
    pass


def h06_electricity_bill(units: float) -> float:
    """Slab rates:
    0-100: 5/unit
    101-300: 7/unit
    >300: 10/unit
    """
    pass


def h07_date_validator(day: int, month: int, year: int) -> bool:
    """Return True if the date is valid (consider leap years, month days)."""
    pass


def h08_character_type(ch: str) -> str:
    """Return "Digit", "Uppercase", "Lowercase", "Special", or "Empty"."""
    pass


def h09_three_number_sort(a: int, b: int, c: int) -> tuple:
    """Return a, b, c in sorted order as a tuple. Do NOT use sorted() or .sort()."""
    pass


def h10_scholarship_eligibility(gpa: float, income: float, extracurriculars: int) -> str:
    """Eligible if: GPA >= 3.5 AND income < 50000, OR (GPA >= 3.0 AND extracurriculars >= 3).
    Return "Full", "Partial", or "None".
    """
    pass


# ===================== EXPERT (5) =====================

def x01_tic_tac_toe_winner(board: list) -> str:
    """board is a list of 3 strings, each 3 chars (X, O, or space).
    Return "X", "O", "Draw", or "Incomplete".
    """
    pass


def x02_expression_evaluator(expr: str) -> float:
    """Evaluate a simple expression like "3+5", "10-3", "4*7", "20/5".
    Return the result. Handle invalid input.
    """
    pass


def x03_calendar_printer(month: int, year: int) -> str:
    """Return a string representation of a calendar for the given month.
    Show day names and dates properly aligned.
    """
    pass


def x04_decision_tree_classifier(features: dict) -> str:
    """Simple decision tree classifier.
    features = {"outlook": "sunny"/"overcast"/"rainy",
                "humidity": "high"/"normal",
                "wind": "strong"/"weak"}
    Use nested conditionals to predict "Play" or "Don't Play".
    """
    pass


def x05_credit_score_rating(score: int, history_years: int, delinquencies: int, utilization: float) -> str:
    """Calculate credit rating:
    Start from score:
      > 750 -> "Excellent"
      > 700 -> "Good"
      > 650 -> "Fair"
      > 580 -> "Poor"
      else -> "Bad"
    Then adjust:
      - If history_years < 2: down one tier
      - If delinquencies > 2: down one tier
      - If utilization > 0.9: down one tier
      - If utilization < 0.3 and history_years > 5: up one tier
    """
    pass


# ===================== TEST RUNNER =====================

def test():
    tests = {
        # Easy
        "e01_is_even": [(2, True), (3, False), (0, True), (-4, True)],
        "e02_is_positive": [(5, "Positive"), (-3, "Negative"), (0, "Zero")],
        "e03_max_of_two": [(3, 5, 5), (10, 2, 10), (7, 7, 7)],
        "e04_absolute": [(5, 5), (-5, 5), (0, 0)],
        "e05_is_vowel": [("a", True), ("E", True), ("b", False), ("", False)],
        "e06_can_vote": [(18, True), (16, False), (70, True)],
        "e07_is_leap_year": [(2020, True), (2021, False), (1900, False), (2000, True)],
        "e08_smallest_of_three": [(3, 7, 5, 3), (10, 2, 8, 2), (1, 1, 1, 1)],
        "e09_ends_with_s": [("dogs", True), ("dog", False), ("", False)],
        "e10_is_long_string": [("short", False), ("this is long!", True)],
        # Medium
        "m01_number_to_word": [(1, "One"), (3, "Three"), (6, "Unknown")],
        "m02_temperature_category": [(-5, "Freezing"), (10, "Cold"), (22, "Warm"), (35, "Hot")],
        "m03_bmi_category": [(16, 1.7, "Underweight"), (22, 1.7, "Normal"), (27, 1.7, "Overweight"), (32, 1.7, "Obese")],
        "m04_days_in_month": [(1, 2023, 31), (2, 2023, 28), (2, 2024, 29), (4, 2023, 30)],
        "m05_triangle_type": [(3, 3, 3, "Equilateral"), (3, 3, 4, "Isosceles"), (3, 4, 5, "Scalene"), (1, 2, 3, "Invalid")],
        "m06_rock_paper_scissors": [("rock", "scissors", "Player 1 wins"), ("scissors", "rock", "Player 2 wins"), ("rock", "rock", "Draw")],
        "m07_quadrant": [(2, 3, "Quadrant 1"), (-2, 3, "Quadrant 2"), (-2, -3, "Quadrant 3"), (2, -3, "Quadrant 4"), (0, 0, "Origin")],
        "m08_grade_comment": [("A", "Excellent"), ("C", "Average"), ("F", "Fail"), ("X", "Invalid grade")],
        "m09_discount": [(100, True, 80.0), (200, False, 180.0), (50, False, 50.0)],
        "m10_is_weekend": [("Saturday", True), ("sunday", True), ("Monday", False)],
        # Hard
        "h01_fizzbuzz": [(3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"), (7, "7")],
        "h02_valid_triangle_angles": [(60, 60, 60, True), (90, 45, 45, True), (0, 90, 90, False), (90, 90, 90, False)],
        "h03_tax_calculator": [(5000, 0), (30000, 3000.0), (75000, 13750.0), (200000, 60000.0)],
        "h04_phone_keypad": [("a", 2), ("c", 2), ("z", 9), ("@", -1)],
        "h05_login_system": [("admin", "admin123", "Success"), ("admin", "wrong", "Wrong password"), ("unknown", "x", "Invalid username")],
        "h06_electricity_bill": [(50, 250.0), (200, 1200.0), (400, 3700.0)],
        "h07_date_validator": [(31, 1, 2023, True), (29, 2, 2023, False), (29, 2, 2024, True)],
        "h08_character_type": [("5", "Digit"), ("A", "Uppercase"), ("a", "Lowercase"), ("@", "Special"), ("", "Empty")],
        "h09_three_number_sort": [(3, 1, 2, (1, 2, 3)), (9, 2, 7, (2, 7, 9))],
        "h10_scholarship_eligibility": [(3.8, 30000, 2, "Full"), (3.2, 20000, 4, "Partial"), (2.5, 100000, 0, "None")],
        # Expert
        "x01_tic_tac_toe_winner": [
            (["X X", " O ", "  O"], "Incomplete"),
        ],
        "x02_expression_evaluator": [("3+5", 8.0), ("10-3", 7.0), ("4*7", 28.0), ("20/5", 4.0)],
    }

    passed = 0
    total = 0
    func_map = {k: v for k, v in globals().items() if k.startswith(("e0", "m0", "h0", "x0"))}

    for name, cases in tests.items():
        func = func_map.get(name)
        if func is None:
            print(f"{name}: NOT IMPLEMENTED")
            continue
        for case in cases:
            total += 1
            *args, expected = case
            try:
                result = func(*args)
                if result == expected:
                    passed += 1
                else:
                    print(f"{name}({', '.join(repr(a) for a in args)}) = {result!r}, expected {expected!r}")
            except Exception as e:
                print(f"{name} ERROR: {e}")

    print(f"\n=== {passed}/{total} passed ===")
    if passed == total:
        print("All exercises complete!")
    return passed == total


# ===================== SOLUTIONS =====================

# --- Easy Solutions ---

def e01_is_even_solution(n):
    return n % 2 == 0


def e02_is_positive_solution(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"


def e03_max_of_two_solution(a, b):
    return a if a >= b else b


def e04_absolute_solution(n):
    return n if n >= 0 else -n


def e05_is_vowel_solution(char):
    return len(char) == 1 and char.lower() in "aeiou"


def e06_can_vote_solution(age):
    return age >= 18


def e07_is_leap_year_solution(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def e08_smallest_of_three_solution(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    return c


def e09_ends_with_s_solution(word):
    return len(word) > 0 and word[-1] == "s"


def e10_is_long_string_solution(s):
    return len(s) > 10


# --- Medium Solutions ---

def m01_number_to_word_solution(n):
    match n:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4:
            return "Four"
        case 5:
            return "Five"
        case _:
            return "Unknown"


def m02_temperature_category_solution(celsius):
    if celsius < 0:
        return "Freezing"
    elif celsius <= 15:
        return "Cold"
    elif celsius <= 30:
        return "Warm"
    return "Hot"


def m03_bmi_category_solution(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def m04_days_in_month_solution(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    return 0


def m05_triangle_type_solution(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"


def m06_rock_paper_scissors_solution(p1, p2):
    if p1 == p2:
        return "Draw"
    if (p1 == "rock" and p2 == "scissors") or \
       (p1 == "scissors" and p2 == "paper") or \
       (p1 == "paper" and p2 == "rock"):
        return "Player 1 wins"
    return "Player 2 wins"


def m07_quadrant_solution(x, y):
    if x == 0 and y == 0:
        return "Origin"
    if x == 0 or y == 0:
        return "On axis"
    if x > 0 and y > 0:
        return "Quadrant 1"
    if x < 0 and y > 0:
        return "Quadrant 2"
    if x < 0 and y < 0:
        return "Quadrant 3"
    return "Quadrant 4"


def m08_grade_comment_solution(grade):
    match grade:
        case "A":
            return "Excellent"
        case "B":
            return "Good"
        case "C":
            return "Average"
        case "D":
            return "Below Average"
        case "F":
            return "Fail"
        case _:
            return "Invalid grade"


def m09_discount_solution(price, is_member):
    if is_member:
        return price * 0.8
    elif price > 100:
        return price * 0.9
    return price


def m10_is_weekend_solution(day):
    return day.lower() in ("saturday", "sunday")


# --- Hard Solutions ---

def h01_fizzbuzz_solution(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def h02_valid_triangle_angles_solution(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b + c == 180


def h03_tax_calculator_solution(income):
    if income <= 10000:
        return 0
    elif income <= 50000:
        return (income - 10000) * 0.15
    elif income <= 100000:
        return 40000 * 0.15 + (income - 50000) * 0.25
    return 40000 * 0.15 + 50000 * 0.25 + (income - 100000) * 0.35


def h04_phone_keypad_solution(char):
    if not char.isalpha():
        return -1
    char = char.lower()
    if char in "abc":
        return 2
    if char in "def":
        return 3
    if char in "ghi":
        return 4
    if char in "jkl":
        return 5
    if char in "mno":
        return 6
    if char in "pqrs":
        return 7
    if char in "tuv":
        return 8
    return 9


def h05_login_system_solution(username, password):
    users = {"admin": "admin123", "user": "pass123"}
    if username not in users:
        return "Invalid username"
    if users[username] != password:
        return "Wrong password"
    return "Success"


def h06_electricity_bill_solution(units):
    if units <= 100:
        return units * 5
    elif units <= 300:
        return 100 * 5 + (units - 100) * 7
    return 100 * 5 + 200 * 7 + (units - 300) * 10


def h07_date_validator_solution(day, month, year):
    if month < 1 or month > 12 or day < 1:
        return False
    days_in_month = [31, 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
                     31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day <= days_in_month[month - 1]


def h08_character_type_solution(ch):
    if len(ch) == 0:
        return "Empty"
    if ch.isdigit():
        return "Digit"
    if ch.isupper():
        return "Uppercase"
    if ch.islower():
        return "Lowercase"
    return "Special"


def h09_three_number_sort_solution(a, b, c):
    if a <= b <= c:
        return (a, b, c)
    if a <= c <= b:
        return (a, c, b)
    if b <= a <= c:
        return (b, a, c)
    if b <= c <= a:
        return (b, c, a)
    if c <= a <= b:
        return (c, a, b)
    return (c, b, a)


def h10_scholarship_eligibility_solution(gpa, income, extracurriculars):
    if gpa >= 3.5 and income < 50000:
        return "Full"
    if gpa >= 3.0 and extracurriculars >= 3:
        return "Partial"
    return "None"


# --- Expert Solutions ---

def x01_tic_tac_toe_winner_solution(board):
    lines = (
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    )
    for line in lines:
        cells = [board[r][c] for r, c in line]
        if cells[0] != " " and cells[0] == cells[1] == cells[2]:
            return cells[0]
    if any(" " in row for row in board):
        return "Incomplete"
    return "Draw"


def x02_expression_evaluator_solution(expr):
    if "+" in expr:
        parts = expr.split("+")
        return float(parts[0]) + float(parts[1])
    if "-" in expr:
        parts = expr.split("-")
        return float(parts[0]) - float(parts[1])
    if "*" in expr:
        parts = expr.split("*")
        return float(parts[0]) * float(parts[1])
    if "/" in expr:
        parts = expr.split("/")
        return float(parts[0]) / float(parts[1])
    raise ValueError("Invalid expression")


def x03_calendar_printer_solution(month, year):
    import calendar
    cal = calendar.TextCalendar()
    return cal.formatmonth(year, month)


def x04_decision_tree_classifier_solution(features):
    outlook = features.get("outlook")
    humidity = features.get("humidity")
    wind = features.get("wind")

    if outlook == "overcast":
        return "Play"
    if outlook == "sunny":
        if humidity == "high":
            return "Don't Play"
        return "Play"
    if outlook == "rainy":
        if wind == "strong":
            return "Don't Play"
        return "Play"
    return "Don't Play"


def x05_credit_score_rating_solution(score, history_years, delinquencies, utilization):
    tiers = ["Bad", "Poor", "Fair", "Good", "Excellent"]

    if score > 750:
        idx = 4
    elif score > 700:
        idx = 3
    elif score > 650:
        idx = 2
    elif score > 580:
        idx = 1
    else:
        idx = 0

    if history_years < 2:
        idx -= 1
    if delinquencies > 2:
        idx -= 1
    if utilization > 0.9:
        idx -= 1
    if utilization < 0.3 and history_years > 5:
        idx += 1

    idx = max(0, min(idx, 4))
    return tiers[idx]


if __name__ == "__main__":
    if "--solutions" in sys.argv:
        print("Solutions are defined in this file with _solution suffix.")
    else:
        test()
