#!/usr/bin/env python3
"""
Personal Profile Generator — Solution

This program collects user information, validates it, and displays
a formatted profile card. Demonstrates variables, types, type conversion,
string formatting, and basic validation.
"""

CURRENT_YEAR = 2026

name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
profession = input("Enter your profession: ")

birth_year = CURRENT_YEAR - age

if "@" in email:
    status = "✅ Verified"
else:
    status = "❌ Invalid Email"

print()

profile_card = f"""
┌─────────────────────────────────────┐
│           PERSONAL PROFILE           │
├─────────────────────────────────────┤
│ Name:       {name:<26}│
│ Age:        {age:<26}│
│ Birth Year: {birth_year:<26}│
│ Profession: {profession:<26}│
│ Email:      {email:<26}│
│ Status:     {status:<26}│
└─────────────────────────────────────┘
"""

print(profile_card)
