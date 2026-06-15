"""
Word Frequency Analyzer - Complete Solution
Analyze word frequency in text using tuples and sets.
"""

import string
from collections import Counter


class WordFrequencyAnalyzer:
    """Analyzes word frequency in text using tuples and sets."""

    def __init__(self, text=None):
        self.text = text or ""
        self._processed = False

    def load_text(self, text):
        self.text = text
        self._processed = False

    def _clean_word(self, word):
        """Remove punctuation and lowercase a word."""
        return word.strip(string.punctuation).lower()

    def _get_sentences(self):
        """Split text into sentences."""
        sentences = self.text.replace("!", ".").replace("?", ".").split(".")
        return [s.strip() for s in sentences if s.strip()]

    def _process(self):
        """Process text and cache results."""
        if self._processed:
            return

        words = self.text.split()
        self.cleaned_words = [self._clean_word(w) for w in words]
        self.cleaned_words = [w for w in self.cleaned_words if w]

        self.word_count = len(self.cleaned_words)
        self.unique_words = set(self.cleaned_words)
        self.unique_count = len(self.unique_words)
        self.counter = Counter(self.cleaned_words)

        sentences = self._get_sentences()
        self.sentence_word_sets = []
        for sentence in sentences:
            words = [self._clean_word(w) for w in sentence.split()]
            words = [w for w in words if w]
            if words:
                self.sentence_word_sets.append(set(words))

        self._processed = True

    def get_word_count(self):
        """Return total word count."""
        self._process()
        return self.word_count

    def get_unique_words(self):
        """Return set of unique words."""
        self._process()
        return self.unique_words

    def get_unique_count(self):
        """Return number of unique words."""
        self._process()
        return self.unique_count

    def get_most_frequent(self, n=5):
        """Return list of (word, count) tuples for top n words."""
        self._process()
        return self.counter.most_common(n)

    def get_least_frequent(self, n=5):
        """Return list of (word, count) tuples for least n words."""
        self._process()
        return self.counter.most_common()[::-1][:n]

    def get_words_with_frequency(self, min_count=1, max_count=None):
        """Return list of (word, count) tuples filtered by frequency."""
        self._process()
        result = self.counter.most_common()
        if max_count is not None:
            result = [(w, c) for w, c in result if min_count <= c <= max_count]
        else:
            result = [(w, c) for w, c in result if c >= min_count]
        return result

    def get_common_across_sentences(self):
        """Return set of words that appear in ALL sentences."""
        self._process()
        if not self.sentence_word_sets:
            return set()
        return set.intersection(*self.sentence_word_sets)

    def get_words_in_sentence_count(self, min_sentences=2):
        """Return words that appear in at least N sentences."""
        self._process()
        word_sentence_count = Counter()
        for sentence_set in self.sentence_word_sets:
            for word in sentence_set:
                word_sentence_count[word] += 1
        return {word for word, count in word_sentence_count.items()
                if count >= min_sentences}

    def get_sorted_unique_words(self):
        """Return sorted list of unique words."""
        self._process()
        return sorted(self.unique_words)

    def get_report(self):
        """Generate a formatted report."""
        self._process()
        lines = []
        lines.append("=== WORD FREQUENCY ANALYZER ===")
        lines.append("")
        lines.append("Input Text:")
        lines.append(f"  {self.text}")
        lines.append("")
        lines.append("--- Basic Stats ---")
        lines.append(f"  Total Words: {self.word_count}")
        lines.append(f"  Unique Words: {self.unique_count}")
        most_freq = self.get_most_frequent(1)
        if most_freq:
            word, count = most_freq[0]
            lines.append(f"  Most Frequent Word: \"{word}\" ({count} times)")
        lines.append("")
        lines.append("--- Top 5 Most Frequent Words ---")
        for word, count in self.get_most_frequent(5):
            lines.append(f"  {word}: {count}")
        lines.append("")
        lines.append("--- All Unique Words (Sorted) ---")
        unique_sorted = self.get_sorted_unique_words()
        lines.append("  " + ", ".join(unique_sorted))
        lines.append("")
        lines.append("--- Common Words Across All Sentences ---")
        common = self.get_common_across_sentences()
        lines.append("  " + ", ".join(sorted(common)) if common else "  (None)")
        lines.append("")
        lines.append("--- Word Frequency Table ---")
        max_word_len = max(len(w) for w in self.unique_words) if self.unique_words else 10
        for word, count in self.get_most_frequent(15):
            bar = "#" * count
            lines.append(f"  {word:<{max_word_len}} |  {bar} ({count})")

        return "\n".join(lines)

    def get_bigrams(self, n=10):
        """Return most common bigrams (2-word phrases)."""
        self._process()
        words = self.cleaned_words
        bigrams = [f"{words[i]} {words[i+1]}" for i in range(len(words) - 1)]
        counter = Counter(bigrams)
        return counter.most_common(n)

    def get_readability_stats(self):
        """Calculate basic readability statistics."""
        self._process()
        sentences = self._get_sentences()
        num_sentences = len(sentences) if sentences else 1
        avg_words_per_sentence = self.word_count / num_sentences
        avg_letters_per_word = sum(len(w) for w in self.cleaned_words) / self.word_count if self.word_count else 0
        return {
            "sentences": num_sentences,
            "avg_words_per_sentence": round(avg_words_per_sentence, 2),
            "avg_letters_per_word": round(avg_letters_per_word, 2),
            "unique_ratio": round(self.unique_count / self.word_count, 2) if self.word_count else 0,
        }

    def export_as_csv(self):
        """Export word frequencies as CSV string."""
        self._process()
        lines = ["word,count"]
        for word, count in self.counter.most_common():
            lines.append(f"{word},{count}")
        return "\n".join(lines)


def main():
    text = (
        "The cat and the dog played in the park. "
        "The dog chased the cat up a tree. "
        "The cat sat on a branch and watched the dog."
    )

    analyzer = WordFrequencyAnalyzer(text)
    print(analyzer.get_report())

    print("\n")
    print("--- Bigrams ---")
    for bigram, count in analyzer.get_bigrams(5):
        print(f"  \"{bigram}\": {count}")

    print("\n")
    print("--- Readability Stats ---")
    stats = analyzer.get_readability_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    print("\n")
    print("--- CSV Export (first 5 rows) ---")
    csv_lines = analyzer.export_as_csv().split("\n")
    for line in csv_lines[:6]:
        print(f"  {line}")


if __name__ == "__main__":
    main()
