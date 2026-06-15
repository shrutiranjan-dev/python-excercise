"""
Python Lists - Examples
Level 0-5: From basics to production-ready code.
Run: python examples.py
"""

print("=" * 60)
print("LEVEL 0: Basic List Creation and Indexing")
print("=" * 60)

# Creating lists
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True, None]
empty = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Empty: {empty}")

# Positive indexing
print(f"\nfruits[0]: {fruits[0]}")
print(f"fruits[2]: {fruits[2]}")
print(f"fruits[4]: {fruits[4]}")

# Negative indexing
print(f"\nfruits[-1]: {fruits[-1]}")
print(f"fruits[-3]: {fruits[-3]}")
print(f"numbers[-2]: {numbers[-2]}")

# len() and in
print(f"\nlen(fruits): {len(fruits)}")
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

print("\n" + "=" * 60)
print("LEVEL 1: List Methods")
print("=" * 60)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {nums}")

# append
nums.append(5)
print(f"After append(5): {nums}")

# extend
nums.extend([3, 5])
print(f"After extend([3,5]): {nums}")

# insert
nums.insert(0, 0)
print(f"After insert(0, 0): {nums}")

# remove
nums.remove(1)
print(f"After remove(1): {nums}")

# pop
popped = nums.pop()
print(f"After pop(), got: {popped}, list: {nums}")

# pop at index
popped2 = nums.pop(0)
print(f"After pop(0), got: {popped2}, list: {nums}")

# index
idx = nums.index(5)
print(f"Index of first 5: {idx}")

# count
cnt = nums.count(5)
print(f"Count of 5: {cnt}")

# sort
nums.sort()
print(f"Sorted: {nums}")

# reverse
nums.reverse()
print(f"Reversed: {nums}")

# copy
nums_copy = nums.copy()
print(f"Copy: {nums_copy}")

# clear
nums_copy.clear()
print(f"After clear: {nums_copy}")

print("\n" + "=" * 60)
print("LEVEL 2: Slicing and List Operations")
print("=" * 60)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(f"Full list: {letters}")

# Basic slicing
print(f"letters[2:5]: {letters[2:5]}")
print(f"letters[:4]: {letters[:4]}")
print(f"letters[6:]: {letters[6:]}")
print(f"letters[:]: {letters[:]}")

# Step slicing
print(f"letters[::2]: {letters[::2]}")
print(f"letters[1::2]: {letters[1::2]}")
print(f"letters[::-1]: {letters[::-1]}")
print(f"letters[8:3:-1]: {letters[8:3:-1]}")

# Negative index slicing
print(f"letters[-3:]: {letters[-3:]}")
print(f"letters[:-3]: {letters[:-3]}")
print(f"letters[-5:-2]: {letters[-5:-2]}")

# Using slice for assignment
words = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"\nBefore slice assign: {words}")
words[1:3] = ["blueberry", "cranberry"]
print(f"After words[1:3]=...: {words}")

# List concatenation and repetition
print(f"\n[1, 2] + [3, 4]: {[1, 2] + [3, 4]}")
print(f"[1] * 5: {[1] * 5}")

print("\n" + "=" * 60)
print("LEVEL 3: Conversation History Management for Chat")
print("=" * 60)

class ConversationHistory:
    """Manages chat conversation history."""

    MAX_HISTORY = 10
    SYSTEM_MESSAGE = {"role": "system", "content": "You are a helpful assistant."}

    def __init__(self):
        self.messages = [self.SYSTEM_MESSAGE]

    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})
        self._trim()

    def add_assistant_message(self, content):
        self.messages.append({"role": "assistant", "content": content})
        self._trim()

    def _trim(self):
        """Keep only the last MAX_HISTORY messages (plus system)."""
        while len(self.messages) > self.MAX_HISTORY + 1:
            # Remove oldest user/assistant pair (skip system)
            self.messages.pop(1)

    def get_context_window(self, n=5):
        """Get last n messages for context."""
        if len(self.messages) <= 1:
            return self.messages
        return [self.messages[0]] + self.messages[-n:]

    def clear_history(self):
        self.messages = [self.SYSTEM_MESSAGE]

    def __len__(self):
        return len(self.messages)

    def __str__(self):
        output = []
        for msg in self.messages:
            role = msg["role"].upper()[:4]
            content = msg["content"][:50] + "..." if len(msg["content"]) > 50 else msg["content"]
            output.append(f"[{role}] {content}")
        return "\n".join(output)


chat = ConversationHistory()
chat.add_user_message("What is Python?")
chat.add_assistant_message("Python is a high-level programming language.")
chat.add_user_message("Explain lists please.")
chat.add_assistant_message("Lists are ordered, mutable sequences in Python.")

