"""
Custom helper module for Level 1 example.
This file demonstrates creating a module with the __name__ guard.
"""


def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


PI = 3.14159


if __name__ == "__main__":
    print("myhelper.py ran directly!")
    print(greet("World"))
    print(f"PI = {PI}")
