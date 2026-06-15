"""
Python Tuples and Sets - 35 Exercises
Easy: 1-10 | Medium: 11-20 | Hard: 21-30 | Expert: 31-35
Solutions at the bottom.
"""

# ============================================================
# EASY (1-10)
# ============================================================

def ex1_create_tuple():
    """Create a tuple containing numbers 1 through 5."""
    return (1, 2, 3, 4, 5)


def ex2_create_single_element_tuple():
    """Create a tuple with a single element 42."""
    return (42,)


def ex3_tuple_indexing(t, idx):
    """Return element at given index from tuple t."""
    return t[idx]


def ex4_tuple_slicing(t):
    """Return first 3 elements of tuple t."""
    return t[:3]


def ex5_tuple_length(t):
    """Return length of tuple t."""
    return len(t)


def ex6_check_in_tuple(t, item):
    """Return True if item is in tuple t."""
    return item in t


def ex7_create_set():
    """Create a set containing numbers 1 through 5."""
    return {1, 2, 3, 4, 5}


def ex8_set_length(s):
    """Return number of elements in set s."""
    return len(s)


def ex9_add_to_set(s, item):
    """Add item to set s and return the set."""
    s.add(item)
    return s


def ex10_check_in_set(s, item):
    """Return True if item is in set s."""
    return item in s


# ============================================================
# MEDIUM (11-20)
# ============================================================

def ex11_tuple_unpack(t):
    """Unpack tuple t = (a, b, c) into variables and return sum a+b+c."""
    a, b, c = t
    return a + b + c


def ex12_tuple_count(t, target):
    """Count occurrences of target in tuple t."""
    return t.count(target)


def ex13_tuple_index(t, target):
    """Return index of first occurrence of target in tuple t."""
    return t.index(target)


def ex14_remove_duplicates_with_set(lst):
    """Remove duplicates from list using a set, return sorted list."""
    return sorted(set(lst))


def ex15_set_union(a, b):
    """Return union of sets a and b."""
    return a | b


def ex16_set_intersection(a, b):
    """Return intersection of sets a and b."""
    return a & b


def ex17_set_difference(a, b):
    """Return elements in a but not in b."""
    return a - b


def ex18_set_symmetric_difference(a, b):
    """Return symmetric difference of sets a and b."""
    return a ^ b


def ex19_is_subset(a, b):
    """Return True if a is subset of b."""
    return a.issubset(b)


def ex20_is_disjoint(a, b):
    """Return True if sets a and b are disjoint."""
    return a.isdisjoint(b)


# ============================================================
# HARD (21-30)
# ============================================================

def ex21_common_elements(lst1, lst2):
    """Return sorted list of common elements between two lists (use sets)."""
    return sorted(set(lst1) & set(lst2))


def ex22_unique_elements(lst1, lst2):
    """Return sorted list of elements that appear in only one of the lists."""
    return sorted(set(lst1) ^ set(lst2))


def ex23_find_pairs_with_sum(nums, target):
    """Return set of tuples (a,b) where a+b=target, a<b, using set."""
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return pairs


def ex24_tuple_of_tuples_to_dict(pairs):
    """Convert tuple of (key, value) tuples to a dict."""
    return dict(pairs)


def ex25_word_unique_letters(word):
    """Return set of unique letters in a word (case-insensitive)."""
    return set(word.lower())


def ex26_jaccard_similarity(a, b):
    """Compute Jaccard similarity between two sets."""
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)


def ex27_find_missing_letters(sentence):
    """Return set of lowercase letters a-z not present in sentence."""
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    present = set(c.lower() for c in sentence if c.isalpha())
    return alphabet - present


def ex28_merge_tuples(t1, t2):
    """Merge two tuples, remove duplicates, return sorted tuple."""
    return tuple(sorted(set(t1 + t2)))


def ex29_k_common_elements(lst, k):
    """Return set of k most common elements in list."""
    from collections import Counter
    counter = Counter(lst)
    return set(item for item, _ in counter.most_common(k))


def ex30_tuple_to_set_with_condition(t, predicate):
    """Return set of elements from tuple t that satisfy predicate function."""
    return {x for x in t if predicate(x)}


# ============================================================
# EXPERT (31-35)
# ============================================================

def ex31_find_triplets(nums, target):
    """Return set of tuples (a,b,c) where a+b+c=target, a<b<c."""
    nums = sorted(nums)
    n = len(nums)
    triplets = set()
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                triplets.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return triplets


def ex32_longest_consecutive_sequence(nums):
    """Return length of longest consecutive element sequence."""
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            current_streak = 1
            while current + 1 in num_set:
                current += 1
                current_streak += 1
            longest = max(longest, current_streak)
    return longest


def ex33_set_cover(sets, universe):
    """Approximate set cover: return indices of sets that cover universe."""
    uncovered = set(universe)
    selected_indices = []
    available = [(i, s) for i, s in enumerate(sets)]
    while uncovered and available:
        best_idx = max(range(len(available)), key=lambda i: len(available[i][1] & uncovered))
        idx, best_set = available.pop(best_idx)
        selected_indices.append(idx)
        uncovered -= best_set
    return sorted(selected_indices) if not uncovered else []


