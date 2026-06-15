# Surprise Project: Student Marks Manager

## Overview
Build a system to manage student marks using Python lists. This project applies list creation, manipulation, sorting, and analysis techniques to solve a real-world grading problem.

## Requirements

1. **Store student data** in parallel lists: `names` (list of strings) and `marks` (list of integers)
2. **Calculate statistics**:
   - Average score
   - Highest score (with student name)
   - Lowest score (with student name)
3. **Sort students** by performance (descending marks)
4. **Threshold filtering**:
   - Find students scoring above a given threshold
   - Find students scoring below a given threshold
5. **Grade assignment** using these boundaries:
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: below 60
6. **Generate a formatted performance report**

## Expected Output

```
=== STUDENT MARKS MANAGER ===

Students:
1. Alice: 85
2. Bob: 92
3. Charlie: 78
4. Diana: 95
5. Eve: 63
6. Frank: 71
7. Grace: 88

--- Statistics ---
Average Score: 81.71
Highest Score: Diana (95)
Lowest Score: Eve (63)

--- Sorted by Performance ---
1. Diana: 95 (A)
2. Bob: 92 (A)
3. Grace: 88 (B)
4. Alice: 85 (B)
5. Charlie: 78 (C)
6. Frank: 71 (C)
7. Eve: 63 (D)

--- Students Above 80 ---
Diana (95), Bob (92), Grace (88), Alice (85)

--- Students Below 70 ---
Eve (63)

--- Grade Distribution ---
A: 2 students
B: 2 students
C: 2 students
D: 1 student
F: 0 students
```

## Hints
- Use `enumerate()` when iterating with index
- `zip()` is helpful for pairing names with marks
- Use list comprehension for threshold filtering
- `max()` and `min()` work on lists of numbers
- Use `sorted()` with `reverse=True` for descending order
- String formatting with f-strings makes report generation cleaner

## Extensions
- Add the ability to **update** a student's marks
- Allow **adding new students** interactively
- Implement **search** by student name (partial match)
- Show **histogram** of grade distribution using ASCII art
- Export report to a **text file**
- Handle **multiple subjects** (use list of lists for marks)
