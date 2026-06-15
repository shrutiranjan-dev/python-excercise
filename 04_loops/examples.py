"""Module 04: Loops - Examples"""

# ---------------------------------------------------------------
# Level 0: for loop with range
# ---------------------------------------------------------------
print("Counting to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

print("Even numbers:")
for i in range(0, 10, 2):
    print(i, end=" ")
print()


# ---------------------------------------------------------------
# Level 1: Iterating over collections
# ---------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

person = {"name": "Alice", "age": 30, "city": "NYC"}
print("Person details:")
for key, value in person.items():
    print(f"  {key}: {value}")


# ---------------------------------------------------------------
# Level 2: While loop with user input
# ---------------------------------------------------------------
print("Enter numbers to sum. Enter 0 to quit.")
total = 0
while True:
    num = float(input("Enter a number: "))
    if num == 0:
        break
    total += num
    print(f"Running total: {total}")
print(f"Final total: {total}")


# ---------------------------------------------------------------
# Level 3: Batch processing tokenized text
# ---------------------------------------------------------------
text = "The quick brown fox jumps over the lazy dog"
tokens = text.lower().split()
batch_size = 3
print(f"Processing {len(tokens)} tokens in batches of {batch_size}:")

for i in range(0, len(tokens), batch_size):
    batch = tokens[i:i + batch_size]
    processed = [token.upper() for token in batch]
    print(f"  Batch {i // batch_size + 1}: {processed}")


# ---------------------------------------------------------------
# Level 4: Prime number finder
# ---------------------------------------------------------------
def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            primes.append(num)
    return primes

print(f"Primes up to 50: {find_primes(50)}")


# ---------------------------------------------------------------
# Level 5: API pagination with rate limiting
# ---------------------------------------------------------------
import time

def mock_api_call(page, page_size):
    """Simulate an API that returns paginated results."""
    items = [f"item-{page * page_size + i}" for i in range(page_size)]
    has_more = page < 3
    return {"items": items, "has_more": has_more, "total": 15}

def fetch_all_pages(page_size=5):
    all_items = []
    page = 0
    rate_limit_delay = 0.5  # seconds between requests

    while True:
        print(f"Fetching page {page + 1}...")
        response = mock_api_call(page, page_size)
        all_items.extend(response["items"])
        print(f"  Got {len(response['items'])} items (total: {len(all_items)})")

        if not response["has_more"]:
            break

        page += 1
        time.sleep(rate_limit_delay)

    print(f"Complete! Fetched {len(all_items)} items total.")
    return all_items

fetch_all_pages()
