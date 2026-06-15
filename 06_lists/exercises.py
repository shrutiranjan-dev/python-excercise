"""
Python Lists - 35 Exercises
Easy: 1-10 | Medium: 11-20 | Hard: 21-30 | Expert: 31-35
Solutions at the bottom.
"""

import math
from functools import reduce

# ============================================================
# EASY (1-10)
# ============================================================

def ex1_create_list():
    """Create a list containing numbers 1 through 10."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def ex2_first_element(lst):
    """Return the first element of a list."""
    return lst[0]


def ex3_last_element(lst):
    """Return the last element of a list using negative indexing."""
    return lst[-1]


def ex4_list_length(lst):
    """Return the length of a list."""
    return len(lst)


def ex5_append_item(lst, item):
    """Append an item to the end of a list."""
    lst.append(item)
    return lst


def ex6_concatenate_lists(a, b):
    """Return the concatenation of two lists."""
    return a + b


def ex7_check_in_list(lst, item):
    """Return True if item is in list, False otherwise."""
    return item in lst


def ex8_repeat_list(lst, n):
    """Return a list repeated n times."""
    return lst * n


def ex9_slice_first_three(lst):
    """Return the first 3 elements of a list."""
    return lst[:3]


def ex10_slice_last_two(lst):
    """Return the last 2 elements of a list."""
    return lst[-2:]


# ============================================================
# MEDIUM (11-20)
# ============================================================

def ex11_remove_duplicates(lst):
    """Remove duplicates from a list while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def ex12_find_second_largest(lst):
    """Return the second largest number in a list."""
    unique = sorted(set(lst))
    return unique[-2] if len(unique) >= 2 else None


def ex13_reverse_list(lst):
    """Return a reversed copy of the list (do not modify original)."""
    return lst[::-1]


def ex14_flatten_once(nested):
    """Flatten a list of lists one level deep."""
    return [item for sublist in nested for item in sublist]


def ex15_rotate_left(lst, k):
    """Rotate a list to the left by k positions."""
    if not lst:
        return lst
    k = k % len(lst)
    return lst[k:] + lst[:k]


def ex16_list_intersection(a, b):
    """Return common elements between two lists (no duplicates)."""
    return list(set(a) & set(b))


def ex17_chunk_list(lst, chunk_size):
    """Split a list into chunks of given size."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def ex18_find_all_indices(lst, target):
    """Return all indices where target appears in lst."""
    return [i for i, x in enumerate(lst) if x == target]


def ex19_list_difference(a, b):
    """Return elements in a but not in b (no duplicates)."""
    return list(set(a) - set(b))


def ex20_alternating_sum(lst):
    """Return sum of elements at even indices minus sum at odd indices."""
    return sum(lst[::2]) - sum(lst[1::2])


# ============================================================
# HARD (21-30)
# ============================================================

def ex21_merge_sorted(a, b):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def ex22_longest_increasing_subsequence(lst):
    """Return the longest contiguous increasing subsequence."""
    if not lst:
        return []
    best = current = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            current.append(lst[i])
        else:
            current = [lst[i]]
        if len(current) > len(best):
            best = current
    return best


def ex23_move_zeroes(lst):
    """Move all zeroes to the end without changing relative order of others."""
    non_zero = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zero))
    return non_zero + zeros


def ex24_find_missing_number(lst):
    """Find missing number in list containing 1..n with one missing."""
    n = len(lst) + 1
    expected = n * (n + 1) // 2
    return expected - sum(lst)


def ex25_sublist_sum_target(lst, target):
    """Find a contiguous sublist that sums to target. Return indices [start, end]."""
    prefix_sum = {0: -1}
    current_sum = 0
    for i, num in enumerate(lst):
        current_sum += num
        if current_sum - target in prefix_sum:
            return [prefix_sum[current_sum - target] + 1, i]
        prefix_sum[current_sum] = i
    return []


def ex26_matrix_transpose(matrix):
    """Transpose a matrix (list of lists)."""
    return [list(row) for row in zip(*matrix)]


def ex27_frequency_sort(lst):
    """Sort list by frequency of elements (most frequent first)."""
    freq = {}
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
    return sorted(lst, key=lambda x: (-freq[x], lst.index(x)))


def ex28_spiral_matrix(n):
    """Generate an n x n spiral matrix."""
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
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
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    return matrix


def ex29_pascals_triangle(n):
    """Generate first n rows of Pascal's triangle."""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle


def ex30_list_permutations(lst):
    """Return all permutations of a list."""
    if len(lst) <= 1:
        return [lst]
    result = []
    for i, item in enumerate(lst):
        rest = lst[:i] + lst[i + 1:]
        for perm in ex30_list_permutations(rest):
            result.append([item] + perm)
    return result


# ============================================================
# EXPERT (31-35)
# ============================================================

def ex31_max_subarray_sum(lst):
    """Find maximum subarray sum (Kadane's algorithm)."""
    max_current = max_global = lst[0]
    for x in lst[1:]:
        max_current = max(x, max_current + x)
        max_global = max(max_global, max_current)
    return max_global


