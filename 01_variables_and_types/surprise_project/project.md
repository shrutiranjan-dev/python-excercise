# 🎯 Surprise Project: Personal Profile Generator

## Overview

Build a program that collects personal information from the user and generates a formatted profile card. This project brings together everything from Module 01: variables, types, user input, type conversion, string formatting, and basic validation.

## Requirements

1. **Collect user input** for:
   - Name (string)
   - Age (integer)
   - Email (string)
   - Profession (string)

2. **Calculate** the user's birth year from their age.

3. **Validate** that the email contains an `@` symbol.

4. **Generate** a formatted profile card that looks like:

```
┌─────────────────────────────────────┐
│           PERSONAL PROFILE           │
├─────────────────────────────────────┤
│ Name:       Alice Johnson           │
│ Age:        28                      │
│ Birth Year: 1998                    │
│ Profession: Software Engineer       │
│ Email:      alice@example.com       │
│ Status:     ✅ Verified             │
└─────────────────────────────────────┘
```

5. **Save** the profile card to a string variable.

6. **Print** the profile card.

## Expected Output

When run with the inputs `Alice Johnson`, `28`, `alice@example.com`, and `Software Engineer`:

```
Enter your name: Alice Johnson
Enter your age: 28
Enter your email: alice@example.com
Enter your profession: Software Engineer

┌─────────────────────────────────────┐
│           PERSONAL PROFILE           │
├─────────────────────────────────────┤
│ Name:       Alice Johnson           │
│ Age:        28                      │
│ Birth Year: 1998                    │
│ Profession: Software Engineer       │
│ Email:      alice@example.com       │
│ Status:     ✅ Verified             │
└─────────────────────────────────────┘
```

If the email is invalid (no `@`):

```
Enter your name: Alice Johnson
Enter your age: 28
Enter your email: invalid-email
Enter your profession: Software Engineer

┌─────────────────────────────────────┐
│           PERSONAL PROFILE           │
├─────────────────────────────────────┤
│ Name:       Alice Johnson           │
│ Age:        28                      │
│ Birth Year: 1998                    │
│ Profession: Software Engineer       │
│ Email:      invalid-email          │
│ Status:     ❌ Invalid Email        │
└─────────────────────────────────────┘
```

## Hints

1. Use `input()` to get data from the user — it always returns a string.
2. Convert age to `int` using `int()`.
3. Calculate birth year: `current_year - age`.
4. Use `in` operator to check if `"@"` is in the email string.
5. Use f-strings for formatting.
6. Use escape characters (`\n`) for newlines.
7. For the box drawing, use `┌`, `─`, `┐`, `│`, `├`, `┘`, `└`, and `─`.
8. Pad strings with spaces for alignment — use f-string format specifiers.

## Extension Challenges

Once you have the basic version working, try these:

1. **Phone number validation**: Add a phone number field and validate it has exactly 10 digits.
2. **Multiple profiles**: Allow the user to create multiple profiles and store them in a list.
3. **Age validation**: Ensure age is between 0 and 150.
4. **Email domain extraction**: If valid, extract the domain (e.g., "example.com" from "alice@example.com").
5. **Formatted output to file**: Save the profile card to a text file.

## Evaluation Criteria

| Criterion | Points |
|---|---|
| All inputs collected correctly | 20% |
| Birth year calculated correctly | 15% |
| Email validation works | 20% |
| Profile card formatting is clean | 25% |
| Code is readable with good variable names | 10% |
| No crashes on valid input | 10% |

## Before You Start

Try to build this without looking at `solution.py`. If you get stuck for more than 30 minutes, peek at the solution, understand it, then close it and build it from memory.
