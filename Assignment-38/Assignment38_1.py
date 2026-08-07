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