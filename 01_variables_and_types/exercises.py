#!/usr/bin/env python3
"""
Variables & Types — Exercises

Instructions:
  Solve each exercise below.
  Run this file to test your solutions.
  Solutions are at the bottom — try for at least 15 minutes before peeking!
"""

# =============================================================================
# EASY (10 exercises)
# =============================================================================

# Exercise E1: Create a variable named `city` with the value "Tokyo"
# and print it.
# Your code here:
city = "Tokyo"
print(city)

# Exercise E2: Create a variable `population` with the value 37_000_000
# and print it.
# Your code here:
population = 37_000_000
print(population)

# Exercise E3: Create a variable `area_sq_km` with the value 2194.0
# and print it.
# Your code here:
area_sq_km = 2194.0
print(area_sq_km)

# Exercise E4: Create a variable `is_capital` with the value True
# and print it.
# Your code here:
is_capital = True
print(is_capital)
# Exercise E5: Use type() to print the type of `population`.
# Your code here:

# Exercise E6: Create two variables `x` and `y` with values 10 and 20.
# Print their sum.
# Your code here:
x=10
y=20
print(f"the sum will be{x+y}")

# Exercise E7: Set `result` to None, then print it.
# Your code here:
result = None
print(result)

# Exercise E8: Create a variable `name` with your name, then print
# "Hello, <name>!" using string concatenation.
# Your code here:
name = "Deku"
print(f"Hello {name}!")
# Exercise E9: Print the type of 3.14.
# Your code here:
print(type(3.14))

# Exercise E10: Create a variable `is_complete` and set it to False.
# Print it.
# Your code here:
is_complete = False
print(is_complete)

# =============================================================================
# MEDIUM (10 exercises)
# =============================================================================

# Exercise M1: Convert the string "123" to an integer, multiply by 2,
# and print the result (should be 246).
# Your code here:
number = int("123")
print(f"answer will be {number * 2}")

# Exercise M2: Ask the user for their age using input(), convert to int,
# and print how old they'll be in 10 years.
# Your code here:
user_age = int(input("enter your age : "))
print(f"in 10 years you'll be {user_age+10}")

# Exercise M3: Use multiple assignment to set `a`, `b`, `c` to 5, 10, 15.
# Print them all on one line.
# Your code here:
a,b,c = 5,10,15
print(a,b,c)

# Exercise M4: Swap the values of `first` and `second` (currently 100 and 200)
# so that first becomes 200 and second becomes 100. Print both.
first = 100
second = 200
# Your code here:
first, second = second,first
print(first, second)

# Exercise M5: Convert the float 3.99 to a string and concatenate it with
# "Price: $" to produce "Price: $3.99". Print the result.
# Your code here:
price = str(3.99)
print("Price: $" + price)

# Exercise M6: Check if the value None is truthy or falsy. Print the result
# of bool(None).
# Your code here:
print(bool(None))


# Exercise M7: Create a constant MAX_USERS = 1000. Then create a variable
# current_users = 750. Print both.
# Your code here:
MAX_USERS = 1000
current_users = 750
print(MAX_USERS, current_users)

# Exercise M8: Use type() to check the type of the value "3.14" (a string).
# Then convert it to float and print the type again.
# Your code here:
string_value = "3.14"
print(type(string_value))
print(type(float(string_value)))

# Exercise M9: Given `val = "0"`, convert it to bool and explain (in a comment)
# why the result is what it is.
val = "0"
# Your code here:
print(bool(val))  # True

# Exercise M10: Set width = 1920 and height = 1080. Use multiple assignment
# to swap them in one line. Print width and height after the swap.
# Your code here:
width = 1920
height = 1080
width, height = height, width
print(width, height)

# =============================================================================
# HARD (10 exercises)
# =============================================================================

# Exercise H1: This code has a type error. Fix it without changing the types.
# count = "5"
# total = count + 10  # This will error — fix it
# print(total)
# Your fix here:
count = "5"
total = int(count) + 10 
print(total)

# Exercise H2: Write code that safely converts a user input to int.
# If the input cannot be converted, set result to None instead of crashing.
user_input = input("Enter a number: ")
# Your code here:

converted_input = int(user_input)
print(converted_input)
    

# Exercise H3: Validate that an email contains "@". Don't use conditionals —
# just check with the `in` operator and print the boolean result.
email = "user@example.com"
# Your code here:
print('@' in email)

