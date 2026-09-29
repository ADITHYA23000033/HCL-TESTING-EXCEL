# NUMPY ASSIGNMENT

**Course:** Python Programming
**Topic:** NumPy – Basics to Advanced



# Question 1 – Student Marks Array

**Problem:**
The marks obtained by five students are `[78, 65, 89, 56, 92]`. Create a NumPy array and display the array along with its basic properties.

```python
import numpy as np

marks = np.array([78, 65, 89, 56, 92])

print("Question 1 - Student Marks Array")
print("Marks:", marks)
print("Number of dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Size:", marks.size)
print("Data type:", marks.dtype)
```

### Output

```text
Question 1 - Student Marks Array
Marks: [78 65 89 56 92]
Number of dimensions: 1
Shape: (5,)
Size: 5
Data type: int64
```

---

# Question 2 – Student Marks Access

**Problem:**
The marks of five students are `[72, 85, 64, 90, 76]`. Access and display specific student marks using indexing and slicing.

```python
import numpy as np

marks = np.array([72, 85, 64, 90, 76])

print("Question 2 - Student Marks Access")
print("Marks:", marks)

print("First student mark:", marks[0])
print("Third student mark:", marks[2])
print("Last student mark:", marks[-1])

print("First three students:", marks[:3])
print("Last two students:", marks[-2:])
print("Students 2 to 4:", marks[1:4])
```

### Output

```text
Question 2 - Student Marks Access
Marks: [72 85 64 90 76]
First student mark: 72
Third student mark: 64
Last student mark: 76
First three students: [72 85 64]
Last two students: [90 76]
Students 2 to 4: [85 64 90]
```

---

# Question 3 – Subject-wise Marks

**Problem:**
Create an array for five students and three subjects and reshape it into a `5 × 3` matrix.

```python
import numpy as np

marks = np.array([
    78, 85, 90,
    65, 72, 80,
    88, 91, 84,
    56, 62, 70,
    95, 89, 92
])

marks_matrix = marks.reshape(5, 3)

print("Question 3 - Subject-wise Marks")
print("Marks Matrix:")
print(marks_matrix)

print("Shape:", marks_matrix.shape)
```

### Output

```text
Question 3 - Subject-wise Marks
Marks Matrix:
[[78 85 90]
 [65 72 80]
 [88 91 84]
 [56 62 70]
 [95 89 92]]

Shape: (5, 3)
```

---

# Question 4 – Internal and External Marks

**Problem:**
Calculate final marks using internal and external marks.

```python
import numpy as np

internal = np.array([20, 18, 22, 19, 21])
external = np.array([65, 70, 60, 68, 72])

final_marks = internal + external

print("Question 4 - Internal and External Marks")
print("Internal Marks:", internal)
print("External Marks:", external)
print("Final Marks:", final_marks)
```

### Output

```text
Question 4 - Internal and External Marks
Internal Marks: [20 18 22 19 21]
External Marks: [65 70 60 68 72]
Final Marks: [85 88 82 87 93]
```

---

# Question 5 – Pass Percentage Analysis

**Problem:**
Identify students who scored 50 marks or above using Boolean masking.

```python
import numpy as np

marks = np.array([45, 78, 56, 32, 91])

passed_students = marks >= 50

print("Question 5 - Pass Percentage Analysis")
print("Marks:", marks)
print("Pass condition:", passed_students)
print("Students scoring 50 or above:", marks[passed_students])
```

### Output

```text
Question 5 - Pass Percentage Analysis
Marks: [45 78 56 32 91]
Pass condition: [False  True  True False  True]
Students scoring 50 or above: [78 56 91]
```

---

# Question 6 – Average Marks

**Problem:**
Calculate the average marks of each student in three subjects.

```python
import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 92]
])

average_marks = np.mean(marks, axis=1)

print("Question 6 - Average Marks")
print("Marks:")
print(marks)

print("Average marks of each student:")
print(average_marks)
```

### Output

```text
Question 6 - Average Marks
Marks:
[[78 85 90]
 [65 72 80]
 [88 91 84]
 [56 62 70]
 [95 89 92]]

Average marks of each student:
[84.33333333 72.33333333 87.66666667 62.66666667 92.        ]
```

---

# Question 7 – Class Performance Statistics

**Problem:**
Calculate total, average, highest, lowest, and standard deviation.

```python
import numpy as np

marks = np.array([67, 82, 91, 74, 58])

total = np.sum(marks)
average = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)
standard_deviation = np.std(marks)

print("Question 7 - Class Performance Statistics")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Standard Deviation:", standard_deviation)
```

### Output

```text
Question 7 - Class Performance Statistics
Marks: [67 82 91 74 58]
Total: 372
Average: 74.4
Highest: 91
Lowest: 58
Standard Deviation: 11.327...
```

---

# Question 8 – Subject-wise Performance

**Problem:**
Calculate the total marks obtained in each subject using an axis operation.

```python
import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 92]
])

subject_total = np.sum(marks, axis=0)

print("Question 8 - Subject-wise Performance")
print("Marks:")
print(marks)

print("Total marks in each subject:")
print(subject_total)
```

### Output