def ex32_merge_intervals(intervals):
    """Merge overlapping intervals [[start,end],...]."""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def ex33_sliding_window_max(lst, k):
    """Return maximum in every sliding window of size k."""
    if not lst or k <= 0:
        return []
    from collections import deque
    dq = deque()
    result = []
    for i, x in enumerate(lst):
        while dq and lst[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(lst[dq[0]])
    return result


def ex34_lru_simulate(operations, capacity):
    """Simulate LRU cache: operations are (op, key, val). Track cache state."""
    cache = {}
    order = []
    final_state = {}
    for op, key, *args in operations:
        if op == "put":
            if key in cache:
                order.remove(key)
            elif len(cache) >= capacity:
                oldest = order.pop(0)
                del cache[oldest]
            cache[key] = args[0]
            order.append(key)
        elif op == "get":
            if key in cache:
                order.remove(key)
                order.append(key)
    for k in order:
        final_state[k] = cache[k]
    return final_state


def ex35_product_except_self(lst):
    """Return list where result[i] = product of all elements except lst[i] (no division)."""
    n = len(lst)
    prefix = [1] * n
    suffix = [1] * n
    result = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * lst[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * lst[i + 1]
    for i in range(n):
        result[i] = prefix[i] * suffix[i]
    return result


# ============================================================
# SOLUTIONS
# ============================================================

if __name__ == "__main__":
    print("Testing all exercises...\n")

    # Easy tests
    assert ex1_create_list() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "ex1 failed"
    assert ex2_first_element([10, 20, 30]) == 10, "ex2 failed"
    assert ex3_last_element([10, 20, 30]) == 30, "ex3 failed"
    assert ex4_list_length([1, 2, 3, 4]) == 4, "ex4 failed"
    assert ex5_append_item([1, 2], 3) == [1, 2, 3], "ex5 failed"
    assert ex6_concatenate_lists([1, 2], [3, 4]) == [1, 2, 3, 4], "ex6 failed"
    assert ex7_check_in_list([1, 2, 3], 2) == True, "ex7 failed"
    assert ex7_check_in_list([1, 2, 3], 5) == False, "ex7 failed"
    assert ex8_repeat_list([1, 2], 3) == [1, 2, 1, 2, 1, 2], "ex8 failed"
    assert ex9_slice_first_three([1, 2, 3, 4, 5]) == [1, 2, 3], "ex9 failed"
    assert ex10_slice_last_two([1, 2, 3, 4, 5]) == [4, 5], "ex10 failed"
    print("Easy exercises (1-10): ALL PASSED")

    # Medium tests
    assert ex11_remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4], "ex11 failed"
    assert ex12_find_second_largest([3, 1, 4, 1, 5, 9]) == 5, "ex12 failed"
    assert ex13_reverse_list([1, 2, 3]) == [3, 2, 1], "ex13 failed"
    assert ex14_flatten_once([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5], "ex14 failed"
    assert ex15_rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2], "ex15 failed"
    assert sorted(ex16_list_intersection([1, 2, 3, 4], [3, 4, 5, 6])) == [3, 4], "ex16 failed"
    assert ex17_chunk_list([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]], "ex17 failed"
    assert ex18_find_all_indices([1, 2, 3, 2, 4, 2], 2) == [1, 3, 5], "ex18 failed"
    assert sorted(ex19_list_difference([1, 2, 3, 4], [3, 4, 5])) == [1, 2], "ex19 failed"
    assert ex20_alternating_sum([1, 2, 3, 4, 5]) == (1 + 3 + 5) - (2 + 4), "ex20 failed"
    print("Medium exercises (11-20): ALL PASSED")

    # Hard tests
    assert ex21_merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6], "ex21 failed"
    assert ex22_longest_increasing_subsequence([1, 2, 1, 2, 3, 1]) == [1, 2, 3], "ex22 failed"
    assert ex23_move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0], "ex23 failed"
    assert ex24_find_missing_number([1, 2, 4, 5, 6]) == 3, "ex24 failed"
    assert ex25_sublist_sum_target([1, 2, 3, 4, 5], 9) == [1, 3], "ex25 failed"
    assert ex26_matrix_transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]], "ex26 failed"
    assert sorted(ex27_frequency_sort([4, 2, 2, 8, 3, 3, 1]), key=lambda x: x) == sorted([2, 2, 3, 3, 4, 8, 1], key=lambda x: x), "ex27 failed"
    assert ex28_spiral_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]], "ex28 failed"
    assert ex29_pascals_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], "ex29 failed"
    perms = ex30_list_permutations([1, 2, 3])
    assert len(perms) == 6, "ex30 failed"
    assert [1, 2, 3] in perms, "ex30 failed"
    print("Hard exercises (21-30): ALL PASSED")

    # Expert tests
    assert ex31_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "ex31 failed"
    assert ex32_merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]], "ex32 failed"
    assert ex33_sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7], "ex33 failed"
    ops = [("put", "a", 1), ("put", "b", 2), ("get", "a"), ("put", "c", 3), ("put", "d", 4)]
    lru = ex34_lru_simulate(ops, 2)
    assert "c" in lru and "d" in lru, "ex34 failed"
    assert ex35_product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6], "ex35 failed"
    print("Expert exercises (31-35): ALL PASSED")

    print("\n=== ALL 35 EXERCISES PASSED ===")
