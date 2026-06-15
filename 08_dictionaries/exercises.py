"""
Python Dictionaries - 35 Exercises
Easy: 1-10 | Medium: 11-20 | Hard: 21-30 | Expert: 31-35
Solutions at the bottom.
"""

from collections import defaultdict, Counter, OrderedDict

# ============================================================
# EASY (1-10)
# ============================================================

def ex1_create_dict():
    """Create a dict with keys 'a', 'b', 'c' and values 1, 2, 3."""
    return {"a": 1, "b": 2, "c": 3}


def ex2_get_value(d, key):
    """Return value for key in dict d using bracket notation."""
    return d[key]


def ex3_get_value_safe(d, key, default=None):
    """Return value for key using .get() with a default."""
    return d.get(key, default)


def ex4_check_key(d, key):
    """Return True if key exists in dict d."""
    return key in d


def ex5_dict_keys(d):
    """Return list of keys in dict d."""
    return list(d.keys())


def ex6_dict_values(d):
    """Return list of values in dict d."""
    return list(d.values())


def ex7_dict_length(d):
    """Return number of key-value pairs in dict d."""
    return len(d)


def ex8_add_key(d, key, value):
    """Add key-value pair to dict d and return the dict."""
    d[key] = value
    return d


def ex9_update_key(d, key, value):
    """Update value for existing key in dict d."""
    d[key] = value
    return d


def ex10_remove_key(d, key):
    """Remove key from dict d using pop and return (dict, removed_value)."""
    val = d.pop(key)
    return d, val


# ============================================================
# MEDIUM (11-20)
# ============================================================

def ex11_dict_from_lists(keys, values):
    """Create dict from two lists (keys and values)."""
    return dict(zip(keys, values))


def ex12_dict_items(d):
    """Return list of (key, value) tuples from dict d."""
    return list(d.items())


def ex13_merge_dicts(a, b):
    """Merge two dicts (b overwrites a). Return new dict."""
    return {**a, **b}


def ex14_invert_dict(d):
    """Swap keys and values. Assume all values are unique."""
    return {v: k for k, v in d.items()}


def ex15_count_chars(s):
    """Return dict counting character frequencies in string s."""
    return {char: s.count(char) for char in set(s)}


def ex16_group_by_first_letter(words):
    """Group words by their first letter using defaultdict(list)."""
    groups = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    return dict(groups)


def ex17_dict_comprehension_squares(n):
    """Return dict {x: x**2 for x in range(n)}."""
    return {x: x**2 for x in range(n)}


def ex18_filter_dict_by_value(d, threshold):
    """Return dict with only items where value > threshold."""
    return {k: v for k, v in d.items() if v > threshold}


def ex19_dict_from_keys(keys, default_value):
    """Create dict from keys list with a default value for each."""
    return dict.fromkeys(keys, default_value)


def ex20_setdefault_example(d, key, value):
    """Use setdefault to set key to value if missing. Return the value."""
    return d.setdefault(key, value)


# ============================================================
# HARD (21-30)
# ============================================================

def ex21_word_frequency(text):
    """Return dict with word frequencies from text string."""
    words = text.lower().split()
    return dict(Counter(words))


def ex22_nested_dict_get(d, keys):
    """Safely get nested value given list of keys (e.g., ['a','b','c'])."""
    current = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current


def ex23_deep_merge(base, override):
    """Deep merge two nested dicts."""
    result = base.copy()
    for key, value in override.items():
        if (key in result and isinstance(result[key], dict)
                and isinstance(value, dict)):
            result[key] = ex23_deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def ex24_sort_dict_by_value(d, reverse=False):
    """Return dict sorted by values (ascending or descending)."""
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def ex25_find_duplicate_values(d):
    """Return list of values that appear more than once in dict."""
    value_counts = Counter(d.values())
    return [val for val, count in value_counts.items() if count > 1]


def ex26_dict_difference(a, b):
    """Return dict of keys in a but not in b, with their values from a."""
    return {k: a[k] for k in a if k not in b}


def ex27_flatten_dict(nested, parent_key="", sep="."):
    """Flatten a nested dict into dot-separated keys."""
    items = []
    for key, value in nested.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(ex27_flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def ex28_unflatten_dict(flat, sep="."):
    """Unflatten dot-separated keys back to nested dict."""
    result = {}
    for key, value in flat.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result


def ex29_top_n_keys(d, n):
    """Return dict of top n keys by value."""
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True)[:n])


