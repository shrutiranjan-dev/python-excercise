#!/usr/bin/env python3
"""
Operators — Exercises

Instructions:
  Solve each exercise below.
  Run this file to test your solutions.
  Solutions are at the bottom — try for at least 15 minutes before peeking!
"""

# =============================================================================
# EASY (10 exercises)
# =============================================================================

# Exercise E1: Calculate and print the result of 25 + 37.
# Your code here:

# Exercise E2: Calculate and print the result of 100 - 34.
# Your code here:

# Exercise E3: Calculate and print the result of 12 * 8.
# Your code here:

# Exercise E4: Calculate and print the result of 81 / 9 (true division).
# Your code here:

# Exercise E5: Calculate and print the result of 25 // 4 (floor division).
# Your code here:

# Exercise E6: Calculate and print the remainder of 29 divided by 5.
# Your code here:

# Exercise E7: Calculate and print 3 to the power of 4.
# Your code here:

# Exercise E8: Check if 15 is greater than 10. Print the result.
# Your code here:

# Exercise E9: Check if 20 is equal to 20. Print the result.
# Your code here:

# Exercise E10: Check if 7 is less than or equal to 5. Print the result.
# Your code here:


# =============================================================================
# MEDIUM (10 exercises)
# =============================================================================

# Exercise M1: Use augmented assignment (+=) to add 10 to x. Print x.
x = 25
# Your code here:

# Exercise M2: Use //= to perform floor division on a by b. Print a.
a = 37
b = 5
# Your code here:

# Exercise M3: Check if 10 is between 5 and 15 using chained comparison.
# Print the result.
# Your code here:

# Exercise M4: Assign "adult" to status if age >= 18, otherwise "minor".
# Use a ternary operator.
age = 17
# Your code here:
print(status)  # minor

# Exercise M5: Check if "cat" is in the animals list. Print the result.
animals = ["dog", "cat", "bird"]
# Your code here:

# Exercise M6: Check if "elephant" is NOT in the animals list. Print result.
# Your code here:

# Exercise M7: Use AND to check if x > 0 and y < 100. Print result.
x = 50
y = 75
# Your code here:

# Exercise M8: Use OR to check if model is "gpt-4" or "claude-3". Print result.
model = "llama-3"
# Your code here:

# Exercise M9: Use NOT to invert the boolean value of is_ready. Print result.
is_ready = False
# Your code here:

# Exercise M10: Check if result is None using the `is` operator. Print result.
result = None
# Your code here:


# =============================================================================
# HARD (10 exercises)
# =============================================================================

# Exercise H1: Given a list of model scores, check if ALL scores are >= 0.5.
# Use logical operators (no loops — assume you have individual variables).
score1, score2, score3 = 0.8, 0.6, 0.9
# Your code here:
print(all_above_threshold)  # True

# Exercise H2: Write a one-liner that checks if a number is both positive
# AND even. Use modulo and comparison operators.
num = 42
# Your code here:
print(is_positive_even)  # True

# Exercise H3: Given a total token count of 3750 and a max of 4096, calculate
# the remaining tokens. Then check if the remaining is at least 10% of max.
used_tokens = 3750
max_tokens = 4096
# Your code here:
print(has_sufficient_buffer)  # True or False?

# Exercise H4: Calculate the cost for 2700 input tokens at $0.015/1k.
# Use operator precedence correctly without extra parentheses.
input_tokens = 2700
rate = 0.015
# Your code here:
print(f"${cost:.4f}")  # $0.0405

# Exercise H5: Check if a temperature value is in the valid range [0.0, 2.0].
# Also check if it's in the "creative" range [0.7, 1.2].
# Use chained comparisons.
temperature = 1.5
# Your code here:
print(is_valid)      # True
print(is_creative)   # False

# Exercise H6: Given a list of supported models, determine if routing to
# "falcon-180b" is supported. If not, set fallback to True using ternary.
supported = ["gpt-4", "claude-3", "llama-3", "mistral"]
target = "falcon-180b"
# Your code here:
print(fallback)  # True

