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

# -----------------------------------------
# Step 4: Value Counts and Percentage
# -----------------------------------------
print("\n" + "-" * 50)
print("4. FinalResult Distribution")
print("-" * 50)

counts = df["FinalResult"].value_counts()
percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("\nCounts:")
print(counts)

print("\nPercentage:")
print(percentage)

if abs(percentage[1] - percentage[0]) <= 10:
    print("\nDataset is Balanced.")
else:
    print("\nDataset is Not Balanced.")