def ex30_dict_intersection_keys(dicts):
    """Given list of dicts, return set of keys common to ALL dicts."""
    if not dicts:
        return set()
    return set.intersection(*(set(d.keys()) for d in dicts))


# ============================================================
# EXPERT (31-35)
# ============================================================

def ex31_lru_cache_simulate(operations, capacity):
    """Simulate LRU cache, return final cache state dict.
    operations: list of ('get'|'put', key, [value])"""
    cache = OrderedDict()
    for op, key, *args in operations:
        if op == "put":
            if key in cache:
                del cache[key]
            elif len(cache) >= capacity:
                cache.popitem(last=False)
            cache[key] = args[0] if args else None
        elif op == "get":
            if key in cache:
                cache.move_to_end(key)
    return dict(cache)


def ex32_trie_insert(words):
    """Build a simple trie (prefix tree) from list of words using nested dicts."""
    root = {}
    for word in words:
        current = root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current["$"] = True
    return root


def ex33_graph_adjacency_list(edges):
    """Convert list of (from, to) edges to adjacency list dict."""
    graph = defaultdict(set)
    for frm, to in edges:
        graph[frm].add(to)
        graph[to].add(frm)
    return {k: sorted(v) for k, v in graph.items()}


def ex34_config_diff(a, b, path=""):
    """Recursively find differences between two nested dicts.
    Return list of (change_type, path, old_value, new_value)."""
    diffs = []
    all_keys = set(a.keys()) | set(b.keys())
    for key in sorted(all_keys):
        new_path = f"{path}.{key}" if path else key
        if key not in a:
            diffs.append(("added", new_path, None, b[key]))
        elif key not in b:
            diffs.append(("removed", new_path, a[key], None))
        elif isinstance(a[key], dict) and isinstance(b[key], dict):
            diffs.extend(ex34_config_diff(a[key], b[key], new_path))
        elif a[key] != b[key]:
            diffs.append(("changed", new_path, a[key], b[key]))
    return diffs


def ex35_json_normalize(data, parent_key="", sep="."):
    """Normalize nested JSON-like dict to flat key-value pairs.
    Handles lists by using index in key path."""
    items = []
    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.extend(ex35_json_normalize(value, new_key, sep=sep).items())
    elif isinstance(data, list):
        for i, value in enumerate(data):
            new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            items.extend(ex35_json_normalize(value, new_key, sep=sep).items())
    else:
        items.append((parent_key, data))
    return dict(items)


# ============================================================
# SOLUTIONS
# ============================================================

