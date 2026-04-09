# 📘 Assignment: Data Structures in Python

## 🎯 Objective

Practice core Python data structures by solving small tasks with lists, dictionaries, sets, and tuples.
Students will organize, transform, and query data using the right structure for each problem.

## 📝 Tasks

### 🛠️ Work with Lists and Tuples

#### Description
Create functions that process ordered data using list operations and immutable tuples.

#### Requirements
Completed program should:

- Implement `summarize_scores(scores)` that returns a tuple `(min_score, max_score, average_score)`.
- Use list methods or comprehensions to filter out invalid scores (less than 0 or greater than 100).
- Print a clear example output for at least one sample list.


### 🛠️ Build a Dictionary-Based Student Lookup

#### Description
Store student records in a dictionary and implement quick lookup/update operations.

#### Requirements
Completed program should:

- Represent students as a dictionary where the key is `student_id` and the value is a nested dictionary with `name` and `grade`.
- Implement `add_or_update_student(records, student_id, name, grade)`.
- Implement `get_student(records, student_id)` that returns student data or a friendly not-found message.


### 🛠️ Use Sets for Unique Data Analysis

#### Description
Use set operations to find unique and shared values across datasets.

#### Requirements
Completed program should:

- Create two sets of course topics completed by two different students.
- Output topics unique to each student and topics they have in common.
- Convert the final shared topics set into a sorted list for display.
