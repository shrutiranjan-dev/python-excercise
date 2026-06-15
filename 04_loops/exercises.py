"""Module 04: Loops - Exercises"""

import sys


# ===================== EASY (10) =====================

def e01_sum_to_n(n: int) -> int:
    """Return the sum of all numbers from 1 to n (inclusive)."""
    pass


def e02_count_vowels(text: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in text. Case-insensitive."""
    pass


def e03_reverse_string(s: str) -> str:
    """Return the reversed string using a loop (not slicing)."""
    pass


def e04_find_max(numbers: list) -> int:
    """Return the maximum number in a list using a loop (not max())."""
    pass


def e05_count_words(text: str) -> int:
    """Return the number of words in text (split by spaces)."""
    pass


def e06_multiplication_table(n: int) -> list:
    """Return a list of [n*1, n*2, ..., n*10]."""
    pass


def e07_countdown(n: int) -> list:
    """Return a list from n down to 1."""
    pass


def e08_sum_even_numbers(numbers: list) -> int:
    """Return the sum of all even numbers in the list."""
    pass


def e09_string_explosion(s: str) -> str:
    """Return a string where each character is repeated by its index+1 times.
    E.g., "abc" -> "abbccc"
    """
    pass


def e10_list_average(numbers: list) -> float:
    """Return the average of numbers. Return 0.0 for empty list."""
    pass


# ===================== MEDIUM (10) =====================

def m01_find_duplicates(items: list) -> list:
    """Return a list of items that appear more than once, in order of first duplicate."""
    pass


def m02_palindrome_check(text: str) -> bool:
    """Return True if text is a palindrome (same forwards and backwards).
    Ignore case, spaces, and punctuation.
    """
    pass


def m03_remove_adjacent_duplicates(s: str) -> str:
    """Remove adjacent duplicate characters.
    E.g., "aabcc" -> "abc"
    """
    pass


def m04_flatten_matrix(matrix: list) -> list:
    """Flatten a 2D list into 1D using nested loops.
    E.g., [[1,2],[3,4]] -> [1,2,3,4]
    """
    pass


def m05_word_frequency(text: str) -> dict:
    """Return a dict of word frequencies in the text (case-insensitive)."""
    pass


def m06_fibonacci_sequence(n: int) -> list:
    """Return the first n Fibonacci numbers.
    fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)
    """
    pass


def m07_find_missing_number(numbers: list) -> int:
    """numbers contains 0 to n with one missing. Find the missing number.
    E.g., [3, 0, 1] -> 2
    """
    pass


def m08_alternating_sum(numbers: list) -> int:
    """Return numbers[0] - numbers[1] + numbers[2] - numbers[3] + ..."""
    pass


def m09_common_elements(list1: list, list2: list) -> list:
    """Return a list of elements that appear in both lists (no duplicates)."""
    pass


def m10_rotate_list(items: list, k: int) -> list:
    """Rotate the list to the right by k positions.
    E.g., [1,2,3,4,5], k=2 -> [4,5,1,2,3]
    """
    pass


# ===================== HARD (10) =====================

def h01_merge_sorted_lists(a: list, b: list) -> list:
    """Merge two sorted lists into one sorted list using a two-pointer approach."""
    pass


def h02_longest_increasing_subsequence(numbers: list) -> list:
    """Return the longest contiguous increasing subsequence.
    E.g., [1,3,5,2,4,6,8] -> [2,4,6,8]
    """
    pass


def h03_sieve_of_eratosthenes(n: int) -> list:
    """Return all prime numbers up to n using the Sieve of Eratosthenes."""
    pass


def h04_matrix_multiplication(a: list, b: list) -> list:
    """Multiply two matrices using nested loops.
    a is m x n, b is n x p. Return m x p matrix.
    """
    pass


def h05_run_length_encoding(s: str) -> list:
    """Return run-length encoding as list of (char, count) tuples.
    E.g., "aaabbc" -> [("a",3), ("b",2), ("c",1)]
    """
    pass


def h06_snake_case_to_camel_case(s: str) -> str:
    """Convert snake_case to camelCase.
    E.g., "hello_world" -> "helloWorld"
    """
    pass


def h07_caesar_cipher(text: str, shift: int) -> str:
    """Shift each letter by `shift` positions in the alphabet.
    Preserve case. Non-letters stay unchanged.
    """
    pass


def h08_tic_tac_toe_valid(board: list) -> bool:
    """board is 3x3 list of "X", "O", or " ".
    Return True if the board state is reachable in a valid game.
    """
    pass


def h09_sudoku_row_validator(grid: list) -> bool:
    """grid is 9x9 list of ints (0 means empty).
    Return True if each row has no duplicates (1-9).
    """
    pass


def h10_binary_search(sorted_list: list, target: int) -> int:
    """Return the index of target in sorted_list using binary search (loop, not recursion).
    Return -1 if not found.
    """
    pass


# ===================== EXPERT (5) =====================

def x01_spiral_matrix(n: int) -> list:
    """Generate an n x n spiral matrix.
    E.g., n=3 -> [[1,2,3],[8,9,4],[7,6,5]]
    """
    pass


def x02_n_queens_count(n: int) -> int:
    """Return the number of ways to place n queens on an n x n board.
    Use backtracking with loops.
    """
    pass


def x03_text_justify(words: list, max_width: int) -> list:
    """Format words into fully-justified lines of exactly max_width characters.
    Equal spacing between words, extra spaces left-to-right.
    Last line is left-justified.
    """
    pass


def x04_sliding_window_max(nums: list, k: int) -> list:
    """Return max of each sliding window of size k.
    E.g., [1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7]
    """
    pass


def x05_largest_rectangle_in_histogram(heights: list) -> int:
    """Return the area of the largest rectangle in a histogram.
    E.g., [2,1,5,6,2,3] -> 10 (using heights 5 and 6)
    """
    pass


# ===================== TEST RUNNER =====================

def test():
    tests = {
        "e01_sum_to_n": [(5, 15), (1, 1), (0, 0)],
        "e02_count_vowels": [("hello", 2), ("AEIOU", 5), ("xyz", 0)],
        "e03_reverse_string": [("abc", "cba"), ("", ""), ("a", "a")],
        "e04_find_max": [([1, 5, 3, 9, 2], 9), ([-5, -2, -10], -2)],
        "e05_count_words": [("hello world", 2), ("", 0), ("a b c", 3)],
        "e06_multiplication_table": [(3, [3, 6, 9, 12, 15, 18, 21, 24, 27, 30])],
        "e07_countdown": [(3, [3, 2, 1]), (1, [1])],
        "e08_sum_even_numbers": [([1, 2, 3, 4, 5, 6], 12), ([1, 3, 5], 0)],
        "e09_string_explosion": [("abc", "abbccc"), ("", ""), ("x", "x")],
        "e10_list_average": [([1, 2, 3, 4], 2.5), ([], 0.0)],
        "m01_find_duplicates": [([1, 2, 3, 2, 4, 3], [2, 3])],
        "m02_palindrome_check": [("racecar", True), ("A man a plan a canal Panama", True), ("hello", False)],
        "m03_remove_adjacent_duplicates": [("aabcc", "abc"), ("abc", "abc"), ("aaabbb", "ab")],
        "m04_flatten_matrix": [([[1, 2], [3, 4]], [1, 2, 3, 4])],
        "m05_word_frequency": [("the cat and the dog", {"the": 2, "cat": 1, "and": 1, "dog": 1})],
        "m06_fibonacci_sequence": [(5, [0, 1, 1, 2, 3]), (1, [0]), (0, [])],
        "m07_find_missing_number": [([3, 0, 1], 2), ([0, 1], 2), ([1, 2], 0)],
        "m08_alternating_sum": [([1, 2, 3, 4], -2), ([5], 5)],
        "m09_common_elements": [([1, 2, 3], [2, 3, 4], [2, 3])],
        "m10_rotate_list": [([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])],
        "h01_merge_sorted_lists": [([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6])],
        "h02_longest_increasing_subsequence": [([1, 3, 5, 2, 4, 6, 8], [2, 4, 6, 8]), ([1, 2, 3], [1, 2, 3])],
        "h03_sieve_of_eratosthenes": [(10, [2, 3, 5, 7]), (20, [2, 3, 5, 7, 11, 13, 17, 19])],
        "h04_matrix_multiplication": [([(1, 2), (3, 4)], [(5, 6), (7, 8)], [[19, 22], [43, 50]])],
        "h05_run_length_encoding": [("aaabbc", [("a", 3), ("b", 2), ("c", 1)])],
        "h06_snake_case_to_camel_case": [("hello_world", "helloWorld"), ("foo_bar_baz", "fooBarBaz")],
        "h07_caesar_cipher": [("abc", 1, "bcd"), ("xyz", 3, "abc"), ("ABC", 1, "BCD")],
        "h10_binary_search": [([1, 3, 5, 7, 9], 5, 2), ([1, 3, 5, 7, 9], 2, -1)],
    }

    passed = 0
    total = 0
    func_map = {k: v for k, v in globals().items() if k.startswith(("e0", "m0", "h0", "x0"))}

    for name, cases in tests.items():
        func = func_map.get(name)
        if func is None:
            continue
        for case in cases:
            total += 1
            *args, expected = case
            try:
                result = func(*args)
                if result == expected:
                    passed += 1
                else:
                    print(f"{name}({', '.join(repr(a) for a in args)}) = {result!r}, expected {expected!r}")
            except Exception as e:
                print(f"{name} ERROR: {e}")

    print(f"\n=== {passed}/{total} passed ===")
    if passed == total:
        print("All exercises complete!")
    return passed == total


# ===================== SOLUTIONS =====================

def e01_sum_to_n_solution(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def e02_count_vowels_solution(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


def e03_reverse_string_solution(s):
    result = ""
    for ch in s:
        result = ch + result
    return result


def e04_find_max_solution(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for n in numbers[1:]:
        if n > max_val:
            max_val = n
    return max_val


def e05_count_words_solution(text):
    if not text.strip():
        return 0
    count = 1
    for ch in text.strip():
        if ch == " ":
            count += 1
    return count


def e06_multiplication_table_solution(n):
    return [n * i for i in range(1, 11)]


def e07_countdown_solution(n):
    return list(range(n, 0, -1))


def e08_sum_even_numbers_solution(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total


def e09_string_explosion_solution(s):
    result = ""
    for i, ch in enumerate(s):
        result += ch * (i + 1)
    return result


def e10_list_average_solution(numbers):
    if not numbers:
        return 0.0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def m01_find_duplicates_solution(items):
    seen = set()
    dupes = []
    for item in items:
        if item in seen and item not in dupes:
            dupes.append(item)
        seen.add(item)
    return dupes


def m02_palindrome_check_solution(text):
    cleaned = ""
    for ch in text.lower():
        if ch.isalnum():
            cleaned += ch
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def m03_remove_adjacent_duplicates_solution(s):
    if not s:
        return ""
    result = s[0]
    for ch in s[1:]:
        if ch != result[-1]:
            result += ch
    return result


def m04_flatten_matrix_solution(matrix):
    result = []
    for row in matrix:
        for val in row:
            result.append(val)
    return result


def m05_word_frequency_solution(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq


def m06_fibonacci_sequence_solution(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def m07_find_missing_number_solution(numbers):
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = 0
    for num in numbers:
        actual_sum += num
    return expected_sum - actual_sum


def m08_alternating_sum_solution(numbers):
    total = 0
    for i, n in enumerate(numbers):
        if i % 2 == 0:
            total += n
        else:
            total -= n
    return total


def m09_common_elements_solution(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result


def m10_rotate_list_solution(items, k):
    if not items:
        return items
    k = k % len(items)
    return items[-k:] + items[:-k]


def h01_merge_sorted_lists_solution(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result


def h02_longest_increasing_subsequence_solution(numbers):
    if not numbers:
        return []
    best_start = 0
    best_len = 1
    curr_start = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            if i - curr_start + 1 > best_len:
                best_len = i - curr_start + 1
                best_start = curr_start
        else:
            curr_start = i
    return numbers[best_start:best_start + best_len]


def h03_sieve_of_eratosthenes_solution(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def h04_matrix_multiplication_solution(a, b):
    m = len(a)
    n = len(b)
    p = len(b[0])
    result = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def h05_run_length_encoding_solution(s):
    if not s:
        return []
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append((s[i - 1], count))
            count = 1
    result.append((s[-1], count))
    return result


def h06_snake_case_to_camel_case_solution(s):
    parts = s.split("_")
    result = parts[0]
    for part in parts[1:]:
        result += part.capitalize()
    return result


def h07_caesar_cipher_solution(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result


def h08_tic_tac_toe_valid_solution(board):
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)
    return o_count <= x_count <= o_count + 1


def h09_sudoku_row_validator_solution(grid):
    for row in grid:
        seen = set()
        for val in row:
            if val != 0:
                if val in seen:
                    return False
                seen.add(val)
    return True


def h10_binary_search_solution(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def x01_spiral_matrix_solution(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    return matrix


def x02_n_queens_count_solution(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                count += backtrack(row + 1)
        return count

    board = [-1] * n
    return backtrack(0)


def x03_text_justify_solution(words, max_width):
    def justify_line(line_words, is_last):
        if len(line_words) == 1 or is_last:
            line = " ".join(line_words)
            return line + " " * (max_width - len(line))
        total_chars = sum(len(w) for w in line_words)
        total_spaces = max_width - total_chars
        gaps = len(line_words) - 1
        spaces_per_gap = total_spaces // gaps
        extra = total_spaces % gaps
        result = ""
        for i, word in enumerate(line_words):
            result += word
            if i < gaps:
                spaces = spaces_per_gap + (1 if i < extra else 0)
                result += " " * spaces
        return result

    result = []
    current = []
    current_len = 0
    for word in words:
        if current_len + len(word) + len(current) > max_width:
            result.append(justify_line(current, False))
            current = [word]
            current_len = len(word)
        else:
            current.append(word)
            current_len += len(word)
    if current:
        result.append(justify_line(current, True))
    return result


def x04_sliding_window_max_solution(nums, k):
    if not nums or k <= 0:
        return []
    from collections import deque
    dq = deque()
    result = []
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


def x05_largest_rectangle_in_histogram_solution(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


if __name__ == "__main__":
    if "--solutions" in sys.argv:
        print("Solutions are defined in this file with _solution suffix.")
    else:
        test()