# Exercise H4: Calculate the total cost of an API call:
#   1500 input tokens at $0.03/1k tokens
#   800 output tokens at $0.06/1k tokens
# Store each intermediate value in a variable and print the total formatted
# to 4 decimal places with a $ prefix.
# Your code here:

input_token = 1500
output_token = 800
price = (input_token / 1000) * 0.03 + (output_token /1000) *0.06
print(f"total cost: ${price:.4}")

# Exercise H5: A model returns confidence scores. Set a threshold of 0.8.
# If confidence >= threshold, set `is_confident = True`, else `False`.
# Don't use if/else — use a direct boolean assignment.
confidence = 0.73
threshold = 0.8
# Your code here:

if (confidence>= threshold):
  is_confident = True
else:
  is_confident = False

print(is_confident)  # Should be False

# Exercise H6: Given a string "99.5", convert it first to float, then to int,
# and explain (in a comment) what happens to the decimal part.
value_str = "99.5"
# Your code here:
print(int(float(value_str)))
# Exercise H7: Create a config dictionary (not a dataclass yet) with
# model_name, temperature, and max_tokens. Access and print each value.
# Your code here:

config_dictionary = {"model_name":"gpt-5.5", "temperature": 0.5, "max_tokens": 1233333333, "Access": True}
print(config_dictionary["model_name"])
print(config_dictionary["temperature"])
print(config_dictionary["max_tokens"])
print(config_dictionary["Access"])


# Exercise H8: Write a one-liner that creates variables name, age, city
# from the list ["Alice", 30, "London"] using unpacking. Print all three.
data = ["Alice", 30, "London"]
# Your code here:
name, age, city = data
print(name, age, city)

# Exercise H9: Given `value = "42"`, verify it's a string. If it is,
# convert it to int and add 8 (result: 50). Use type() to check.
value = "42"
# Your code here:
if type(value) == str:
  print(int(value) +8)
else:  print("value is not a string")


# Exercise H10: Create variables with type hints for:
#   - model_name: str = "claude-3"
#   - max_tokens: int = 4096
#   - temperature: float = 0.5
#   - use_vision: bool = True
# Print all four.
# Your code here:
model_name: str = "claude-3"
max_tokens: int = 4096
temperature: float = 0.5
use_vision: bool = True

print(f"the model name is {model_name}, max token limit is {max_tokens}, temperature is {temperature}, use vision is {use_vision}")

# =============================================================================
# EXPERT (5 exercises)
# =============================================================================

# Exercise X1: Create a dataclass called `ServerConfig` with fields:
#   host: str
#   port: int
#   ssl: bool
# Create an instance and print it.
# Your code here:




# Exercise X2: Calculate the memory estimate for storing a list of
# 1_000_000 float values. Assume each float takes 24 bytes.
# Store the result in a variable `memory_bytes`, then convert to MB.
# Print the result.
# Your code here:

# Exercise X3: Create a simple type validator function (not a decorator)
# that takes a value and an expected type, returns True if type matches,
# False otherwise. Test it with int, str, float.
# Your code here:

# Exercise X4: Write code that takes a user's birth year (as int), calculates
# their age, and prints "You are X years old". Handle the case where the
# year hasn't happened yet (future year) by printing "Invalid year".
current_year = 2026
# Your code here:

# Exercise X5: Model configuration with computed fields.
# Create a dataclass `ModelConfig` with:
#   model_name: str
#   context_window: int
#   cost_per_1k_input: float
#   cost_per_1k_output: float
# Create an instance and manually compute:
#   - max_input_tokens = context_window // 2
#   - cost_per_full_context = (max_input_tokens / 1000) * cost_per_1k_input
# Print both computed values.
# Your code here:


# =============================================================================
# SOLUTIONS
# =============================================================================

# --- EASY ---

# E1:
# city = "Tokyo"
# print(city)

# E2:
# population = 37_000_000
# print(population)

# E3:
# area_sq_km = 2194.0
# print(area_sq_km)

# E4:
# is_capital = True
# print(is_capital)

# E5:
# print(type(population))  # <class 'int'>

# E6:
# x = 10
# y = 20
# print(x + y)  # 30

# E7:
# result = None
# print(result)

# E8:
# name = "YourName"
# print("Hello, " + name + "!")

# E9:
# print(type(3.14))  # <class 'float'>

