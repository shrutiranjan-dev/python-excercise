"""
Student Marks Manager - Complete Solution
A system to manage student marks using Python lists.
"""


class StudentMarksManager:
    """Manages student names and marks using parallel lists."""

    def __init__(self):
        self.names = []
        self.marks = []
        self._grade_boundaries = [
            (90, "A"), (80, "B"), (70, "C"), (60, "D")
        ]

    def add_student(self, name, mark):
        """Add a student with their mark."""
        self.names.append(name)
        self.marks.append(mark)

    def add_students(self, name_list, mark_list):
        """Add multiple students at once."""
        self.names.extend(name_list)
        self.marks.extend(mark_list)

    def get_grade(self, mark):
        """Return letter grade for a given mark."""
        for threshold, grade in self._grade_boundaries:
            if mark >= threshold:
                return grade
        return "F"

    def get_average(self):
        """Calculate average score."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def get_highest(self):
        """Return (name, mark) of highest scoring student."""
        if not self.marks:
            return None, None
        max_mark = max(self.marks)
        idx = self.marks.index(max_mark)
        return self.names[idx], max_mark

    def get_lowest(self):
        """Return (name, mark) of lowest scoring student."""
        if not self.marks:
            return None, None
        min_mark = min(self.marks)
        idx = self.marks.index(min_mark)
        return self.names[idx], min_mark

    def get_sorted_students(self):
        """Return list of (name, mark, grade) sorted by mark descending."""
        paired = list(zip(self.names, self.marks))
        paired.sort(key=lambda x: x[1], reverse=True)
        return [(name, mark, self.get_grade(mark)) for name, mark in paired]

    def get_above_threshold(self, threshold):
        """Return list of (name, mark) for students above threshold."""
        return [(self.names[i], self.marks[i])
                for i in range(len(self.marks))
                if self.marks[i] > threshold]

    def get_below_threshold(self, threshold):
        """Return list of (name, mark) for students below threshold."""
        return [(self.names[i], self.marks[i])
                for i in range(len(self.marks))
                if self.marks[i] < threshold]

    def get_grade_distribution(self):
        """Return dict of grade -> count."""
        distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for mark in self.marks:
            grade = self.get_grade(mark)
            distribution[grade] += 1
        return distribution

    def get_report(self):
        """Generate a formatted performance report."""
        lines = []
        lines.append("=== STUDENT MARKS MANAGER ===")
        lines.append("")

        lines.append("Students:")
        for i, (name, mark) in enumerate(zip(self.names, self.marks), 1):
            lines.append(f"  {i}. {name}: {mark}")

        lines.append("")
        lines.append("--- Statistics ---")
        avg = self.get_average()
        lines.append(f"  Average Score: {avg:.2f}")
        name_h, mark_h = self.get_highest()
        lines.append(f"  Highest Score: {name_h} ({mark_h})")
        name_l, mark_l = self.get_lowest()
        lines.append(f"  Lowest Score: {name_l} ({mark_l})")

        lines.append("")
        lines.append("--- Sorted by Performance ---")
        for i, (name, mark, grade) in enumerate(self.get_sorted_students(), 1):
            lines.append(f"  {i}. {name}: {mark} ({grade})")

        lines.append("")
        lines.append("--- Students Above 80 ---")
        above = self.get_above_threshold(80)
        lines.append("  " + ", ".join(f"{n} ({m})" for n, m in above))

        lines.append("")
        lines.append("--- Students Below 70 ---")
        below = self.get_below_threshold(70)
        lines.append("  " + ", ".join(f"{n} ({m})" for n, m in below))

        lines.append("")
        lines.append("--- Grade Distribution ---")
        dist = self.get_grade_distribution()
        for grade in ["A", "B", "C", "D", "F"]:
            count = dist[grade]
            label = "student" if count == 1 else "students"
            lines.append(f"  {grade}: {count} {label}")

        return "\n".join(lines)

    def update_mark(self, name, new_mark):
        """Update a student's mark by name."""
        if name in self.names:
            idx = self.names.index(name)
            self.marks[idx] = new_mark
            return True
        return False

    def search(self, query):
        """Search students by name (partial match, case-insensitive)."""
        results = []
        for i, name in enumerate(self.names):
            if query.lower() in name.lower():
                results.append((name, self.marks[i], self.get_grade(self.marks[i])))
        return results

    def get_histogram(self):
        """Generate ASCII histogram of grade distribution."""
        dist = self.get_grade_distribution()
        lines = []
        lines.append("Grade Distribution Histogram:")
        for grade in ["A", "B", "C", "D", "F"]:
            bar = "█" * dist[grade]
            lines.append(f"  {grade}: {bar} ({dist[grade]})")
        return "\n".join(lines)


def main():
    manager = StudentMarksManager()

    manager.add_students(
        ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"],
        [85, 92, 78, 95, 63, 71, 88]
    )

    print(manager.get_report())
    print()
    print(manager.get_histogram())

    # Demonstrate update
    print("\n--- Updating Eve's mark from 63 to 75 ---")
    manager.update_mark("Eve", 75)
    print(manager.get_report())

    # Demonstrate search
    print("\n--- Searching for 'a' ---")
    for name, mark, grade in manager.search("a"):
        print(f"  {name}: {mark} ({grade})")


if __name__ == "__main__":
    main()
