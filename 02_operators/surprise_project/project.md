# 🎯 Surprise Project: Smart Calculator

## Overview

Build a calculator that takes two numbers and an operator, performs the operation, and shows a step-by-step evaluation. This project demonstrates arithmetic, comparison, and logical operators in a real-world tool.

## Requirements

1. **Take two numbers** from the user (handle both int and float input).

2. **Take an operator** from the user. Supported operators:
   - `+` (addition)
   - `-` (subtraction)
   - `*` (multiplication)
   - `/` (true division)
   - `//` (floor division)
   - `%` (modulus)
   - `**` (exponentiation)

3. **Handle division by zero** — print an error message instead of crashing.

4. **Show step-by-step evaluation**:

```
=== Smart Calculator ===
Enter first number: 10
Enter second number: 3
Enter operator (+, -, *, /, //, %, **): /

Step-by-step evaluation:
  10 / 3
= 10.0 / 3.0     (converted to float)
= 3.3333         (result)

Result: 10.0 / 3.0 = 3.3333
```

5. **Validate inputs:**
   - Numbers must be valid (convert to float)
   - Operator must be one of the supported operators
   - Division by zero should show: `Error: Cannot divide by zero`

6. **Format the result:**
   - If the result is a whole number (e.g., 4.0), display it as `4`
   - Otherwise, show up to 4 decimal places

## Expected Output

### Normal operation:

```
=== Smart Calculator ===
Enter first number: 10
Enter second number: 3
Enter operator (+, -, *, /, //, %, **): /

Step-by-step evaluation:
  10 / 3
= 10.0 / 3.0
= 3.3333

Result: 10.0 / 3.0 = 3.3333
```

### Division by zero:

```
=== Smart Calculator ===
Enter first number: 5
Enter second number: 0
Enter operator (+, -, *, /, //, %, **): /

Step-by-step evaluation:
  5 / 0
= 5.0 / 0.0
= Error: Cannot divide by zero
```

### Invalid operator:

```
=== Smart Calculator ===
Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /, //, %, **): ^
Error: Unsupported operator '^'. Please use one of: +, -, *, /, //, %, **
```

## Hints

1. Use `float()` to convert input to a number (supports integer and decimal input).
2. Use a chained conditional (if/elif/else) to check the operator.
3. To check if a float is a whole number: `result == int(result)` or `result % 1 == 0`.
4. For formatting, use f-string format specifiers: `f"{result:.4f}"`.
5. Use `: thinspace` for the step-by-step to align nicely.
6. Remember `//` and `%` also can't work with zero divisor.

## Extension Challenges

Once the basic version works, try these:

1. **History mode**: Keep a history of all calculations and show them at the end.
2. **Chain calculations**: Use the result as the first number for the next operation.
3. **Scientific operations**: Add `sin`, `cos`, `tan`, `log`, `sqrt` operators.
4. **Parentheses support**: Parse and evaluate expressions with parentheses (advanced).
5. **Memory functions**: Add M+, M-, MR, MC (memory store, recall, clear).

## Evaluation Criteria

| Criterion | Points |
|---|---|
| All 7 operators work correctly | 25% |
| Division by zero handled | 20% |
| Input validation (numbers + operator) | 20% |
| Step-by-step output format | 20% |
| Whole number formatting | 10% |
| Code readability | 5% |

## Before You Start

Try to build this without looking at `solution.py`. If you get stuck for more than 30 minutes, peek at the solution, understand it, then close it and build it from memory.
