# 📘 Assignment: Python Text Processing

## 🎯 Objective

Build practical Python skills for working with text data by combining string operations, file input/output, and reusable text-cleaning logic.
Students will read text from files, transform it, and generate a simple report.

## 📝 Tasks

### 🛠️ Build Text Cleaning Functions

#### Description
Create reusable functions that normalize raw text so it can be analyzed consistently.

#### Requirements
Completed program should:

- Implement a function `clean_text(text)` that converts text to lowercase and removes punctuation.
- Replace multiple spaces with a single space and strip leading/trailing whitespace.
- Return the cleaned text as a string and include at least 2 quick test examples in comments or print output.


### 🛠️ Analyze a Text File

#### Description
Read a text file, apply your cleaning function, and calculate useful summary statistics.

#### Requirements
Completed program should:

- Open a file named `sample.txt` using file I/O and read its content safely.
- Count total words, unique words, and the 5 most frequent words.
- Print results in a clear, labeled format.


### 🛠️ Save Processed Output

#### Description
Export analysis results and cleaned text to output files for later review.

#### Requirements
Completed program should:

- Write the cleaned text to `cleaned_output.txt`.
- Write summary results to `report.txt` (word count, unique words, top 5 words).
- Handle missing input file errors gracefully with a helpful message.