print("Full conversation:")
print(chat)
print(f"\nTotal messages: {len(chat)}")
print(f"Context window (last 2): {[m['role'] for m in chat.get_context_window(2)]}")

print("\n" + "=" * 60)
print("LEVEL 4: Matrix Operations with Nested Lists")
print("=" * 60)

def create_matrix(rows, cols, default=0):
    """Create a matrix filled with default value."""
    return [[default for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        print(f"  {row}")

def add_matrices(a, b):
    """Element-wise addition of two matrices."""
    rows, cols = len(a), len(a[0])
    return [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]

def multiply_matrices(a, b):
    """Matrix multiplication."""
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise ValueError("Incompatible dimensions")
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(cols_a))
    return result

def transpose(matrix):
    """Transpose a matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def rotate_90(matrix):
    """Rotate matrix 90 degrees clockwise."""
    return [list(row)[::-1] for row in zip(*matrix)]


print("Matrix A:")
A = [[1, 2, 3], [4, 5, 6]]
print_matrix(A)

print("\nMatrix B:")
B = [[7, 8, 9], [10, 11, 12]]
print_matrix(B)

print("\nA + B:")
print_matrix(add_matrices(A, B))

print("\nMatrix C (3x2):")
C = [[1, 2], [3, 4], [5, 6]]
print_matrix(C)

print("\nA * C (2x3 * 3x2 = 2x2):")
print_matrix(multiply_matrices(A, C))

print("\nTranspose of A (2x3 -> 3x2):")
print_matrix(transpose(A))

print("\nRotate 90 degrees clockwise:")
print_matrix(rotate_90([[1, 2], [3, 4]]))

print("\n" + "=" * 60)
print("LEVEL 5: Token Batch Processor with Sliding Window")
print("=" * 60)

import time
import random

class TokenBatchProcessor:
    """Processes tokens in batches using a sliding window approach."""

    def __init__(self, tokens, window_size=3, stride=1):
        self.tokens = tokens
        self.window_size = window_size
        self.stride = stride
        self.windows = self._create_windows()

    def _create_windows(self):
        """Create overlapping windows from token list."""
        windows = []
        for i in range(0, len(self.tokens) - self.window_size + 1, self.stride):
            windows.append(self.tokens[i:i + self.window_size])
        return windows

    def process(self, processor_fn):
        """Apply processor_fn to each window and return results."""
        results = []
        for i, window in enumerate(self.windows):
            processed = processor_fn(window, i)
            results.append(processed)
        return results

    def batch_process(self, processor_fn, batch_size=2):
        """Process in batches with simulated parallelism."""
        all_results = []
        for i in range(0, len(self.windows), batch_size):
            batch = self.windows[i:i + batch_size]
            print(f"Processing batch {i // batch_size + 1}: windows {i} to {i + len(batch) - 1}")
            batch_results = [processor_fn(w, idx) for idx, w in enumerate(batch, i)]
            all_results.extend(batch_results)
        return all_results

    def sliding_train_test_split(self, test_ratio=0.2):
        """Split windows into train and test sets."""
        split_idx = int(len(self.windows) * (1 - test_ratio))
        train_windows = self.windows[:split_idx]
        test_windows = self.windows[split_idx:]
        return train_windows, test_windows

    def get_context(self, position, context_size=5):
        """Get context around a position."""
        start = max(0, position - context_size // 2)
        end = min(len(self.tokens), position + context_size // 2 + 1)
        return self.tokens[start:end]

    def __str__(self):
        return (f"TokenBatchProcessor({len(self.tokens)} tokens, "
                f"{len(self.windows)} windows, "
                f"window_size={self.window_size}, stride={self.stride})")


tokens = [f"tok_{i}" for i in range(20)]
print(f"Original tokens: {tokens}")

processor = TokenBatchProcessor(tokens, window_size=4, stride=2)
print(f"\n{processor}")
print(f"\nWindows: {processor.windows}")

print("\n--- Process each window (count tokens) ---")
results = processor.process(lambda w, i: f"Window{i}: {len(w)} tokens, first={w[0]}, last={w[-1]}")
for r in results:
    print(f"  {r}")

print("\n--- Batch processing ---")
batch_results = processor.batch_process(
    lambda w, i: f"Win{i}: avg_len={sum(len(t) for t in w) / len(w):.1f}",
    batch_size=3
)
for r in batch_results:
    print(f"  {r}")

print("\n--- Train/Test Split ---")
train, test = processor.sliding_train_test_split(test_ratio=0.3)
print(f"Train windows: {train}")
print(f"Test windows: {test}")

print("\n--- Context around position 10 ---")
context = processor.get_context(10, context_size=7)
print(f"Context around token 10: {context}")

print("\nAll examples completed successfully!")
