# Surprise Project: Word Frequency Analyzer

## Overview
Build a text analysis tool that uses tuples and sets to analyze word frequency in a paragraph. This project demonstrates tuple packing/unpacking, set operations for deduplication and comparison, and dictionary-based frequency counting.

## Requirements

1. **Input**: Take a text paragraph (string)
2. **Word splitting**: Split text into words (lowercase, remove punctuation)
3. **Word frequency**: Count how many times each word appears
4. **Unique words**: Show the set of unique words
5. **Common words across sentences**: Split into sentences and find words common to ALL sentences (intersection)
6. **Top N frequent words**: Return the N most frequent words with their counts
7. **Formatted report**: Output a clean formatted report

## Expected Output

```
=== WORD FREQUENCY ANALYZER ===

Input Text:
The cat and the dog played in the park. The dog chased the cat up a tree. 
The cat sat on a branch and watched the dog.

--- Basic Stats ---
Total Words: 23
Unique Words: 12
Most Frequent Word: "the" (5 times)

--- Top 5 Most Frequent Words ---
  the: 5
  cat: 3
  dog: 3
  and: 2
  a: 2

--- All Unique Words (Sorted) ---
  a, and, branch, cat, chased, dog, in, on, park, played, sat, the, tree, up, watched

--- Common Words Across All Sentences ---
  the, cat, dog

--- Word Frequency Table ---
  the      |  #####
  cat      |  ###
  dog      |  ###
  and      |  ##
  a        |  ##
  played   |  #
  in       |  #
  park     |  #
  ...
```

## Hints
- Use `split('.')` or `nltk.sent_tokenize` to get sentences
- `string.punctuation` from the `string` module helps remove punctuation
- Use `set.intersection()` to find common words across sentences
- Use `collections.Counter` for easy frequency counting
- Tuples can store `(word, count)` pairs for sorting
- `sorted(counter.items(), key=lambda x: x[1], reverse=True)` sorts by frequency

## Extensions
- Support **file input** instead of hardcoded text
- Generate a **word cloud** (simple ASCII version)
- Calculate **readability score** (avg words per sentence, etc.)
- Find **bigrams** (2-word phrases) and their frequencies
- Export report as **CSV or JSON**
- Support **multiple languages** (handle Unicode text)
