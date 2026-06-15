#!/usr/bin/env python3
"""
Smart Calculator — Solution

A calculator that takes two numbers and an operator, performs the operation,
and shows step-by-step evaluation. Demonstrates arithmetic, comparison, and
logical operators with input validation.
"""

SUPPORTED_OPERATORS = ["+", "-", "*", "/", "//", "%", "**"]

print("=== Smart Calculator ===")

num1_input = input("Enter first number: ")
num2_input = input("Enter second number: ")
operator = input("Enter operator (+, -, *, /, //, %, **): ")

try:
    num1 = float(num1_input)
    num2 = float(num2_input)
except ValueError:
    print("Error: Invalid number input")
    exit()

if operator not in SUPPORTED_OPERATORS:
    print(f"Error: Unsupported operator '{operator}'. Please use one of: {', '.join(SUPPORTED_OPERATORS)}")
    exit()

print()
print("Step-by-step evaluation:")

num1_str = str(int(num1)) if num1 == int(num1) else str(num1)
num2_str = str(int(num2)) if num2 == int(num2) else str(num2)

print(f"  {num1_str} {operator} {num2_str}")
print(f"= {num1_str} {operator} {num2_str}")

if operator in ["/", "//", "%"] and num2 == 0:
    print(f"= Error: Cannot divide by zero")
    exit()

result = None

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "//":
    result = num1 // num2
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2

if result is not None:
    if result == int(result) and not isinstance(result, bool):
        result_str = str(int(result))
    else:
        result_str = f"{result:.4f}"

    print(f"= {result_str}")
    print()
    print(f"Result: {num1_str} {operator} {num2_str} = {result_str}")
