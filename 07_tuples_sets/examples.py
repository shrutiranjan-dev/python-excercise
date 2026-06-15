"""
Python Tuples and Sets - Examples
Level 0-5: From basics to production-ready code.
Run: python examples.py
"""

print("=" * 60)
print("LEVEL 0: Basic Tuple Creation")
print("=" * 60)

# Creating tuples
empty = ()
single = (5,)
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
nested = ((1, 2), (3, 4), (5, 6))

print(f"Empty tuple: {empty}")
print(f"Single element: {single}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Nested: {nested}")

# Tuple packing (no parentheses)
packed = 10, 20, 30
print(f"Packed tuple: {packed}")

# Tuple immutability
print(f"\nnested[0]: {nested[0]}")
print(f"nested[0][1]: {nested[0][1]}")

# Indexing and slicing (same as lists)
print(f"\nnumbers[0]: {numbers[0]}")
print(f"numbers[-1]: {numbers[-1]}")
print(f"numbers[1:4]: {numbers[1:4]}")

# Tuple methods
t = (1, 2, 3, 2, 4, 2, 5)
print(f"\nt.count(2): {t.count(2)}")
print(f"t.index(3): {t.index(3)}")
print(f"len(t): {len(t)}")

print("\n" + "=" * 60)
print("LEVEL 1: Tuple Unpacking")
print("=" * 60)

# Basic unpacking
point = (3, 4)
x, y = point
print(f"Point: {point}, x={x}, y={y}")

# Multiple return values
def min_max(lst):
    return min(lst), max(lst)

vals = [3, 1, 4, 1, 5, 9, 2, 6]
low, high = min_max(vals)
print(f"List: {vals}")
print(f"Min: {low}, Max: {high}")

# Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print(f"\nExtended unpacking:")
print(f"first={first}, rest={rest}")

first, *middle, last = (1, 2, 3, 4, 5)
print(f"first={first}, middle={middle}, last={last}")

# Swapping
a, b = 10, 20
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Named tuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y", "z"])
p = Point(1, 2, 3)
print(f"\nNamed tuple: Point(x={p.x}, y={p.y}, z={p.z})")
print(f"As tuple: {tuple(p)}")

print("\n" + "=" * 60)
print("LEVEL 2: Basic Set Operations")
print("=" * 60)

# Creating sets
empty = set()
fruits = {"apple", "banana", "cherry", "date"}
numbers = set([1, 2, 2, 3, 3, 3, 4])
print(f"Empty set: {empty}")
print(f"Fruits: {fruits}")
print(f"Numbers (no duplicates): {numbers}")

# Adding and removing
s = {1, 2, 3}
s.add(4)
print(f"\nAfter add(4): {s}")
s.remove(2)
print(f"After remove(2): {s}")
s.discard(10)  # no error
print(f"After discard(10): {s}")
popped = s.pop()
print(f"After pop(), got: {popped}, set: {s}")

# Set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"\na = {a}")
print(f"b = {b}")
print(f"Union:          a | b = {a | b}")
print(f"Intersection:   a & b = {a & b}")
print(f"Difference:     a - b = {a - b}")
print(f"Difference:     b - a = {b - a}")
print(f"Sym Diff:       a ^ b = {a ^ b}")

# Subset/superset
x = {1, 2}
y = {1, 2, 3, 4}
print(f"\nx = {x}, y = {y}")
print(f"x.issubset(y): {x.issubset(y)}")
print(f"y.issuperset(x): {y.issuperset(x)}")
print(f"x.isdisjoint({5}): {x.isdisjoint({5})}")

# Set comprehension
squares = {x**2 for x in range(10)}
print(f"\nSet comprehension: {squares}")

# Frozen set
fs = frozenset([1, 2, 3])
print(f"Frozen set: {fs}")

print("\n" + "=" * 60)
print("LEVEL 3: Unique Document IDs in RAG Pipeline")
print("=" * 60)

