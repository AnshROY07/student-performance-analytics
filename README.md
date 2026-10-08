# Student Performance Analytics System

## Objective

The objective of this project is to develop a Python-based Student Performance Analytics System that analyzes student marks and attendance data.

The system calculates total and average marks, assigns grades, determines pass/fail status, performs subject-wise analysis, and identifies the top-performing students using Pandas and NumPy.

## Technologies Used

- Python
- Pandas
- NumPy
- VS Code
- Git & GitHub

## Dataset

The project uses a CSV dataset named `students.csv`.

The dataset contains information about:

- Student ID
- Student Name
- Department
- Python Marks
- Math Marks
- DBMS Marks
- Attendance

The dataset contains 20 student records and is used for performance analysis.

## Key Features

- Load student data from a CSV file
- Display student information using Pandas
- Calculate total marks
- Calculate average marks
- Assign grades based on average marks
- Determine Pass/Fail status using marks and attendance
- Calculate overall class performance
- Perform subject-wise analysis
- Find the best-performing subject
- Identify the top 5 performing students
- Use NumPy for numerical analysis
- Use functions and loops for data processing

## Implementation

The project is implemented using Python with Pandas and NumPy.

### Pandas
Pandas is used to:
- Read the `students.csv` dataset
- Create and process the DataFrame
- Calculate totals and averages
- Assign grades and results
- Perform sorting and analysis

### NumPy
NumPy is used to:
- Convert subject marks into a NumPy array
- Calculate overall mean marks
- Find highest and lowest marks
- Calculate subject-wise averages

### Functions
Reusable functions are used for:
- Grade calculation
- Pass/Fail checking
- Finding top-performing students

### Loops
Loops are used for subject-wise performance analysis.

## Project Output

The system displays:

- Complete student dataset
- Total and average marks of each student
- Grades of students
- Pass/Fail results
- Highest, lowest, and overall class average
- Subject-wise averages
- Best-performing subject
- Top 5 performing students
- NumPy-based numerical analysis

## Project Structure

```text
student-performance-analytics/
│
├── main.py
├── functions.py
├── students.csv
└── README.md

## Learning Outcomes

Through this project, I learned how to:

- Work with CSV datasets using Pandas
- Perform data analysis using Pandas and NumPy
- Create and use Python functions
- Use loops for data processing
- Calculate student performance metrics
- Analyze subject-wise performance
- Organize a Python project into multiple files
- Use Git and GitHub for project management