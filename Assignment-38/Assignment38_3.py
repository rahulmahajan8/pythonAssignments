import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# Step 1: Load Dataset
# -----------------------------------------
df = pd.read_csv("student_performance_ml.csv")

print("-" * 50)
print("1. Dataset Information")
print("-" * 50)

print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nTotal Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# -----------------------------------------
# Step 2: Student Count
# -----------------------------------------
print("\n" + "-" * 50)
print("2. Student Statistics")
print("-" * 50)

print("Total Students:", len(df))

passed = (df["FinalResult"] == 1).sum()
failed = (df["FinalResult"] == 0).sum()

print("Passed Students:", passed)
print("Failed Students:", failed)

# -----------------------------------------
# Step 3: Average, Maximum, Minimum
# -----------------------------------------
print("\n" + "-" * 50)
print("3. Calculations")
print("-" * 50)

print("Average StudyHours:", df["StudyHours"].mean())
print("Average Attendance:", df["Attendance"].mean())
print("Maximum PreviousScore:", df["PreviousScore"].max())
print("Minimum SleepHours:", df["SleepHours"].min())