# Exercise H7: Use the walrus operator (:=) to assign and check in one line.
# Assign half = total // 2, then check if half is greater than 10. Print both.
total = 50
# Your code here:
# Should print: half=25, greater_than_10=True

# Exercise H8: Calculate if a given year is a leap year.
# Leap year rule: divisible by 4 AND (NOT divisible by 100 OR divisible by 400)
year = 2024
# Your code here:
print(is_leap)  # True

# Exercise H9: Check operator precedence. Without running, what is the result
# of: 2 + 3 * 4 ** 2 / 8? Write the expression and verify with print.
# Your code here:
# Expected: ?

# Exercise H10: Given a batch of data, check if the batch size is valid:
# - batch_size must be > 0
# - len(data) must be divisible by batch_size (no remainder)
# - len(data) must be at least 2 * batch_size
data = list(range(128))
batch_size = 32
# Your code here:
print(is_valid_batch)  # True


# =============================================================================
# EXPERT (5 exercises)
# =============================================================================

# Exercise X1: Implement a simple rate limiter check using modulo.
# Given a request counter and a limit of 60 requests per minute,
# check if the current request should be allowed (every 60th request
# should be denied as the "reset" marker).
request_number = 120
limit = 60
# Your code here:
print(should_allow)  # False (120 % 60 == 0, so it's the reset)

# Exercise X2: Token bucket algorithm simulation.
# Bucket capacity: 1000 tokens
# Current tokens: 450
# Request needs: 200 tokens
# After processing, refill rate is 10 tokens per second for 15 seconds.
# Calculate if the request can be processed, and the final token count.
capacity = 1000
current = 450
needed = 200
refill_rate = 10
refill_seconds = 15
# Your code here:
print(can_process)    # True
print(final_tokens)   # 400

# Exercise X3: Implement a simple BLEU score precision check.
# Given matched_ngrams = 3 and total_ngrams = 5, calculate precision.
# Apply a brevity penalty: if candidate_length < reference_length,
# multiply by exp(1 - reference_length / candidate_length).
# Use only operators (no math.exp, just approximate with **? or use math).
# Hint: e^x ≈ 2.718**x
matched_ngrams = 3
total_ngrams = 5
candidate_len = 8
reference_len = 10
# Your code here:
print(bleu_score)  # Approximate BLEU score

# Exercise X4: F1 score calculator using only operators.
# Given precision and recall as floats, calculate:
# F1 = 2 * (precision * recall) / (precision + recall)
# Handle the case where precision + recall == 0 (result should be 0.0).
precision = 0.8
recall = 0.6
# Your code here:
print(f1_score)  # 0.6857...

# Exercise X5: Semantic similarity threshold using multiple checks.
# Given two probability distributions (as individual variables for simplicity):
# p1 = 0.9, p2 = 0.05, p3 = 0.05
# q1 = 0.7, q2 = 0.2, q3 = 0.1
# Check if the dot product >= 0.8 AND the max difference <= 0.3.
# Calculate dot product as p1*q1 + p2*q2 + p3*q3
# Max difference as max(|p1-q1|, |p2-q2|, |p3-q3|)
p1, p2, p3 = 0.9, 0.05, 0.05
q1, q2, q3 = 0.7, 0.2, 0.1
# Your code here:
print(is_similar)  # True or False?


# =============================================================================
# SOLUTIONS
# =============================================================================

# --- EASY ---

# E1:
# print(25 + 37)  # 62

# E2:
# print(100 - 34)  # 66

# E3:
# print(12 * 8)  # 96

# E4:
# print(81 / 9)  # 9.0

# E5:
# print(25 // 4)  # 6

# E6:
# print(29 % 5)  # 4

# E7:
# print(3 ** 4)  # 81

# E8:
# print(15 > 10)  # True

# E9:
# print(20 == 20)  # True

# E10:
# print(7 <= 5)  # False


# --- MEDIUM ---

# M1:
# x = 25
# x += 10
# print(x)  # 35

# M2:
# a = 37
# b = 5
# a //= b
# print(a)  # 7

# M3:
# print(5 < 10 < 15)  # True

