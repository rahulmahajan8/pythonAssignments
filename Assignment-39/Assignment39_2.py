# ==========================================================
# Decision Tree Classifier - Student Performance Prediction
# ==========================================================

# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ==========================================================
# Step 2: Load Dataset
# ==========================================================

data = pd.read_csv("student_performance_ml.csv")

print("First 5 Records:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())


# ==========================================================
# Step 3: Data Analysis
# ==========================================================

print("\nStatistical Summary:")
print(data.describe())

print("\nClass Distribution:")
print(data["FinalResult"].value_counts())

# ==========================================================
# Step 4: Visualization
# ==========================================================

plt.figure(figsize=(6,4))
data["FinalResult"].value_counts().plot(kind="bar", color=["red","green"])
plt.title("Pass and Fail Count")
plt.xlabel("Final Result")
plt.ylabel("Students")
plt.show()

# ==========================================================
# Step 5: Train-Test Split
# ==========================================================

X = data[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

y = data["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