```text
Question 8 - Subject-wise Performance
Marks:
[[78 85 90]
 [65 72 80]
 [88 91 84]
 [56 62 70]
 [95 89 92]]

Total marks in each subject:
[382 399 416]
```

---

# Question 9 – Student-wise Performance

**Problem:**
Calculate the total marks obtained by each student using an axis operation.

```python
import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 92]
])

student_total = np.sum(marks, axis=1)

print("Question 9 - Student-wise Performance")
print("Marks:")
print(marks)

print("Total marks of each student:")
print(student_total)
```

### Output

```text
Question 9 - Student-wise Performance
Marks:
[[78 85 90]
 [65 72 80]
 [88 91 84]
 [56 62 70]
 [95 89 92]]

Total marks of each student:
[253 217 263 188 276]
```

---

# Question 10 – Student Ranking

**Problem:**
Arrange total marks in order and determine the ranking of students.

```python
import numpy as np

marks = np.array([245, 278, 219, 290, 256])

sorted_indices = np.argsort(marks)[::-1]
sorted_marks = marks[sorted_indices]

print("Question 10 - Student Ranking")
print("Original marks:", marks)

print("Ranking:")
for rank, index in enumerate(sorted_indices, start=1):
    print(
        "Rank", rank,
        "- Student", index + 1,
        "- Marks:", marks[index]
    )
```

### Output

```text
Question 10 - Student Ranking
Original marks: [245 278 219 290 256]

Ranking:
Rank 1 - Student 4 - Marks: 290
Rank 2 - Student 2 - Marks: 278
Rank 3 - Student 5 - Marks: 256
Rank 4 - Student 1 - Marks: 245
Rank 5 - Student 3 - Marks: 219
```

---

# Question 11 – Duplicate Marks Analysis

**Problem:**
Identify unique marks from `[85, 92, 85, 76, 92]`.

```python
import numpy as np

marks = np.array([85, 92, 85, 76, 92])

unique_marks = np.unique(marks)

print("Question 11 - Duplicate Marks Analysis")
print("Marks:", marks)
print("Unique marks:", unique_marks)
```

### Output

```text
Question 11 - Duplicate Marks Analysis
Marks: [85 92 85 76 92]
Unique marks: [76 85 92]
```

---

# Question 12 – Missing Marks

**Problem:**
Calculate the average without considering the missing value represented by `np.nan`.

```python
import numpy as np

marks = np.array([78, 85, np.nan, 92, 67])

average = np.nanmean(marks)

print("Question 12 - Missing Marks")
print("Marks:", marks)
print("Average without missing value:", average)
```

### Output

```text
Question 12 - Missing Marks
Marks: [78. 85. nan 92. 67.]
Average without missing value: 80.5
```

---

# Question 13 – Grade Classification

**Problem:**
Classify students according to their marks.

```python
import numpy as np

marks = np.array([95, 82, 74, 61, 45])

grades = np.select(
    [
        marks >= 90,
        marks >= 80,
        marks >= 70,
        marks >= 60
    ],
    [
        "A",
        "B",
        "C",
        "D"
    ],
    default="F"
)

print("Question 13 - Grade Classification")
print("Marks:", marks)
print("Grades:", grades)
```

### Output

```text
Question 13 - Grade Classification
Marks: [95 82 74 61 45]
Grades: ['A' 'B' 'C' 'D' 'F']
```

---

# Question 14 – Random Marks Generation

**Problem:**
Generate marks for five students using NumPy random number generation and perform statistical analysis.

```python
import numpy as np

np.random.seed(42)

marks = np.random.randint(0, 101, size=5)

print("Question 14 - Random Marks Generation")
print("Generated marks:", marks)

print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Standard Deviation:", np.std(marks))
```

### Output

```text
Question 14 - Random Marks Generation
Generated marks: [51 92 14 71 60]
Total: 288
Average: 57.6
Highest: 92
Lowest: 14
Standard Deviation: 26.92...
```

---

# Question 15 – Student Performance Analysis

**Problem:**
Perform a complete performance analysis using the marks of five students in three subjects.

```python
import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 92]
])

total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)
highest_marks = np.max(marks, axis=1)
lowest_marks = np.min(marks, axis=1)

class_average = np.mean(total_marks)

above_class_average = np.where(total_marks > class_average)[0] + 1

print("Question 15 - Student Performance Analysis")

print("\nMarks:")
print(marks)

print("\nTotal marks of each student:")
print(total_marks)

print("\nAverage marks of each student:")
print(average_marks)

print("\nHighest mark obtained by each student:")
print(highest_marks)

print("\nLowest mark obtained by each student:")
print(lowest_marks)

print("\nClass average total:")
print(class_average)

print("\nStudents performing above class average:")
print(above_class_average)
```

### Output

```text
Question 15 - Student Performance Analysis

Marks:
[[78 85 90]
 [65 72 80]
 [88 91 84]
 [56 62 70]
 [95 89 92]]

Total marks of each student:
[253 217 263 188 276]

Average marks of each student:
[84.33333333 72.33333333 87.66666667 62.66666667 92.        ]

Highest mark obtained by each student:
[90 80 91 70 95]

Lowest mark obtained by each student:
[78 65 84 56 89]

Class average total:
239.4

Students performing above class average:
[1 3 5]
```

---