# M4:
# age = 17
# status = "adult" if age >= 18 else "minor"
# print(status)  # minor

# M5:
# animals = ["dog", "cat", "bird"]
# print("cat" in animals)  # True

# M6:
# print("elephant" not in animals)  # True

# M7:
# x = 50
# y = 75
# result = x > 0 and y < 100
# print(result)  # True

# M8:
# model = "llama-3"
# result = model == "gpt-4" or model == "claude-3"
# print(result)  # False

# M9:
# is_ready = False
# print(not is_ready)  # True

# M10:
# result = None
# print(result is None)  # True


# --- HARD ---

# H1:
# score1, score2, score3 = 0.8, 0.6, 0.9
# all_above_threshold = score1 >= 0.5 and score2 >= 0.5 and score3 >= 0.5
# print(all_above_threshold)  # True

# H2:
# num = 42
# is_positive_even = num > 0 and num % 2 == 0
# print(is_positive_even)  # True

# H3:
# used_tokens = 3750
# max_tokens = 4096
# remaining = max_tokens - used_tokens
# has_sufficient_buffer = remaining >= max_tokens * 0.1
# print(has_sufficient_buffer)  # True (remaining=346, 10% of 4096=409.6... wait, 346 < 409.6, so False)
# Actually: remaining = 4096 - 3750 = 346, 10% of 4096 = 409.6, 346 < 409.6 → False

# H4:
# input_tokens = 2700
# rate = 0.015
# cost = input_tokens / 1000 * rate
# print(f"${cost:.4f}")  # $0.0405

# H5:
# temperature = 1.5
# is_valid = 0.0 <= temperature <= 2.0
# is_creative = 0.7 <= temperature <= 1.2
# print(is_valid)     # True
# print(is_creative)  # False

# H6:
# supported = ["gpt-4", "claude-3", "llama-3", "mistral"]
# target = "falcon-180b"
# fallback = True if target not in supported else False
# print(fallback)  # True

# H7:
# total = 50
# print(f"half={(half := total // 2)}, greater_than_10={half > 10}")
# half=25, greater_than_10=True

# H8:
# year = 2024
# is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# print(is_leap)  # True

# H9:
# result = 2 + 3 * 4 ** 2 / 8  # 2 + 3 * 16 / 8 → 2 + 48 / 8 → 2 + 6 → 8
# print(result)  # 8.0

# H10:
# data = list(range(128))
# batch_size = 32
# is_valid_batch = batch_size > 0 and len(data) % batch_size == 0 and len(data) >= 2 * batch_size
# print(is_valid_batch)  # True


# --- EXPERT ---

# X1:
# request_number = 120
# limit = 60
# should_allow = request_number % limit != 0
# print(should_allow)  # False

# X2:
# capacity = 1000
# current = 450
# needed = 200
# refill_rate = 10
# refill_seconds = 15
# can_process = current >= needed
# current -= needed if can_process else 0
# current = min(current + refill_rate * refill_seconds, capacity)
# final_tokens = current
# print(can_process)   # True
# print(final_tokens)  # 400

# X3:
# matched_ngrams = 3
# total_ngrams = 5
# candidate_len = 8
# reference_len = 10
# precision = matched_ngrams / total_ngrams
# brevity_penalty = 2.718 ** (1 - reference_len / candidate_len) if candidate_len < reference_len else 1
# bleu_score = precision * brevity_penalty
# print(bleu_score)  # ~0.496

# X4:
# precision = 0.8
# recall = 0.6
# f1_score = 0.0 if precision + recall == 0 else 2 * (precision * recall) / (precision + recall)
# print(f1_score)  # 0.685714...

# X5:
# p1, p2, p3 = 0.9, 0.05, 0.05
# q1, q2, q3 = 0.7, 0.2, 0.1
# dot_product = p1 * q1 + p2 * q2 + p3 * q3
# max_diff = max(abs(p1 - q1), abs(p2 - q2), abs(p3 - q3))
# is_similar = dot_product >= 0.8 and max_diff <= 0.3
# print(is_similar)  # False (dot=0.645)