class RAGRetriever:
    """Simulated RAG pipeline with deduplication."""

    def __init__(self):
        self.documents = {}
        self.doc_counter = 0

    def add_document(self, text, metadata=None):
        self.doc_counter += 1
        doc_id = f"doc_{self.doc_counter}"
        self.documents[doc_id] = {
            "text": text,
            "metadata": metadata or {}
        }
        return doc_id

    def search(self, query, n=3):
        """Simulate retrieving top-n documents."""
        doc_ids = list(self.documents.keys())[:n * 2]
        return doc_ids[:n]

    def retrieve_unique(self, queries):
        """Retrieve documents across multiple queries, deduplicated."""
        all_ids = []
        for query in queries:
            results = self.search(query)
            all_ids.extend(results)
        return list(set(all_ids))

    def retrieve_common(self, queries):
        """Retrieve documents present in ALL query results."""
        if not queries:
            return set()
        sets = [set(self.search(q)) for q in queries]
        return set.intersection(*sets)

    def compute_overlap(self, query_a, query_b):
        """Compute Jaccard similarity between two query results."""
        docs_a = set(self.search(query_a, n=5))
        docs_b = set(self.search(query_b, n=5))
        if not docs_a and not docs_b:
            return 1.0
        intersection = docs_a & docs_b
        union = docs_a | docs_b
        return len(intersection) / len(union)


retriever = RAGRetriever()

retriever.add_document("Python is a programming language.", {"type": "tutorial"})
retriever.add_document("Python lists are ordered collections.", {"type": "reference"})
retriever.add_document("Sets in Python store unique elements.", {"type": "reference"})
retriever.add_document("Tuples are immutable sequences.", {"type": "reference"})
retriever.add_document("Dictionaries map keys to values.", {"type": "reference"})
retriever.add_document("List comprehensions are Pythonic.", {"type": "tutorial"})

queries = ["Python lists", "Python data structures", "Python collections"]
unique = retriever.retrieve_unique(queries)
print(f"Unique docs across {len(queries)} queries: {unique}")

common = retriever.retrieve_common(queries)
print(f"Docs common to all queries: {common}")

overlap = retriever.compute_overlap("Python", "data structures")
print(f"Overlap (Jaccard) between queries: {overlap:.2f}")

print("\n" + "=" * 60)
print("LEVEL 4: Vocabulary Overlap Analysis")
print("=" * 60)

class VocabularyAnalyzer:
    """Analyze vocabulary overlap between text sources."""

    def __init__(self):
        self.corpora = {}

    def add_corpus(self, name, text):
        """Add a text corpus with given name."""
        words = set(
            word.lower().strip(".,!?;:\"()[]")
            for word in text.split()
        )
        words.discard("")
        self.corpora[name] = words

    def unique_words(self, corpus_name):
        return self.corpora.get(corpus_name, set())

    def common_words(self, *corpora):
        if not corpora:
            return set()
        return set.intersection(*(self.corpora[c] for c in corpora))

    def union_words(self, *corpora):
        if not corpora:
            return set()
        return set.union(*(self.corpora[c] for c in corpora))

    def vocab_overlap(self, a, b):
        """Jaccard similarity between two corpora."""
        set_a = self.corpora.get(a, set())
        set_b = self.corpora.get(b, set())
        if not set_a and not set_b:
            return 1.0
        return len(set_a & set_b) / len(set_a | set_b)

    def unique_to_corpus(self, corpus_name, reference_name):
        """Words in corpus but not in reference."""
        return self.corpora.get(corpus_name, set()) - self.corpora.get(reference_name, set())

    def summary(self):
        lines = []
        for name, words in self.corpora.items():
            lines.append(f"{name}: {len(words)} unique words")
        return "\n".join(lines)


analyzer = VocabularyAnalyzer()

analyzer.add_corpus("python_docs", "Python is a programming language Python is easy to learn")
analyzer.add_corpus("js_docs", "JavaScript is a programming language for web development")
analyzer.add_corpus("ml_docs", "Machine learning is a subset of artificial intelligence Python is popular for ML")

print("Corpus Summary:")
print(analyzer.summary())

