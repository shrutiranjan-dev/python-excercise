"""
Strings — Exercises (Module 09)

Total: 35 exercises
  Easy: 10
  Medium: 10
  Hard: 10
  Expert: 5

Solutions are at the bottom of the file.
"""

# ============================================================
# EASY (10 exercises)
# ============================================================

# 1. Create a variable `name` with value "Python" and print its first character.


# 2. Convert "hello world" to uppercase and print it.


# 3. Given `text = "  spaces  "`, strip whitespace and print the result.


# 4. Split "apple,banana,orange" by comma and print the resulting list.


# 5. Join ["code", "learn", "grow"] with " - " separator and print.


# 6. Replace "dog" with "cat" in "I have a dog" and print.


# 7. Check if "Python Programming" starts with "Python" and print the boolean.


# 8. Count how many times "a" appears in "banana" and print the count.


# 9. Find the index of "orld" in "Hello World" and print it (use find).


# 10. Check if "12345" consists only of digits and print the boolean.


# ============================================================
# MEDIUM (10 exercises)
# ============================================================

# 11. Reverse the string "Python" using slicing and print it.


# 12. Given `s = "a b c d e"`, split by space, then join back with "|" and print.


# 13. Use an f-string to print "My name is X and I am Y years old" with variables.


# 14. Extract the email domain from "user@example.com" (everything after @) and print.


# 15. Given `word = "racecar"`, check if it's a palindrome and print True/False.


# 16. Capitalize the first letter of each word in "hello world python" using title().


# 17. Create a string that contains a double quote character inside it.


# 18. Format the number 0.1234 as "12.34%" using f-string formatting.


# 19. Remove all vowels (a, e, i, o, u) from "beautiful" and print the result.


# 20. Pad the string "5" with leading zeros to length 3 ("005") and print.


# ============================================================
# HARD (10 exercises)
# ============================================================

# 21. Write a function `word_count(text)` that returns a dict of word frequencies.
#     Words are case-insensitive, punctuation should be stripped.

def word_count(text):
    pass

# Test: word_count("Hello hello! World, world.") -> {"hello": 2, "world": 2}


# 22. Write a function `is_anagram(s1, s2)` that returns True if strings are anagrams.

def is_anagram(s1, s2):
    pass

# Test: is_anagram("listen", "silent") -> True


# 23. Write a function `extract_hashtags(text)` that returns a list of hashtags.

def extract_hashtags(text):
    pass

# Test: extract_hashtags("I love #python and #coding") -> ["#python", "#coding"]


# 24. Write a function `mask_email(email)` that masks the local part.
#     E.g., "john.doe@example.com" -> "j*****e@example.com"

def mask_email(email):
    pass


# 25. Write a function `rotate_string(s, n)` that rotates a string left by n positions.
#     rotate_string("hello", 2) -> "llohe"

def rotate_string(s, n):
    pass


# 26. Write a function `is_pangram(text)` that checks if the text contains all letters A-Z.

def is_pangram(text):
    pass

# Test: is_pangram("The quick brown fox jumps over the lazy dog") -> True


# 27. Write a function `format_phone(phone)` that formats "1234567890" -> "(123) 456-7890".

def format_phone(phone):
    pass


# 28. Write a function `camel_to_snake(name)` that converts "camelCase" to "snake_case".

def camel_to_snake(name):
    pass


# 29. Write a function `remove_duplicate_words(text)` that removes consecutive duplicates.
#     "hello hello world world" -> "hello world"

def remove_duplicate_words(text):
    pass


# 30. Write a function `interleave_strings(a, b)` that interleaves two strings.
#     interleave_strings("abc", "123") -> "a1b2c3"

def interleave_strings(a, b):
    pass


# ============================================================
# EXPERT (5 exercises)
# ============================================================

# 31. Write a function `generate_acronym(phrase)` that returns an acronym.
#     "As Soon As Possible" -> "ASAP"

def generate_acronym(phrase):
    pass


# 32. Write a function `simple_glob_match(pattern, text)` that supports * and ?
#     * matches any sequence, ? matches single char.

def simple_glob_match(pattern, text):
    pass


# 33. Write a function `dedent(text)` that removes common leading whitespace.
#     Similar to textwrap.dedent.

def dedent(text):
    pass


# 34. Write a function `find_all_emails(text)` that extracts all email addresses.

def find_all_emails(text):
    pass


# 35. Write a function `format_paragraph(text, width)` that formats text to a given width.
#     Wrap words to the next line rather than breaking mid-word.

def format_paragraph(text, width):
    pass


# ============================================================
# SOLUTIONS
# ============================================================

r"""
=== EASY ===

# 1
name = "Python"
print(name[0])

# 2
print("hello world".upper())

# 3
text = "  spaces  "
print(text.strip())

# 4
print("apple,banana,orange".split(","))

# 5
print(" - ".join(["code", "learn", "grow"]))

# 6
print("I have a dog".replace("dog", "cat"))

# 7
print("Python Programming".startswith("Python"))

# 8
print("banana".count("a"))

# 9
print("Hello World".find("orld"))

# 10
print("12345".isdigit())

=== MEDIUM ===

# 11
print("Python"[::-1])

# 12
s = "a b c d e"
parts = s.split(" ")
print("|".join(parts))

# 13
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old")

# 14
email = "user@example.com"
print(email.split("@")[1])

# 15
word = "racecar"
print(word == word[::-1])

# 16
print("hello world python".title())

# 17
s = 'She said "Hello"'

# 18
print(f"{0.1234:.2%}")

# 19
text = "beautiful"
vowels = "aeiou"
result = "".join(c for c in text if c not in vowels)
print(result)

# 20
print("5".zfill(3))

=== HARD ===

# 21
def word_count(text):
    import re
    words = re.findall(r"\b\\w+\b", text.lower())
    return {w: words.count(w) for w in set(words)}

# 22
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# 23
def extract_hashtags(text):
    return [word for word in text.split() if word.startswith("#")]

# 24
def mask_email(email):
    local, domain = email.split("@")
    return local[0] + "*" * (len(local) - 2) + local[-1] + "@" + domain

# 25
def rotate_string(s, n):
    n = n % len(s)
    return s[n:] + s[:n]

# 26
def is_pangram(text):
    import string
    return set(c.lower() for c in text if c.isalpha()) == set(string.ascii_lowercase)

# 27
def format_phone(phone):
    return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"

# 28
def camel_to_snake(name):
    result = ""
    for c in name:
        if c.isupper():
            result += "_" + c.lower()
        else:
            result += c
    return result.lstrip("_")

# 29
def remove_duplicate_words(text):
    words = text.split()
    result = [words[0]]
    for w in words[1:]:
        if w != result[-1]:
            result.append(w)
    return " ".join(result)

# 30
def interleave_strings(a, b):
    result = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            result.append(a[i])
        if i < len(b):
            result.append(b[i])
    return "".join(result)

=== EXPERT ===

# 31
def generate_acronym(phrase):
    return "".join(word[0].upper() for word in phrase.split() if word)

# 32
def simple_glob_match(pattern, text):
    import re
    regex = "^" + re.escape(pattern).replace("\\*", ".*").replace("\\?", ".") + "$"
    return bool(re.match(regex, text))

# 33
def dedent(text):
    import textwrap
    return textwrap.dedent(text)

# 34
def find_all_emails(text):
    import re
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# 35
def format_paragraph(text, width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= width:
            current = (current + " " + word).strip()
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return "\n".join(lines)
"""