# E10:
# is_complete = False
# print(is_complete)


# --- MEDIUM ---

# M1:
# num = int("123")
# print(num * 2)  # 246

# M2:
# age = int(input("Enter your age: "))
# print(f"In 10 years you'll be {age + 10}")

# M3:
# a, b, c = 5, 10, 15
# print(a, b, c)

# M4:
# first, second = 100, 200
# first, second = second, first
# print(first, second)  # 200 100

# M5:
# price = str(3.99)
# print("Price: $" + price)

# M6:
# print(bool(None))  # False

# M7:
# MAX_USERS = 1000
# current_users = 750
# print(MAX_USERS, current_users)

# M8:
# val = "3.14"
# print(type(val))  # <class 'str'>
# val = float(val)
# print(type(val))  # <class 'float'>

# M9:
# val = "0"
# result = bool(val)
# print(result)  # True — because any non-empty string is truthy
#               # Even though the string contains "0", it's not empty

# M10:
# width, height = 1920, 1080
# width, height = height, width
# print(width, height)  # 1080 1920


# --- HARD ---

# H1:
# count = "5"
# total = int(count) + 10  # Convert string to int first
# print(total)  # 15

# H2:
# user_input = input("Enter a number: ")
# if user_input.lstrip('-').isdigit() or (user_input.count('.') == 1 and
#     user_input.replace('.', '').lstrip('-').isdigit()):
#     result = float(user_input)
# else:
#     result = None
# print(result)

# Or simpler:
# try:
#     result = int(user_input)
# except ValueError:
#     result = None
# print(result)

# H3:
# email = "user@example.com"
# has_at = "@" in email
# print(has_at)  # True

# H4:
# input_tokens = 1500
# output_tokens = 800
# input_cost = (input_tokens / 1000) * 0.03
# output_cost = (output_tokens / 1000) * 0.06
# total_cost = input_cost + output_cost
# print(f"${total_cost:.4f}")  # $0.0930

# H5:
# confidence = 0.73
# threshold = 0.8
# is_confident = confidence >= threshold
# print(is_confident)  # False

# H6:
# value_str = "99.5"
# value_float = float(value_str)
# value_int = int(value_float)
# print(value_int)  # 99 — truncation, not rounding

# H7:
# config = {"model_name": "gpt-4", "temperature": 0.7, "max_tokens": 2048}
# print(config["model_name"])
# print(config["temperature"])
# print(config["max_tokens"])

# H8:
# data = ["Alice", 30, "London"]
# name, age, city = data
# print(name, age, city)

# H9:
# value = "42"
# if type(value) == str:
#     result = int(value) + 8
#     print(result)  # 50

# H10:
# model_name: str = "claude-3"
# max_tokens: int = 4096
# temperature: float = 0.5
# use_vision: bool = True
# print(model_name, max_tokens, temperature, use_vision)


# --- EXPERT ---

# X1:
# from dataclasses import dataclass
# @dataclass
# class ServerConfig:
#     host: str
#     port: int
#     ssl: bool
# config = ServerConfig("localhost", 8080, True)
# print(config)

# X2:
# num_elements = 1_000_000
# bytes_per_float = 24
# memory_bytes = num_elements * bytes_per_float
# memory_mb = memory_bytes / (1024 * 1024)
# print(f"{memory_mb:.2f} MB")  # ~22.89 MB

# X3:
# def check_type(value, expected_type):
#     return type(value) == expected_type
# print(check_type(42, int))     # True
# print(check_type("hi", str))   # True
# print(check_type(3.14, float)) # True
# print(check_type(42, str))     # False

# X4:
# birth_year = int(input("Enter your birth year: "))
# current_year = 2026
# if birth_year > current_year:
#     print("Invalid year")
# else:
#     age = current_year - birth_year
#     print(f"You are {age} years old")

# X5:
# from dataclasses import dataclass
# @dataclass
# class ModelConfig:
#     model_name: str
#     context_window: int
#     cost_per_1k_input: float
#     cost_per_1k_output: float
# cfg = ModelConfig("gpt-4", 8192, 0.03, 0.06)
# max_input_tokens = cfg.context_window // 2
# cost_per_full_context = (max_input_tokens / 1000) * cfg.cost_per_1k_input
# print(f"Max input tokens: {max_input_tokens}")
# print(f"Cost per full context: ${cost_per_full_context:.4f}")