print(f"\nCommon words (all): {analyzer.common_words('python_docs', 'js_docs', 'ml_docs')}")
print(f"Union words (python + js): {analyzer.union_words('python_docs', 'js_docs')}")
print(f"Python-JS overlap: {analyzer.vocab_overlap('python_docs', 'js_docs'):.2f}")
print(f"Python-ML overlap: {analyzer.vocab_overlap('python_docs', 'ml_docs'):.2f}")
print(f"Unique to ML: {analyzer.unique_to_corpus('ml_docs', 'python_docs')}")

print("\n" + "=" * 60)
print("LEVEL 5: Data Deduplication Pipeline")
print("=" * 60)

import hashlib
import json
from datetime import datetime


class DeduplicationPipeline:
    """Production-ready data deduplication pipeline."""

    def __init__(self):
        self.seen_hashes = set()
        self.duplicates = []
        self.unique_records = []

    def _compute_hash(self, record, fields=None):
        """Compute hash of record for deduplication."""
        if fields:
            relevant = {k: record[k] for k in fields if k in record}
        else:
            relevant = record
        content = json.dumps(relevant, sort_keys=True, default=str)
        return hashlib.sha256(content.encode()).hexdigest()

    def deduplicate_exact(self, records, fields=None):
        """Remove exact duplicates based on fields (or all fields)."""
        seen = set()
        unique = []
        dups = []
        for record in records:
            h = self._compute_hash(record, fields)
            if h not in seen:
                seen.add(h)
                unique.append(record)
            else:
                dups.append(record)
        self.unique_records = unique
        self.duplicates = dups
        return unique, dups

    def deduplicate_fuzzy(self, records, key, threshold=0.8):
        """Simple fuzzy dedup based on Jaccard similarity of word sets."""
        unique = []
        dups = []
        seen_sets = []

        for record in records:
            words = set(record.get(key, "").lower().split())
            is_dup = False
            for existing_set in seen_sets:
                if not words or not existing_set:
                    continue
                jaccard = len(words & existing_set) / len(words | existing_set)
                if jaccard >= threshold:
                    dups.append(record)
                    is_dup = True
                    break
            if not is_dup:
                seen_sets.append(words)
                unique.append(record)

        return unique, dups

    def hash_set_stats(self):
        return {
            "total_seen": len(self.seen_hashes),
            "total_unique": len(self.unique_records),
            "total_duplicates": len(self.duplicates),
        }

    def union_with(self, other_pipeline):
        """Merge with another pipeline's seen hashes."""
        self.seen_hashes = self.seen_hashes | other_pipeline.seen_hashes

    def clear(self):
        self.seen_hashes.clear()
        self.duplicates.clear()
        self.unique_records.clear()


pipeline = DeduplicationPipeline()

records = [
    {"id": 1, "title": "Python Lists", "content": "About lists", "author": "Alice"},
    {"id": 2, "title": "Python Lists", "content": "About lists", "author": "Alice"},
    {"id": 3, "title": "Python Sets", "content": "About sets", "author": "Bob"},
    {"id": 4, "title": "Python Tuples", "content": "About tuples", "author": "Charlie"},
    {"id": 5, "title": "Python Sets", "content": "About sets", "author": "Bob"},
]

print(f"Total records: {len(records)}")
unique, dups = pipeline.deduplicate_exact(records, fields=["title", "content"])
print(f"Unique (by title+content): {len(unique)}")
for u in unique:
    print(f"  {u['title']} - {u['author']}")
print(f"Duplicates: {len(dups)}")
for d in dups:
    print(f"  {d['title']} - {d['author']}")

print(f"\nHash set stats: {pipeline.hash_set_stats()}")

# Fuzzy dedup example
fuzzy_records = [
    {"text": "Python is a great programming language"},
    {"text": "Python is a great programming language"},
    {"text": "Python is an awesome programming language"},
    {"text": "JavaScript is for web development"},
]

unique_f, dups_f = pipeline.deduplicate_fuzzy(fuzzy_records, "text", threshold=0.6)
print(f"\nFuzzy dedup:")
print(f"  Unique: {len(unique_f)}")
for u in unique_f:
    print(f"    {u['text']}")
print(f"  Duplicates: {len(dups_f)}")
for d in dups_f:
    print(f"    {d['text']}")

print("\nAll examples completed successfully!")
