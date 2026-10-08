import pandas as pd
import numpy as np

from functions import calculate_grade, check_result, get_top_students

# Read CSV file
df = pd.read_csv("students.csv")

# Display student data
print("===== STUDENT PERFORMANCE ANALYTICS =====")

print("\nStudent Data:")
print(df)
print("\nFirst 5 Students:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nDescriptive Statistics:")
print(df.describe())

# Calculate Total Marks
df["Total"] = df["Python"] + df["Math"] + df["DBMS"]

# Calculate Average Marks
df["Average"] = df["Total"] / 3

print("\nStudent Performance with Total and Average:")
print(df[[
    "Student_ID",
    "Name",
    "Python",
    "Math",
    "DBMS",
    "Total",
    "Average"
]])
    # Assign grade to each student
df["Grade"] = df["Average"].apply(calculate_grade)
print("\nStudent Grades:")
print(df[["Student_ID", "Name", "Average", "Grade"]])
    
    # Assign Pass/Fail result
df["Result"] = df.apply(check_result, axis=1)

print("\nStudent Results:")
print(df[[
    "Student_ID",
    "Name",
    "Average",
    "Attendance",
    "Grade",
    "Result"
]])

df.apply(check_result, axis=1)

# Overall performance analysis

highest_average = df["Average"].max()

print("\nHighest Average:")
print(highest_average)

lowest_average = df["Average"].min()

print("\nLowest Average:")
print(lowest_average)

class_average = df["Average"].mean()

print("\nOverall Class Average:")
print(class_average)

pass_count = (df["Result"] == "Pass").sum()

print("\nTotal Pass Students:")
print(pass_count)
fail_count = (df["Result"] == "Fail").sum()

print("\nTotal Fail Students:")
print(fail_count)

# Subject-wise performance analysis

python_average = df["Python"].mean()
math_average = df["Math"].mean()
dbms_average = df["DBMS"].mean()

print("\n===== SUBJECT-WISE PERFORMANCE =====")

print("Python Average:", python_average)
print("Math Average:", math_average)
print("DBMS Average:", dbms_average)

# Find the best performing subject

subject_averages = {
    "Python": python_average,
    "Math": math_average,
    "DBMS": dbms_average
}

best_subject = max(subject_averages, key=subject_averages.get)

print("\nBest Performing Subject:", best_subject)

# Find Top 5 Performing Students

top_students = get_top_students(df)

print("\n===== TOP 5 PERFORMING STUDENTS =====")

print(top_students[[
    "Student_ID",
    "Name",
    "Department",
    "Average",
    "Grade"
]])



# NumPy analysis

marks = df[["Python", "Math", "DBMS"]].to_numpy()

print("\n===== NUMPY ANALYSIS =====")

print("Marks Array:")
print(marks)


# Overall marks statistics

overall_mean = np.mean(marks)
highest_mark = np.max(marks)
lowest_mark = np.min(marks)

print("\nOverall Mean Marks:", overall_mean)
print("Highest Individual Mark:", highest_mark)
print("Lowest Individual Mark:", lowest_mark)


# Subject-wise NumPy average

subject_mean = np.mean(marks, axis=0)

print("\nNumPy Subject Averages:")
print("Python:", subject_mean[0])
print("Math:", subject_mean[1])
print("DBMS:", subject_mean[2])

# Loop for subject-wise analysis

subjects = ["Python", "Math", "DBMS"]

print("\n===== LOOP-BASED SUBJECT ANALYSIS =====")

for subject in subjects:
    average = df[subject].mean()
    highest = df[subject].max()
    lowest = df[subject].min()

    print(f"\n{subject}")
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
    
    # Final Project Summary

print("\n")
print("=" * 50)
print("       STUDENT PERFORMANCE SUMMARY")
print("=" * 50)

print(f"Total Students      : {len(df)}")
print(f"Class Average       : {class_average:.2f}")
print(f"Highest Average     : {highest_average:.2f}")
print(f"Lowest Average      : {lowest_average:.2f}")
print(f"Passed Students     : {pass_count}")
print(f"Failed Students     : {fail_count}")
print(f"Best Subject        : {best_subject}")

print("\nTop 5 Performing Students:")
print(top_students[["Name", "Average", "Grade"]].to_string(index=False))

print("\n" + "=" * 50)
print("             ANALYSIS COMPLETED")
print("=" * 50)