if __name__ == "__main__":
    print("Testing all exercises...\n")

    # Easy tests
    assert ex1_create_dict() == {"a": 1, "b": 2, "c": 3}, "ex1 failed"
    assert ex2_get_value({"a": 10, "b": 20}, "a") == 10, "ex2 failed"
    assert ex3_get_value_safe({"a": 1}, "b", 0) == 0, "ex3 failed"
    assert ex4_check_key({"a": 1}, "a") == True, "ex4 failed"
    assert ex4_check_key({"a": 1}, "b") == False, "ex4 failed"
    assert sorted(ex5_dict_keys({"b": 2, "a": 1})) == ["a", "b"], "ex5 failed"
    assert sorted(ex6_dict_values({"a": 2, "b": 1})) == [1, 2], "ex6 failed"
    assert ex7_dict_length({"a": 1, "b": 2, "c": 3}) == 3, "ex7 failed"
    assert ex8_add_key({"a": 1}, "b", 2) == {"a": 1, "b": 2}, "ex8 failed"
    assert ex9_update_key({"a": 1}, "a", 10) == {"a": 10}, "ex9 failed"
    d, val = ex10_remove_key({"a": 1, "b": 2}, "a")
    assert d == {"b": 2} and val == 1, "ex10 failed"
    print("Easy exercises (1-10): ALL PASSED")

    # Medium tests
    assert ex11_dict_from_lists(["a", "b"], [1, 2]) == {"a": 1, "b": 2}, "ex11 failed"
    items = ex12_dict_items({"a": 1, "b": 2})
    assert ("a", 1) in items and ("b", 2) in items, "ex12 failed"
    assert ex13_merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}, "ex13 failed"
    assert ex14_invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}, "ex14 failed"
    assert ex15_count_chars("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}, "ex15 failed"
    grouped = ex16_group_by_first_letter(["apple", "banana", "avocado", "blueberry"])
    assert "a" in grouped and "b" in grouped, "ex16 failed"
    assert ex17_dict_comprehension_squares(5) == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}, "ex17 failed"
    assert ex18_filter_dict_by_value({"a": 1, "b": 5, "c": 3}, 2) == {"b": 5, "c": 3}, "ex18 failed"
    assert ex19_dict_from_keys(["a", "b", "c"], 0) == {"a": 0, "b": 0, "c": 0}, "ex19 failed"
    d = {"a": 1}
    val = ex20_setdefault_example(d, "b", 2)
    assert d == {"a": 1, "b": 2} and val == 2, "ex20 failed"
    print("Medium exercises (11-20): ALL PASSED")

    # Hard tests
    freq = ex21_word_frequency("the cat and the dog")
    assert freq == {"the": 2, "cat": 1, "and": 1, "dog": 1}, "ex21 failed"
    nested = {"a": {"b": {"c": 42}}}
    assert ex22_nested_dict_get(nested, ["a", "b", "c"]) == 42, "ex22 failed"
    assert ex22_nested_dict_get(nested, ["a", "x"]) is None, "ex22 failed"
    base = {"a": {"x": 1}, "b": 2}
    override = {"a": {"y": 2}, "c": 3}
    merged = ex23_deep_merge(base, override)
    assert merged == {"a": {"x": 1, "y": 2}, "b": 2, "c": 3}, "ex23 failed"
    sorted_d = ex24_sort_dict_by_value({"a": 3, "b": 1, "c": 2})
    assert list(sorted_d.values()) == [1, 2, 3], "ex24 failed"
    assert sorted(ex25_find_duplicate_values({"a": 1, "b": 2, "c": 1})) == [1], "ex25 failed"
    assert ex26_dict_difference({"a": 1, "b": 2}, {"b": 2}) == {"a": 1}, "ex26 failed"
    flat = ex27_flatten_dict({"a": {"b": 1, "c": 2}, "d": 3})
    assert flat == {"a.b": 1, "a.c": 2, "d": 3}, "ex27 failed"
    unflat = ex28_unflatten_dict({"a.b": 1, "a.c": 2, "d": 3})
    assert unflat == {"a": {"b": 1, "c": 2}, "d": 3}, "ex28 failed"
    top = ex29_top_n_keys({"a": 5, "b": 1, "c": 3, "d": 4}, 2)
    assert top == {"a": 5, "d": 4}, "ex29 failed"
    common = ex30_dict_intersection_keys([{"a": 1, "b": 2}, {"b": 3, "c": 4}])
    assert common == {"b"}, "ex30 failed"
    print("Hard exercises (21-30): ALL PASSED")

    # Expert tests
    ops = [("put", "a", 1), ("put", "b", 2), ("get", "a"), ("put", "c", 3)]
    lru = ex31_lru_cache_simulate(ops, 2)
    assert "a" in lru and "c" in lru and "b" not in lru, "ex31 failed"
    trie = ex32_trie_insert(["cat", "car", "dog"])
    assert "c" in trie and "d" in trie, "ex32 failed"
    assert trie["c"]["a"]["t"]["$"] == True, "ex32 failed"
    graph = ex33_graph_adjacency_list([(1, 2), (2, 3), (1, 3)])
    assert graph[1] == [2, 3], "ex33 failed"
    diffs = ex34_config_diff({"a": 1, "b": 2}, {"a": 1, "b": 3})
    assert len(diffs) == 1 and diffs[0][0] == "changed", "ex34 failed"
    norm = ex35_json_normalize({"a": {"b": [1, 2, 3]}, "c": "hello"})
    assert norm["a.b.0"] == 1 and norm["c"] == "hello", "ex35 failed"
    print("Expert exercises (31-35): ALL PASSED")

    print("\n=== ALL 35 EXERCISES PASSED ===")