def ex34_word_break_possibilities(s, word_dict):
    """Return set of possible word sequences using recursive backtracking."""
    word_set = set(word_dict)
    memo = {}

    def helper(remaining):
        if remaining in memo:
            return memo[remaining]
        if not remaining:
            return {()}
        results = set()
        for word in word_set:
            if remaining.startswith(word):
                for rest in helper(remaining[len(word):]):
                    results.add((word,) + rest)
        memo[remaining] = results
        return results

    return helper(s)


def ex35_prime_factors_set(n):
    """Return set of prime factors of n."""
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.add(n)
    return factors


# ============================================================
# SOLUTIONS
# ============================================================

if __name__ == "__main__":
    print("Testing all exercises...\n")

    # Easy tests
    assert ex1_create_tuple() == (1, 2, 3, 4, 5), "ex1 failed"
    assert ex2_create_single_element_tuple() == (42,), "ex2 failed"
    assert ex3_tuple_indexing((10, 20, 30), 1) == 20, "ex3 failed"
    assert ex4_tuple_slicing((1, 2, 3, 4, 5)) == (1, 2, 3), "ex4 failed"
    assert ex5_tuple_length((1, 2, 3)) == 3, "ex5 failed"
    assert ex6_check_in_tuple((1, 2, 3), 2) == True, "ex6 failed"
    assert ex6_check_in_tuple((1, 2, 3), 5) == False, "ex6 failed"
    assert ex7_create_set() == {1, 2, 3, 4, 5}, "ex7 failed"
    assert ex8_set_length({1, 2, 3}) == 3, "ex8 failed"
    assert ex9_add_to_set({1, 2}, 3) == {1, 2, 3}, "ex9 failed"
    assert ex10_check_in_set({1, 2, 3}, 2) == True, "ex10 failed"
    print("Easy exercises (1-10): ALL PASSED")

    # Medium tests
    assert ex11_tuple_unpack((1, 2, 3)) == 6, "ex11 failed"
    assert ex12_tuple_count((1, 2, 2, 3, 2), 2) == 3, "ex12 failed"
    assert ex13_tuple_index((1, 2, 3, 2), 3) == 2, "ex13 failed"
    assert ex14_remove_duplicates_with_set([3, 1, 2, 1, 3]) == [1, 2, 3], "ex14 failed"
    assert ex15_set_union({1, 2}, {2, 3}) == {1, 2, 3}, "ex15 failed"
    assert ex16_set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}, "ex16 failed"
    assert ex17_set_difference({1, 2, 3}, {2, 3}) == {1}, "ex17 failed"
    assert ex18_set_symmetric_difference({1, 2}, {2, 3}) == {1, 3}, "ex18 failed"
    assert ex19_is_subset({1, 2}, {1, 2, 3}) == True, "ex19 failed"
    assert ex19_is_subset({1, 2, 4}, {1, 2, 3}) == False, "ex19 failed"
    assert ex20_is_disjoint({1, 2}, {3, 4}) == True, "ex20 failed"
    assert ex20_is_disjoint({1, 2}, {2, 3}) == False, "ex20 failed"
    print("Medium exercises (11-20): ALL PASSED")

    # Hard tests
    assert ex21_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4], "ex21 failed"
    assert ex22_unique_elements([1, 2, 3, 4], [3, 4, 5]) == [1, 2, 5], "ex22 failed"
    pairs = ex23_find_pairs_with_sum([1, 2, 3, 4, 5], 5)
    assert (1, 4) in pairs and (2, 3) in pairs, "ex23 failed"
    assert ex24_tuple_of_tuples_to_dict((("a", 1), ("b", 2))) == {"a": 1, "b": 2}, "ex24 failed"
    assert ex25_word_unique_letters("Hello") == set("helo"), "ex25 failed"
    assert abs(ex26_jaccard_similarity({1, 2, 3}, {2, 3, 4}) - 0.5) < 0.001, "ex26 failed"
    assert len(ex27_find_missing_letters("abcdefghijklmnopqrstuvwxyz")) == 0, "ex27 failed"
    assert ex28_merge_tuples((1, 2, 3), (3, 4, 5)) == (1, 2, 3, 4, 5), "ex28 failed"
    assert ex29_k_common_elements([1, 1, 1, 2, 2, 3], 2) == {1, 2}, "ex29 failed"
    assert ex30_tuple_to_set_with_condition((1, 2, 3, 4, 5), lambda x: x > 3) == {4, 5}, "ex30 failed"
    print("Hard exercises (21-30): ALL PASSED")

    # Expert tests
    triplets = ex31_find_triplets([-1, 0, 1, 2, -1, -4], 0)
    assert (-1, -1, 2) in triplets or (-1, 0, 1) in triplets, "ex31 failed"
    assert ex32_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4, "ex32 failed"
    sets = [{1, 2}, {2, 3}, {3, 4}, {1, 4}]
    result = ex33_set_cover(sets, {1, 2, 3, 4})
    assert len(result) > 0, "ex33 failed"
    words = ex34_word_break_possibilities("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    assert ("cat", "sand", "dog") in words or ("cats", "and", "dog") in words, "ex34 failed"
    assert ex35_prime_factors_set(12) == {2, 3}, "ex35 failed"
    print("Expert exercises (31-35): ALL PASSED")

    print("\n=== ALL 35 EXERCISES PASSED ===")
