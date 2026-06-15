"""Module 03: Conditionals - Examples"""

# ---------------------------------------------------------------
# Level 0: Basic if-else
# ---------------------------------------------------------------
temperature = 30
if temperature > 25:
    print("It's hot outside!")
else:
    print("It's cool outside.")


# ---------------------------------------------------------------
# Level 1: if-elif-else chain
# ---------------------------------------------------------------
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score} -> Grade: {grade}")


# ---------------------------------------------------------------
# Level 2: Nested conditionals with user input
# ---------------------------------------------------------------
age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ").strip().lower() == "yes"

if age >= 16:
    if has_license:
        print("You can drive!")
    else:
        print("You need to get a license first.")
else:
    years_left = 16 - age
    print(f"Wait {years_left} more year(s) before you can drive.")


# ---------------------------------------------------------------
# Level 3: Model confidence threshold router
# ---------------------------------------------------------------
query = "Explain quantum computing"
confidence = 0.72

if confidence >= 0.95:
    model = "gpt-4"
    response = f"[{model}] Detailed answer about: {query}"
elif confidence >= 0.80:
    model = "claude-3"
    response = f"[{model}] Balanced answer about: {query}"
elif confidence >= 0.60:
    model = "llama-3"
    response = f"[{model}] Concise answer about: {query}"
else:
    model = "fallback"
    response = f"[{model}] I'm not confident. Please rephrase: {query}"

print(response)


# ---------------------------------------------------------------
# Level 4: Grade calculator with match-case
# ---------------------------------------------------------------
letter = input("Enter your letter grade (A/B/C/D/F): ").upper()
match letter:
    case "A":
        print("Excellent! 90-100")
    case "B":
        print("Good! 80-89")
    case "C":
        print("Average! 70-79")
    case "D":
        print("Below average! 60-69")
    case "F":
        print("Failing! Below 60")
    case _:
        print("Invalid grade.")


# ---------------------------------------------------------------
# Level 5: Multi-stage content moderation filter
# ---------------------------------------------------------------
content = "Buy cheap watches!!! CLICK HERE: http://spam.com"

has_url = "http" in content or "www." in content
has_all_caps_words = sum(1 for w in content.split() if w.isupper() and len(w) > 2)
excessive_punctuation = content.count("!") + content.count("?") > 3
spam_keywords = ["buy", "cheap", "click here", "free money", "act now"]
has_spam_keyword = any(kw in content.lower() for kw in spam_keywords)

if has_url and has_spam_keyword:
    decision = "BLOCKED — Spam with malicious link"
elif has_all_caps_words > 3 and excessive_punctuation:
    decision = "BLOCKED — Shouting detected"
elif has_spam_keyword and excessive_punctuation:
    decision = "FLAGGED — Potential spam, review needed"
elif has_url:
    decision = "FLAGGED — Contains link, moderate review"
elif has_all_caps_words > 1:
    decision = "MONITORED — Excessive caps, warn user"
else:
    decision = "APPROVED — Content looks clean"

print(f"Content: {content[:50]}...")
print(f"Decision: {decision}")
